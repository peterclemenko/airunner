# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/memory_preferences/templates/memory_preferences.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_memory_preferences(object):
    def setupUi(self, memory_preferences):
        memory_preferences.setObjectName("memory_preferences")
        memory_preferences.resize(603, 903)
        self.gridLayout = QtWidgets.QGridLayout(memory_preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.optimize_memory_button = QtWidgets.QPushButton(parent=memory_preferences)
        self.optimize_memory_button.setObjectName("optimize_memory_button")
        self.verticalLayout_3.addWidget(self.optimize_memory_button)
        self.line_7 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.use_accelerated_transformers = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_accelerated_transformers.setFont(font)
        self.use_accelerated_transformers.setObjectName("use_accelerated_transformers")
        self.verticalLayout_3.addWidget(self.use_accelerated_transformers)
        self.label_8 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setIndent(-1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.line_8 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_3.addWidget(self.line_8)
        self.use_attention_slicing = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_attention_slicing.setFont(font)
        self.use_attention_slicing.setObjectName("use_attention_slicing")
        self.verticalLayout_3.addWidget(self.use_attention_slicing)
        self.label_4 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.line_4 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.use_lastchannels = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_lastchannels.setFont(font)
        self.use_lastchannels.setObjectName("use_lastchannels")
        self.verticalLayout_3.addWidget(self.use_lastchannels)
        self.label_3 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line = QtWidgets.QFrame(parent=memory_preferences)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.use_enable_sequential_cpu_offload = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_enable_sequential_cpu_offload.setFont(font)
        self.use_enable_sequential_cpu_offload.setObjectName("use_enable_sequential_cpu_offload")
        self.verticalLayout_3.addWidget(self.use_enable_sequential_cpu_offload)
        self.label = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.enable_model_cpu_offload = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.enable_model_cpu_offload.setFont(font)
        self.enable_model_cpu_offload.setObjectName("enable_model_cpu_offload")
        self.verticalLayout_3.addWidget(self.enable_model_cpu_offload)
        self.label_2 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.use_tf32 = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_tf32.setFont(font)
        self.use_tf32.setObjectName("use_tf32")
        self.verticalLayout_3.addWidget(self.use_tf32)
        self.label_5 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setIndent(-1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.line_5 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.use_enable_vae_slicing = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_enable_vae_slicing.setFont(font)
        self.use_enable_vae_slicing.setObjectName("use_enable_vae_slicing")
        self.verticalLayout_3.addWidget(self.use_enable_vae_slicing)
        self.label_6 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.line_6 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.use_tiled_vae = QtWidgets.QCheckBox(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_tiled_vae.setFont(font)
        self.use_tiled_vae.setObjectName("use_tiled_vae")
        self.verticalLayout_3.addWidget(self.use_tiled_vae)
        self.label_7 = QtWidgets.QLabel(parent=memory_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setIndent(-1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.line_9 = QtWidgets.QFrame(parent=memory_preferences)
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.use_tome = QtWidgets.QGroupBox(parent=memory_preferences)
        self.use_tome.setCheckable(True)
        self.use_tome.setObjectName("use_tome")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.use_tome)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(parent=self.use_tome)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.tome_sd_ratio = SliderWidget(parent=self.use_tome)
        self.tome_sd_ratio.setMinimumSize(QtCore.QSize(0, 20))
        self.tome_sd_ratio.setProperty("slider_callback", "handle_value_change")
        self.tome_sd_ratio.setProperty("current_value", 1000)
        self.tome_sd_ratio.setProperty("slider_maximum", 1000)
        self.tome_sd_ratio.setProperty("spinbox_maximum", 1.0)
        self.tome_sd_ratio.setProperty("display_as_float", True)
        self.tome_sd_ratio.setProperty("spinbox_single_step", 0.01)
        self.tome_sd_ratio.setProperty("spinbox_page_step", 0.1)
        self.tome_sd_ratio.setProperty("spinbox_minimum", 0.0)
        self.tome_sd_ratio.setProperty("slider_minimum", 0)
        self.tome_sd_ratio.setObjectName("tome_sd_ratio")
        self.gridLayout_2.addWidget(self.tome_sd_ratio, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.use_tome)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(memory_preferences)
        self.use_enable_vae_slicing.toggled['bool'].connect(memory_preferences.action_toggled_vae_slicing) # type: ignore
        self.use_tiled_vae.toggled['bool'].connect(memory_preferences.action_toggled_tile_vae) # type: ignore
        self.use_tf32.toggled['bool'].connect(memory_preferences.action_toggled_tf32) # type: ignore
        self.use_enable_sequential_cpu_offload.toggled['bool'].connect(memory_preferences.action_toggled_sequential_cpu_offload) # type: ignore
        self.use_accelerated_transformers.toggled['bool'].connect(memory_preferences.action_toggled_accelerated_transformers) # type: ignore
        self.optimize_memory_button.clicked.connect(memory_preferences.action_button_clicked_optimize_memory_settings) # type: ignore
        self.use_lastchannels.toggled['bool'].connect(memory_preferences.action_toggled_last_memory) # type: ignore
        self.use_attention_slicing.toggled['bool'].connect(memory_preferences.action_toggled_attention_slicing) # type: ignore
        self.enable_model_cpu_offload.toggled['bool'].connect(memory_preferences.action_toggled_model_cpu_offload) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(memory_preferences)

    def retranslateUi(self, memory_preferences):
        _translate = QtCore.QCoreApplication.translate
        memory_preferences.setWindowTitle(_translate("memory_preferences", "Form"))
        self.optimize_memory_button.setText(_translate("memory_preferences", "Optimize Memory Settings"))
        self.use_accelerated_transformers.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">Optimized and memory-efficient attention implementation.</span></p></body></html>"))
        self.use_accelerated_transformers.setText(_translate("memory_preferences", "Accelerated Transformers"))
        self.label_8.setText(_translate("memory_preferences", "Faster inference, lower VRAM usage"))
        self.label_9.setText(_translate("memory_preferences", "Keep this checked to take advantage of torch 2.0"))
        self.use_attention_slicing.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">Perform computation in steps instead of all at once.</span></p><p><span style=\" font-weight:400;\">About 10% slower inference times.</span></p><p><span style=\" font-weight:400;\">Uses as little as 3.2 GB of VRAM.</span></p></body></html>"))
        self.use_attention_slicing.setText(_translate("memory_preferences", "Attention Slicing"))
        self.label_4.setText(_translate("memory_preferences", "Less VRAM usage, slight inference impact"))
        self.use_lastchannels.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">Alternative way of ordering NCHW tensors in memory preserving dimensions ordering. Channels last tensors ordered in such a way that channels become the densest dimension (aka storing images pixel-per-pixel). </span></p><p><span style=\" font-weight:400;\">Since not all operators currently support channels last format it may result in a worst performance, so it’s better to try it and see if it works for your model.</span></p></body></html>"))
        self.use_lastchannels.setText(_translate("memory_preferences", "Channels last memory"))
        self.label_3.setText(_translate("memory_preferences", "May slow inference on some models, speed up on others"))
        self.use_enable_sequential_cpu_offload.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">Use with </span>attention slicing<span style=\" font-weight:400;\"> for lower memory consumption.</span></p><p><span style=\" font-weight:400;\">Offloads the weights to CPU and only load them to GPU when performing the forward pass for memory savings.</span></p></body></html>"))
        self.use_enable_sequential_cpu_offload.setText(_translate("memory_preferences", "Sequential CPU offload"))
        self.label.setText(_translate("memory_preferences", "Less VRAM usage, slower inference"))
        self.enable_model_cpu_offload.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">Use with attention slicing for lower memory consumption.</span></p><p><span style=\" font-weight:400;\">Moves whole models to the GPU, instead of handling each model’s constituent </span><span style=\" font-weight:400; font-style:italic;\">modules</span><span style=\" font-weight:400;\">. This results in a negligible impact on inference time (compared with moving the pipeline to </span><span style=\" font-family:\'monospace\'; font-weight:400;\">cuda</span><span style=\" font-weight:400;\">), while still providing some memory savings.</span></p></body></html>"))
        self.enable_model_cpu_offload.setText(_translate("memory_preferences", "Model CPU offload"))
        self.label_2.setText(_translate("memory_preferences", "Less VRAM usage, slight inference impact"))
        self.use_tf32.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">On Ampere and later CUDA devices matrix multiplications and convolutions can use the TensorFloat32 (TF32) mode for faster but slightly less accurate computations.</span></p></body></html>"))
        self.use_tf32.setText(_translate("memory_preferences", "TF32"))
        self.label_5.setText(_translate("memory_preferences", "faster matrix multiplications on ampere achitecture"))
        self.use_enable_vae_slicing.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">Use with Attention Slicing or Xformers</span></p><p><span style=\" font-weight:400;\">Decode large batches of images with limited VRAM, or to enable batches with 32 images or more.</span></p></body></html>"))
        self.use_enable_vae_slicing.setText(_translate("memory_preferences", "Vae Slicing"))
        self.label_6.setText(_translate("memory_preferences", "Work with large batches"))
        self.use_tiled_vae.setToolTip(_translate("memory_preferences", "<html><head/><body><p><span style=\" font-weight:400;\">Use with Attention Slicing or Xformers</span></p><p><span style=\" font-weight:400;\">Makes it possible to work with large images on limited VRAM. Splits image into overlapping tiles, decodes tiles, blends outputs to make final image.</span></p></body></html>"))
        self.use_tiled_vae.setText(_translate("memory_preferences", "Tile vae"))
        self.label_7.setText(_translate("memory_preferences", "Work with large images"))
        self.use_tome.setToolTip(_translate("memory_preferences", "Merge redundant tokens for faster inference. May result in slight reduction in image quality."))
        self.use_tome.setTitle(_translate("memory_preferences", "ToMe Token Merging"))
        self.label_10.setText(_translate("memory_preferences", "Faster inference, slight image impact"))
        self.tome_sd_ratio.setProperty("label_text", _translate("memory_preferences", "Ratio"))
        self.tome_sd_ratio.setProperty("settings_property", _translate("memory_preferences", "tome_sd_ratio"))
from airunner.widgets.slider.slider_widget import SliderWidget
