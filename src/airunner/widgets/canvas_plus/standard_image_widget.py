from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QImage

from PIL import Image

from airunner.widgets.canvas_plus.standard_base_widget import StandardBaseWidget
from airunner.widgets.canvas_plus.templates.standard_image_widget_ui import Ui_standard_image_widget
from airunner.utils import load_metadata_from_image, prepare_metadata
from airunner.widgets.slider.slider_widget import SliderWidget
from airunner.aihandler.logger import Logger


class StandardImageWidget(StandardBaseWidget):
    logger = Logger(prefix="StandardImageWidget")
    widget_class_ = Ui_standard_image_widget
    _pixmap = None
    _label = None
    _layout = None
    image_path = None
    image_label = None
    image_batch = None
    meta_data = None
    _image = None

    @property
    def image(self):
        if self._image is None:
            try:
                self.image = self.app.canvas_widget.current_layer.image
            except Exception as e:
                self.logger.error(f"Error while getting image: {e}")
        return self._image
    
    @image.setter
    def image(self, image):
        self._image = image

    @property
    def canvas_widget(self):
        return self.ui.canvas_widget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui.advanced_settings.hide()
        self.load_upscale_options()
        self.set_controlnet_settings_properties()
        self.set_input_image_widget_properties()
    
    def set_controlnet_settings_properties(self):
        self.ui.controlnet_settings.initialize()

    def set_input_image_widget_properties(self):
        self.ui.input_image_widget.initialize()
        self.ui.controlnet_settings.initialize()
    
    def update_image_input_thumbnail(self):
        self.ui.input_image_widget.set_thumbnail()

    def update_controlnet_settings_thumbnail(self):
        self.ui.controlnet_settings.set_thumbnail()
    
    def update_thumbnails(self):
        self.update_image_input_thumbnail()
        self.update_controlnet_settings_thumbnail()
    
    def upscale_number_changed(self, val):
        print("upscale int", val)
    
    def handle_advanced_settings_checkbox(self, val):
        if val:
            self.ui.advanced_settings.show()
        else:
            self.ui.advanced_settings.hide()
    
    def load_upscale_options(self):
        self.ui.upscale_model.blockSignals(True)
        model = self.app.settings["standard_image_settings"]["upscale_model"]
        index = self.ui.upscale_model.findText(model)
        if index == -1:
            index = 0
        self.ui.upscale_model.setCurrentIndex(index)
        self.ui.upscale_model.blockSignals(False)

        self.ui.face_enhance.blockSignals(True)
        self.ui.face_enhance.setChecked(self.app.settings["standard_image_settings"]["face_enhance"])
        self.ui.face_enhance.blockSignals(False)
    
    def upscale_model_changed(self, model):
        settings = self.app.settings
        settings["standard_image_settings"]["upscale_model"] = model
        self.app.settings = settings

    def face_enhance_toggled(self, val):
        settings = self.app.settings
        settings["standard_image_settings"]["face_enhance"] = val
        self.app.settings = settings
    
    def handle_controlnet_changed(self, val):
        settings = self.app.settings
        settings["standard_image_settings"]["controlnet"] = val
        self.app.settings = settings

    def handle_image_data(self, data):
        images = data["images"]
        if len(images) == 1:
            self.load_image_from_path(data["path"])
    
    def load_image_from_path(self, image_path):
        image = Image.open(image_path)
        self.load_image_from_object(image=image, image_path=image_path)
        self.app.ui.image_browser.add_image(image_path)
    
    def load_image_from_object(self, image, image_path=NotImplemented):
        self.set_pixmap(image=image, image_path=image_path)

    def set_pixmap(self, image_path=None, image=None):
        self.image_path = image_path
        self.image = image
        meta_data = image.info
        self.meta_data = meta_data if meta_data is not None else load_metadata_from_image(image)
        return
        #size = self.ui.image_frame.width() - 20

        pixmap = self._pixmap
        if not pixmap:
            pixmap = QPixmap()
            self._pixmap = pixmap

        if image_path:
            pixmap.load(image_path)
        else:
            raw_data = image.tobytes("raw", "RGBA")
            qimage = QImage(
                raw_data, 
                image.size[0], 
                image.size[1], 
                QImage.Format.Format_RGBA8888
            )
            pixmap = QPixmap.fromImage(qimage)
        
        width = pixmap.width()
        height = pixmap.height()
        
        label = self._label
        if not label:
            label = QLabel(self.ui.image_frame)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self._label = label

        pixmap = pixmap.scaled(
            size, 
            size, 
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        label.setPixmap(pixmap)
        label.setFixedWidth(size)
        label.setFixedHeight(size)

        # on label click:
        label.mousePressEvent = self.handle_label_clicked
        label.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = self._layout
        if not layout:
            layout = QVBoxLayout(self.ui.image_frame)
            layout.addWidget(label)        
            self._layout = layout
        
        # get the metadata from this image, load it as a png first
        # then load the metadata from the png
        if image_path:
            image = Image.open(image_path)
            meta_data = image.info

            meta_data["width"] = width
            meta_data["height"] = height

            #self.set_table_data(meta_data)
    
    def handle_label_clicked(self, event):
        # create a popup window and show the full size image in it
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Image preview")
        layout = QVBoxLayout(self.dialog)
        self.dialog.setLayout(layout)

        if self.image_path:
            self.image = Image.open(self.image_path)

        if self.image:
            raw_data = self.image.tobytes("raw", "RGBA")
            qimage = QImage(
                raw_data, 
                self.image.size[0], 
                self.image.size[1], 
                QImage.Format.Format_RGBA8888
            )
            pixmap = QPixmap.fromImage(qimage)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        
        self.dialog.show()
    
    def similar_image_with_prompt(self):
        """
        Using the LLM, generate a description of the image
        """
        self.app.describe_image(image=self.image, callback=self.handle_prompt_generated)
        # prompt = self.app.generator_tab_widget.ui.prompt.toPlainText()
        # negative_prompt = self.app.generator_tab_widget.ui.negative_prompt.toPlainText()
        # self.handle_prompt_generated([prompt], [negative_prompt])
    
    def handle_prompt_generated(self, prompt, negative_prompt):
        meta_data = load_metadata_from_image(self.image)
        meta_data["prompt"] = prompt[0]
        meta_data["negative_prompt"] = negative_prompt[0]
        meta_data = prepare_metadata({ "options": meta_data })
        if self.image_path:
            image = Image.open(self.image_path)
            image.save(self.image_path, pnginfo=meta_data)
        else:
            image = self.app.canvas_widget.current_layer.image
        self.image = image
        self.meta_data = load_metadata_from_image(self.image)
        self.generate_similar_image()

    def similar_image(self):
        self.generate_similar_image()
    
    def generate_similar_image(self, batch_size=1):
        meta_data = self.meta_data or {}
        
        prompt = meta_data.get("prompt", None)
        negative_prompt = meta_data.get("negative_prompt", None)
        prompt = None if prompt == "" else prompt
        negative_prompt = None if negative_prompt == "" else negative_prompt

        if prompt is None:
            #return self.similar_image_with_prompt()
            prompt = ""
        if negative_prompt is None:
            meta_data["negative_prompt"] = "verybadimagenegative_v1.3, EasyNegative"
        
        image_similarity = self.app.settings["standard_image_settings"]["image_similarity"]
        controlnet = self.app.settings["standard_image_settings"]["controlnet"]

        meta_data.pop("seed", None)
        meta_data["action"] = "txt2img"
        meta_data["width"] = self.image.width
        meta_data["height"] = self.image.height
        meta_data["enable_controlnet"] = True
        meta_data["controlnet"] = controlnet.lower()
        meta_data["controlnet_conditioning_scale"] = image_similarity / 100.0
        meta_data["strength"] = 1.1 - (image_similarity / 100.0)
        meta_data["enable_input_image"] = True
        meta_data["use_cropped_image"] = False
        meta_data["batch_size"] = batch_size

        self.app.generator_tab_widget.call_generate(
            image=self.image,
            override_data=meta_data
        )
    
    def handle_similar_slider_change(self, value):
        self.similarity = value

    def similar_batch(self):
        self.generate_similar_image(batch_size=4)

    def upscale_2x_clicked(self):
        meta_data = self.meta_data or {}
        
        prompt = meta_data.get("prompt", None)
        negative_prompt = meta_data.get("negative_prompt", None)
        prompt = None if prompt == "" else prompt
        negative_prompt = None if negative_prompt == "" else negative_prompt

        if prompt is None:
            prompt = ""
        if negative_prompt is None:
            meta_data["negative_prompt"] = "verybadimagenegative_v1.3, EasyNegative"
        
        meta_data.pop("seed", None)
        meta_data["model_data_path"] = self.app.settings["standard_image_settings"]["upscale_model"]
        meta_data["face_enhance"] = self.app.settings["standard_image_settings"]['face_enhance']
        meta_data["denoise_strength"] = 0.5
        meta_data["action"] = "upscale"
        meta_data["width"] = self.ui.canvas_widget.current_layer.image.width
        meta_data["height"] = self.ui.canvas_widget.current_layer.image.height
        meta_data["enable_input_image"] = True
        meta_data["use_cropped_image"] = False

        self.app.generator_tab_widget.call_generate(
            image=self.ui.canvas_widget.current_layer.image,
            override_data=meta_data
        )
    
    def initialize(self):
        # find all SliderWidget widgets in the template and call initialize
        for widget in self.findChildren(SliderWidget):
            try:
                current_value = getattr(
                    self.generator_settings,
                    widget.property("settings_property").split(".")[1]
                )
            except Exception as e:
                current_value = None
            if current_value is not None:
                widget.setProperty("current_value", current_value)
            widget.initialize()
        self.initialized = True