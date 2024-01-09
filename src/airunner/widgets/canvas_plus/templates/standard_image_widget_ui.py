# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/canvas_plus/templates/standard_image_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_standard_image_widget(object):
    def setupUi(self, standard_image_widget):
        standard_image_widget.setObjectName("standard_image_widget")
        standard_image_widget.resize(690, 969)
        standard_image_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_2 = QtWidgets.QGridLayout(standard_image_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(parent=standard_image_widget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.sidebar = QtWidgets.QWidget(parent=self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QtCore.QSize(0, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(450, 16777215))
        self.sidebar.setObjectName("sidebar")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.sidebar)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.brushes_container = BrushesContainer(parent=self.tab_5)
        self.brushes_container.setAcceptDrops(True)
        self.brushes_container.setObjectName("brushes_container")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.brushes_container)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_3.addWidget(self.brushes_container, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lora_container_widget = LoraContainerWidget(parent=self.tab_4)
        self.lora_container_widget.setObjectName("lora_container_widget")
        self.gridLayout_8.addWidget(self.lora_container_widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.embeddings_container_widget = EmbeddingsContainerWidget(parent=self.tab_3)
        self.embeddings_container_widget.setObjectName("embeddings_container_widget")
        self.gridLayout_9.addWidget(self.embeddings_container_widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.samples_widget = SliderWidget(parent=self.tab)
        self.samples_widget.setMinimumSize(QtCore.QSize(0, 20))
        self.samples_widget.setProperty("slider_callback", "handle_value_change")
        self.samples_widget.setProperty("current_value", 100)
        self.samples_widget.setProperty("slider_maximum", 100)
        self.samples_widget.setProperty("spinbox_maximum", 1.0)
        self.samples_widget.setProperty("display_as_float", True)
        self.samples_widget.setProperty("spinbox_single_step", 0.01)
        self.samples_widget.setProperty("spinbox_page_step", 0.01)
        self.samples_widget.setProperty("spinbox_minimum", 0.0)
        self.samples_widget.setProperty("slider_minimum", 0)
        self.samples_widget.setObjectName("samples_widget")
        self.horizontalLayout_4.addWidget(self.samples_widget)
        self.generate_single_simillar_button = QtWidgets.QPushButton(parent=self.tab)
        self.generate_single_simillar_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_single_simillar_button.setObjectName("generate_single_simillar_button")
        self.horizontalLayout_4.addWidget(self.generate_single_simillar_button)
        self.generate_batch_similar_button = QtWidgets.QPushButton(parent=self.tab)
        self.generate_batch_similar_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate_batch_similar_button.setObjectName("generate_batch_similar_button")
        self.horizontalLayout_4.addWidget(self.generate_batch_similar_button)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.advanced_settings = QtWidgets.QWidget(parent=self.tab)
        self.advanced_settings.setObjectName("advanced_settings")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.advanced_settings)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.input_image_widget = InputImageSettingsWidget(parent=self.advanced_settings)
        self.input_image_widget.setObjectName("input_image_widget")
        self.gridLayout_4.addWidget(self.input_image_widget, 0, 0, 1, 1)
        self.controlnet_settings = ControlNetSettingsWidget(parent=self.advanced_settings)
        self.controlnet_settings.setObjectName("controlnet_settings")
        self.gridLayout_4.addWidget(self.controlnet_settings, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.advanced_settings, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 3, 0, 1, 1)
        self.advanced_settings_checkbox = QtWidgets.QCheckBox(parent=self.tab)
        self.advanced_settings_checkbox.setObjectName("advanced_settings_checkbox")
        self.gridLayout_5.addWidget(self.advanced_settings_checkbox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upscale_model = QtWidgets.QComboBox(parent=self.tab_2)
        self.upscale_model.setObjectName("upscale_model")
        self.upscale_model.addItem("")
        self.upscale_model.addItem("")
        self.upscale_model.addItem("")
        self.upscale_model.addItem("")
        self.upscale_model.addItem("")
        self.upscale_model.addItem("")
        self.horizontalLayout.addWidget(self.upscale_model)
        self.face_enhance = QtWidgets.QCheckBox(parent=self.tab_2)
        self.face_enhance.setObjectName("face_enhance")
        self.horizontalLayout.addWidget(self.face_enhance)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.tab_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.upscale_2x = QtWidgets.QPushButton(parent=self.tab_2)
        self.upscale_2x.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.upscale_2x.setObjectName("upscale_2x")
        self.horizontalLayout_2.addWidget(self.upscale_2x)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setStyleSheet("")
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.tab_6)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.TabPosition.East)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.tab_7)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 414, 933))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.samples_widget_2 = SliderWidget(parent=self.scrollAreaWidgetContents_2)
        self.samples_widget_2.setProperty("slider_callback", "handle_value_change")
        self.samples_widget_2.setProperty("current_value", 0)
        self.samples_widget_2.setProperty("slider_maximum", 500)
        self.samples_widget_2.setProperty("spinbox_maximum", 500.0)
        self.samples_widget_2.setProperty("display_as_float", False)
        self.samples_widget_2.setProperty("spinbox_single_step", 1)
        self.samples_widget_2.setProperty("spinbox_page_step", 1)
        self.samples_widget_2.setProperty("spinbox_minimum", 1)
        self.samples_widget_2.setProperty("slider_minimum", 1)
        self.samples_widget_2.setObjectName("samples_widget_2")
        self.horizontalLayout_6.addWidget(self.samples_widget_2)
        self.clip_skip_slider_widget = SliderWidget(parent=self.scrollAreaWidgetContents_2)
        self.clip_skip_slider_widget.setProperty("current_value", 0)
        self.clip_skip_slider_widget.setProperty("slider_maximum", 11)
        self.clip_skip_slider_widget.setProperty("spinbox_maximum", 12.0)
        self.clip_skip_slider_widget.setProperty("display_as_float", False)
        self.clip_skip_slider_widget.setProperty("spinbox_single_step", 1)
        self.clip_skip_slider_widget.setProperty("spinbox_page_step", 1)
        self.clip_skip_slider_widget.setProperty("spinbox_minimum", 0)
        self.clip_skip_slider_widget.setProperty("slider_minimum", 0)
        self.clip_skip_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.clip_skip_slider_widget.setProperty("settings_property", "generator.clip_skip")
        self.clip_skip_slider_widget.setObjectName("clip_skip_slider_widget")
        self.horizontalLayout_6.addWidget(self.clip_skip_slider_widget)
        self.gridLayout_10.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.seed_widget = SeedWidget(parent=self.scrollAreaWidgetContents_2)
        self.seed_widget.setProperty("generator_section", "")
        self.seed_widget.setProperty("generator_name", "")
        self.seed_widget.setObjectName("seed_widget")
        self.horizontalLayout_3.addWidget(self.seed_widget)
        self.seed_widget_latents = SeedWidget(parent=self.scrollAreaWidgetContents_2)
        self.seed_widget_latents.setProperty("generator_section", "")
        self.seed_widget_latents.setProperty("generator_name", "")
        self.seed_widget_latents.setObjectName("seed_widget_latents")
        self.horizontalLayout_3.addWidget(self.seed_widget_latents)
        self.gridLayout_10.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.steps_widget = SliderWidget(parent=self.scrollAreaWidgetContents_2)
        self.steps_widget.setProperty("slider_callback", "handle_value_change")
        self.steps_widget.setProperty("current_value", 0)
        self.steps_widget.setProperty("slider_maximum", 200)
        self.steps_widget.setProperty("spinbox_maximum", 200.0)
        self.steps_widget.setProperty("display_as_float", False)
        self.steps_widget.setProperty("spinbox_single_step", 1)
        self.steps_widget.setProperty("spinbox_page_step", 1)
        self.steps_widget.setProperty("spinbox_minimum", 1)
        self.steps_widget.setProperty("slider_minimum", 1)
        self.steps_widget.setProperty("settings_property", "generator.steps")
        self.steps_widget.setObjectName("steps_widget")
        self.horizontalLayout_5.addWidget(self.steps_widget)
        self.scale_widget = SliderWidget(parent=self.scrollAreaWidgetContents_2)
        self.scale_widget.setProperty("current_value", 0)
        self.scale_widget.setProperty("slider_maximum", 10000)
        self.scale_widget.setProperty("spinbox_maximum", 100.0)
        self.scale_widget.setProperty("display_as_float", True)
        self.scale_widget.setProperty("spinbox_single_step", 0.01)
        self.scale_widget.setProperty("spinbox_page_step", 0.01)
        self.scale_widget.setProperty("slider_callback", "handle_value_change")
        self.scale_widget.setProperty("settings_property", "generator.scale")
        self.scale_widget.setObjectName("scale_widget")
        self.horizontalLayout_5.addWidget(self.scale_widget)
        self.gridLayout_10.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.ddim_frames = QtWidgets.QHBoxLayout()
        self.ddim_frames.setObjectName("ddim_frames")
        self.ddim_eta_slider_widget = SliderWidget(parent=self.scrollAreaWidgetContents_2)
        self.ddim_eta_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.ddim_eta_slider_widget.setProperty("current_value", 1)
        self.ddim_eta_slider_widget.setProperty("slider_maximum", 10)
        self.ddim_eta_slider_widget.setProperty("spinbox_maximum", 10)
        self.ddim_eta_slider_widget.setProperty("display_as_float", False)
        self.ddim_eta_slider_widget.setProperty("spinbox_single_step", 1)
        self.ddim_eta_slider_widget.setProperty("spinbox_page_step", 1)
        self.ddim_eta_slider_widget.setProperty("spinbox_minimum", 1)
        self.ddim_eta_slider_widget.setProperty("slider_minimum", 1)
        self.ddim_eta_slider_widget.setProperty("settings_property", "generator.ddim_eta")
        self.ddim_eta_slider_widget.setObjectName("ddim_eta_slider_widget")
        self.ddim_frames.addWidget(self.ddim_eta_slider_widget)
        self.frames_slider_widget = SliderWidget(parent=self.scrollAreaWidgetContents_2)
        self.frames_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.frames_slider_widget.setProperty("current_value", 0)
        self.frames_slider_widget.setProperty("slider_maximum", 200)
        self.frames_slider_widget.setProperty("spinbox_maximum", 200.0)
        self.frames_slider_widget.setProperty("display_as_float", False)
        self.frames_slider_widget.setProperty("spinbox_single_step", 1)
        self.frames_slider_widget.setProperty("spinbox_page_step", 1)
        self.frames_slider_widget.setProperty("spinbox_minimum", 1)
        self.frames_slider_widget.setProperty("slider_minimum", 1)
        self.frames_slider_widget.setProperty("settings_property", "generator.n_samples")
        self.frames_slider_widget.setObjectName("frames_slider_widget")
        self.ddim_frames.addWidget(self.frames_slider_widget)
        self.gridLayout_10.addLayout(self.ddim_frames, 4, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.pipeline = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents_2)
        self.pipeline.setObjectName("pipeline")
        self.verticalLayout_4.addWidget(self.pipeline)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.version = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents_2)
        self.version.setObjectName("version")
        self.verticalLayout_7.addWidget(self.version)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.model = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents_2)
        self.model.setObjectName("model")
        self.verticalLayout.addWidget(self.model)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.scheduler = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents_2)
        self.scheduler.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.scheduler.setObjectName("scheduler")
        self.verticalLayout_2.addWidget(self.scheduler)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_10.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_10.addItem(spacerItem2, 5, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_13.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("applications-graphics")
        self.tabWidget_2.addTab(self.tab_7, icon, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.llm_settings_widget = LLMSettingsWidget(parent=self.tab_8)
        self.llm_settings_widget.setObjectName("llm_settings_widget")
        self.gridLayout_12.addWidget(self.llm_settings_widget, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("emblem-documents")
        self.tabWidget_2.addTab(self.tab_8, icon, "")
        self.gridLayout_11.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("document-properties")
        self.tabWidget.addTab(self.tab_6, icon, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 9, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.canvas_widget = CanvasPlusWidget(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_widget.sizePolicy().hasHeightForWidth())
        self.canvas_widget.setSizePolicy(sizePolicy)
        self.canvas_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.canvas_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.canvas_widget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.canvas_widget.setAcceptDrops(True)
        self.canvas_widget.setObjectName("canvas_widget")
        self.gridLayout.addWidget(self.canvas_widget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(standard_image_widget)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.upscale_model.currentTextChanged['QString'].connect(standard_image_widget.upscale_model_changed) # type: ignore
        self.face_enhance.clicked['bool'].connect(standard_image_widget.face_enhance_toggled) # type: ignore
        self.comboBox.currentIndexChanged['int'].connect(standard_image_widget.upscale_number_changed) # type: ignore
        self.upscale_2x.clicked.connect(standard_image_widget.upscale_2x_clicked) # type: ignore
        self.advanced_settings_checkbox.clicked['bool'].connect(standard_image_widget.handle_advanced_settings_checkbox) # type: ignore
        self.generate_single_simillar_button.clicked.connect(standard_image_widget.similar_image) # type: ignore
        self.generate_batch_similar_button.clicked.connect(standard_image_widget.similar_batch) # type: ignore
        self.pipeline.currentTextChanged['QString'].connect(standard_image_widget.handle_pipeline_changed) # type: ignore
        self.version.currentTextChanged['QString'].connect(standard_image_widget.handle_version_changed) # type: ignore
        self.model.currentTextChanged['QString'].connect(standard_image_widget.handle_model_changed) # type: ignore
        self.scheduler.currentTextChanged['QString'].connect(standard_image_widget.handle_scheduler_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(standard_image_widget)

    def retranslateUi(self, standard_image_widget):
        _translate = QtCore.QCoreApplication.translate
        standard_image_widget.setWindowTitle(_translate("standard_image_widget", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("standard_image_widget", "Presets"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_5), _translate("standard_image_widget", "Stable Diffusion setting presets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("standard_image_widget", "LoRA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("standard_image_widget", "Embeddings"))
        self.samples_widget.setProperty("label_text", _translate("standard_image_widget", "Similarity"))
        self.samples_widget.setProperty("settings_property", _translate("standard_image_widget", "standard_image_widget_settings.image_similarity"))
        self.generate_single_simillar_button.setToolTip(_translate("standard_image_widget", "Generate one variation"))
        self.generate_single_simillar_button.setText(_translate("standard_image_widget", "Single"))
        self.generate_batch_similar_button.setToolTip(_translate("standard_image_widget", "Generate a batch of four variations"))
        self.generate_batch_similar_button.setText(_translate("standard_image_widget", "Batch"))
        self.advanced_settings_checkbox.setText(_translate("standard_image_widget", "Advanced settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("standard_image_widget", "Similar"))
        self.upscale_model.setItemText(0, _translate("standard_image_widget", "RealESRGAN_x4plus"))
        self.upscale_model.setItemText(1, _translate("standard_image_widget", "RealESRNet_x4plus"))
        self.upscale_model.setItemText(2, _translate("standard_image_widget", "RealESRGAN_x4plus_anime_6B"))
        self.upscale_model.setItemText(3, _translate("standard_image_widget", "RealESRGAN_x2plus"))
        self.upscale_model.setItemText(4, _translate("standard_image_widget", "realesr-animevideov3"))
        self.upscale_model.setItemText(5, _translate("standard_image_widget", "realesr-general-x4v3"))
        self.face_enhance.setText(_translate("standard_image_widget", "Face enhance"))
        self.comboBox.setItemText(0, _translate("standard_image_widget", "2x"))
        self.comboBox.setItemText(1, _translate("standard_image_widget", "4x"))
        self.upscale_2x.setText(_translate("standard_image_widget", "Upscale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("standard_image_widget", "Upscale"))
        self.samples_widget_2.setProperty("label_text", _translate("standard_image_widget", "Samples"))
        self.samples_widget_2.setProperty("settings_property", _translate("standard_image_widget", "generator.n_samples"))
        self.clip_skip_slider_widget.setProperty("label_text", _translate("standard_image_widget", "Clip Skip"))
        self.seed_widget.setProperty("property_name", _translate("standard_image_widget", "generator.random_seed"))
        self.seed_widget_latents.setProperty("property_name", _translate("standard_image_widget", "generator.random_latents_seed"))
        self.steps_widget.setProperty("label_text", _translate("standard_image_widget", "Steps"))
        self.scale_widget.setProperty("label_text", _translate("standard_image_widget", "Scale"))
        self.ddim_eta_slider_widget.setProperty("label_text", _translate("standard_image_widget", "DDIM ETA"))
        self.frames_slider_widget.setProperty("label_text", _translate("standard_image_widget", "Frames"))
        self.label_5.setText(_translate("standard_image_widget", "Pipeline"))
        self.label_6.setText(_translate("standard_image_widget", "Version"))
        self.label_3.setText(_translate("standard_image_widget", "Model"))
        self.label_4.setText(_translate("standard_image_widget", "Scheduler"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("standard_image_widget", "Image"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("standard_image_widget", "Text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("standard_image_widget", "Settings"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_6), _translate("standard_image_widget", "Stable Diffusion settings"))
from airunner.widgets.brushes.brushes_container import BrushesContainer
from airunner.widgets.canvas_plus.canvas_plus_widget import CanvasPlusWidget
from airunner.widgets.controlnet_settings.controlnet_settings_widget import ControlNetSettingsWidget
from airunner.widgets.embeddings.embeddings_container_widget import EmbeddingsContainerWidget
from airunner.widgets.input_image.input_image_settings_widget import InputImageSettingsWidget
from airunner.widgets.llm.llm_settings_widget import LLMSettingsWidget
from airunner.widgets.lora.lora_container_widget import LoraContainerWidget
from airunner.widgets.seed.seed_widget import SeedWidget
from airunner.widgets.slider.slider_widget import SliderWidget
