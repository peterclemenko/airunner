from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QSizePolicy

from airunner.aihandler.enums import EngineResponseCode
from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.embeddings.embedding_widget import EmbeddingWidget
from airunner.widgets.embeddings.templates.embeddings_container_ui import Ui_embeddings_container


class EmbeddingsContainerWidget(BaseWidget):
    widget_class_ = Ui_embeddings_container
    _embedding_names = None
    embedding_widgets = {}
    bad_model_embedding_map = {}
    search_filter = ""
    spacer = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register("message_handler_signal", self)

        self.scan_for_embeddings()
    
    def on_message_handler_signal(self, message):
        self.message_handler(message)

    def disable_embedding(self, name, model_name):
        if name not in self.embedding_widgets:
            return
        self.embedding_widgets[name].setEnabled(False)
        if name not in self.bad_model_embedding_map:
            self.bad_model_embedding_map[name] = []
        if model_name not in self.bad_model_embedding_map[name]:
            self.bad_model_embedding_map[name].append(model_name)

    def register_embedding_widget(self, name, widget):
        self.embedding_widgets[name] = widget

    def enable_embeddings(self):
        for name in self.embedding_widgets.keys():
            enable = True
            if name in self.bad_model_embedding_map:
                if self.app.model in self.bad_model_embedding_map[name]:
                    enable = False
            self.embedding_widgets[name].setEnabled(enable)

    def handle_embedding_load_failed(self, message):
        # TODO:
        #  on model change, re-enable the buttons
        embedding_name = message["embedding_name"]
        model_name = message["model_name"]
        self.disable_embedding(embedding_name, model_name)

    def update_embedding_names(self):
        self._embedding_names = None
        for tab_name in self.app.tabs.keys():
            tab = self.app.tabs[tab_name]
            # clear embeddings
            try:
                tab.embeddings.widget().deleteLater()
            except AttributeError:
                pass
            self.load_embeddings(tab)

    @pyqtSlot(dict)
    def message_handler(self, response: dict):
        code = response["code"]
        message = response["message"]
        if code == EngineResponseCode.EMBEDDING_LOAD_FAILED:
            self.handle_embedding_load_failed(message)

    def load_embeddings(self):
        self.clear_embedding_widgets()
        
        embeddings = self.app.get_embeddings(self.search_filter)
        
        for embedding in embeddings:
            self.add_embedding(embedding)
        
        if not self.spacer:
            self.spacer = QWidget()
            self.spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.scrollAreaWidgetContents.layout().addWidget(self.spacer)

    def add_embedding(self, embedding):
        embedding_widget = EmbeddingWidget(embedding=embedding)
        self.register_embedding_widget(embedding["name"], embedding_widget)
        self.ui.scrollAreaWidgetContents.layout().addWidget(embedding_widget)

    def action_clicked_button_scan_for_embeddings(self):
        self.scan_for_embeddings()
    
    def check_saved_embeddings(self):
        self.app.delete_missing_embeddings()

    def scan_for_embeddings(self):
        self.app.scan_for_embeddings()
        self.load_embeddings()

    def toggle_all_toggled(self, checked):
        for i in range(self.ui.embeddings.widget().layout().count()):
            widget = self.ui.embeddings.widget().layout().itemAt(i).widget()
            if widget:
                try:
                    widget.ui.enabledCheckbox.setChecked(checked)
                except AttributeError:
                    continue

    def search_text_changed(self, val):
        self.search_filter = val
        self.clear_embedding_widgets()
        self.load_embeddings()
    
    def clear_embedding_widgets(self):
        if self.spacer:
            self.ui.scrollAreaWidgetContents.layout().removeWidget(self.spacer)
        for i in reversed(range(self.ui.scrollAreaWidgetContents.layout().count())):
            widget = self.ui.scrollAreaWidgetContents.layout().itemAt(i).widget()
            if isinstance(widget, EmbeddingWidget):
                widget.deleteLater()
