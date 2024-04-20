from typing import Callable
from PySide6.QtCore import QObject, Signal as BaseSignal, Slot
from airunner.enums import SignalCode


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Signal(QObject):
    """
    This class represents a signal that can be emitted and received.
    """
    signal = BaseSignal(dict)

    def __init__(self, callback: Callable):
        super().__init__()
        self.callback = callback

        self.signal.connect(self.on_signal_received)

    @Slot(object)
    def on_signal_received(self, data: dict):
        self.callback(data)


SIGNALS = {}

class SignalMediator(metaclass=SingletonMeta):
    """
    This class is responsible for mediating signals between classes.
    """

    def register(
        self,
        code: SignalCode,
        slot_function: Callable
    ):
        """
        Register a signal to be received by a class.

        :param code: The SignalCode of the signal to register
        :param slot_function: The function to call when the signal is received.
        """
        # Create a new Signal instance for this signal name
        if code not in SIGNALS:
            SIGNALS[code] = []
        SIGNALS[code].append(Signal(callback=slot_function))

    def emit_signal(
        self,
        code: SignalCode,
        data: object = None
    ):
        """
        Emit a signal.
        :param code:
        :param data:
        :return:
        """
        data = {} if data is None else data
        if code in SIGNALS:
            for signal in SIGNALS[code]:
                signal.signal.emit(data)
