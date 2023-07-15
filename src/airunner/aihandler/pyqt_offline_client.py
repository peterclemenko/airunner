import json
import traceback

from airunner.aihandler.logger import logger
import queue
import time
from PyQt6 import QtCore
from PyQt6.QtCore import QThread
from airunner.aihandler.qtvar import BooleanVar
from airunner.aihandler.settings import LOG_LEVEL


class OfflineClient(QtCore.QObject):
    sd_runner = None
    llm_runner = None
    app = None
    current_txt2img_model = None
    current_inpaint_model = None
    request_signal_status = QtCore.pyqtSignal(str)
    response_signal_status = QtCore.pyqtSignal(str)
    response_worker = None
    request_worker = None
    response_worker_thread = None
    request_worker_thread = None

    @property
    def message(self):
        """
        Does nothing. Only used for the setter.
        """
        return ""

    @message.setter
    def message(self, msg):
        """
        Set the message property
        """
        if msg == "cancel":
            self.logger.info("cancel message recieved")
            self.cancel()
        else:
            self.logger.info("Putting message in queue")
            self.queue.put(msg)

    @property
    def response(self):
        """
        Get the response from the server
        :return: response string
        """
        return ""

    @response.setter
    def response(self, msg):
        """
        Set the response
        :param msg:
        :return: None
        """
        self.res_queue.put(msg)

    def cancel(self):
        self.sd_runner.cancel()

    def __init__(self, **kwargs):
        super().__init__(
            parent=kwargs.get("parent", None)
        )
        # self.load_extensions = kwargs.get("load_extensions", True)  TODO: extensions
        self.quit_event = BooleanVar()
        self.queue = queue.Queue()
        self.res_queue = queue.Queue()
        self.quit_event.set(False)
        self.logger = logger
        self.logger.set_level(kwargs.get("log_level"))
        self.runners = kwargs.get("runners", [])
        self.message_var = kwargs.get("message_var")
        self.runner_type = kwargs.get("runner_type", "sd")
        self.do_start()

    def do_start(self):
        self.force_request_worker_reset()

    def handle_response(self, response):
        """
        Handle the response from the server
        :param response:
        :return: None
        """
        res = json.loads(response.decode("utf-8"))
        if "response" in res:
            self.response = response
        else:
            self.message = response

    def handle_error(self, error):
        traceback.print_exc()
        self.logger.error(error)

    def handle_sd_request(self, action, data):
        model = None
        model = data["options"][f"{data['action']}_model"]
        # on model change, reload the runner
        if (action in ("txt2img", "img2img") and self.current_txt2img_model != model) or (
                action in ("inpaint", "outpaint") and self.current_inpaint_model != model):
            do_reload = False
            if action in ("txt2img", "img2img"):
                if self.current_txt2img_model is not None:
                    do_reload = True
                self.current_txt2img_model = model
            elif action in ("inpaint", "outpaint"):
                if self.current_inpaint_model is not None:
                    do_reload = True
                self.current_inpaint_model = model
            if do_reload:
                # self.init_sd_runner()
                self.sd_runner.initialized = False
                self.sd_runner.reload_model = True

        if (action in ("txt2img", "img2img") and self.sd_runner.action in ("inpaint", "outpaint")) or \
                (action in ("inpaint", "outpaint") and self.sd_runner.action in ("txt2img", "img2img")):
            self.sd_runner.initialized = False

        self.sd_runner.generator_sample(data)

    def callback(self, data):
        action = data.get("action")
        if action in ("llm"):
            self.llm_request_handler(**data)
        else:
            self.handle_sd_request(action, data)


    def create_worker_thread(self):
        # start worker in a new thread using the self.worker method
        self.response_worker = ResponseWorker(client=self)
        self.request_worker = RequestWorker(client=self, callback=self.callback)
        self.response_worker_thread = QThread()
        self.response_worker_thread.started.connect(self.response_worker.startWork)
        self.request_worker_thread = QThread()
        self.request_worker_thread.started.connect(self.request_worker.startWork)
        self.response_worker_thread.start()
        self.request_worker_thread.start()
        self.response_worker.moveToThread(self.response_worker_thread)
        self.request_worker.moveToThread(self.request_worker_thread)
        self.response_worker.signalStatus.connect(self.request_signal_status)
        self.request_worker.signalStatus.connect(self.response_signal_status)

    def force_request_worker_reset(self):
        if self.request_worker_thread and self.request_worker_thread.isRunning():
            print('Terminating thread.')
            self.request_worker_thread.terminate()

            print('Waiting for thread termination.')
            self.request_worker_thread.wait()

            self.request_signal_status.emit('Idle.')

        if self.response_worker_thread and self.response_worker_thread.isRunning():
            print('Terminating thread.')
            self.response_worker_thread.terminate()

            print('Waiting for thread termination.')
            self.response_worker_thread.wait()

            self.response_signal_status.emit('Idle.')

        self.create_worker_thread()

    def force_request_worker_quit(self):
        if self.request_worker_thread.isRunning():
            self.request_worker_thread.terminate()
            self.request_worker_thread.wait()

    def cancel_current_request(self):
        # cancel the current operation
        pass


class RequestWorker(QtCore.QObject):
    client: OfflineClient
    signalStatus = QtCore.pyqtSignal(str)
    running = False

    def __init__(self, parent=None, client=None, callback=None):
        self.client = client
        super(self.__class__, self).__init__(None)
        self.callback = callback

    @QtCore.pyqtSlot()
    def startWork(self):
        self.running = True
        while self.running:
            # check if we are connected to server
            if not self.client.queue.empty():
                try:
                    msg = self.client.queue.get(timeout=1)
                except queue.Empty:
                    msg = None
                if msg == "quit":
                    # self.parent.quit_event.set(True)
                    # break
                    pass
                self.callback(msg)
            time.sleep(0.01)


class ResponseWorker(QtCore.QObject):
    client: OfflineClient
    signalStatus = QtCore.pyqtSignal(str)
    running = False

    def __init__(self, parent=None, client=None):
        logger.set_level(LOG_LEVEL)
        self.client = client
        super(self.__class__, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startWork(self):
        self.running = True
        while self.running:
            try:
                msg = self.client.res_queue.get(timeout=1)
            except queue.Empty:
                msg = None
            if msg != "" and msg is not None:
                self.client.handle_response(msg)
