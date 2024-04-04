import os

import requests
from json.decoder import JSONDecodeError
from PySide6.QtCore import QThread
from airunner.aihandler.stablediffusion.download_worker import DownloadWorker


class DownloadCivitAI:
    def __init__(self):
        self.thread = None
        self.worker = None
        self.file_name = None

    @staticmethod
    def get_json(model_id):
        # if model_id == id/name split and get the id
        if "/" in model_id:
            model_id = model_id.split("/")[0]
        url = f"https://civitai.com/api/v1/models/{model_id}"
        response = requests.get(url)
        json = None
        try:
            json = response.json()
        except JSONDecodeError:
            print(f"Failed to decode JSON from {url}")
            print(response)
        return json

    def download_model(self, url, file_name, size_kb, callback):
        self.file_name = file_name
        self.worker = DownloadWorker(url, file_name, size_kb)
        self.thread = QThread()

        self.worker.moveToThread(self.thread)

        # Connect signals
        self.worker.finished.connect(self.thread.quit)
        self.worker.progress.connect(lambda current, total: callback(current, total))
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.started.connect(self.worker.download)
        self.thread.start()

    def remove_file(self):
        if os.path.exists(self.file_name):  # Check if the file exists and delete if so
            os.remove(self.file_name)
            print(f"Download of {self.file_name} was cancelled and the file has been deleted.")

    def stop_download(self):
        if self.worker:
            self.worker.cancel()
            self.remove_file()
