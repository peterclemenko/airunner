import os

from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QSize

from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.llm.templates.loading_ui import Ui_loading_message


class LoadingWidget(BaseWidget):
    widget_class_ = Ui_loading_message

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        HERE = os.path.dirname(os.path.abspath(__file__))
        movie = QMovie(os.path.join(HERE, "../../icons/dark/Spinner-1s-200px.gif"))
        movie.setScaledSize(QSize(64, 64))  # Resize the GIF
        self.ui.label.setMovie(movie)  # Set the QMovie object to the label
        movie.start()  # Start the animation