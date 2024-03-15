# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'memory_preferences.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from airunner.widgets.slider.slider_widget import SliderWidget

class Ui_memory_preferences(object):
    def setupUi(self, memory_preferences):
        if not memory_preferences.objectName():
            memory_preferences.setObjectName(u"memory_preferences")
        memory_preferences.resize(603, 903)
        self.gridLayout = QGridLayout(memory_preferences)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.optimize_memory_button = QPushButton(memory_preferences)
        self.optimize_memory_button.setObjectName(u"optimize_memory_button")

        self.verticalLayout_3.addWidget(self.optimize_memory_button)

        self.line_7 = QFrame(memory_preferences)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_7)

        self.use_accelerated_transformers = QCheckBox(memory_preferences)
        self.use_accelerated_transformers.setObjectName(u"use_accelerated_transformers")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.use_accelerated_transformers.setFont(font)

        self.verticalLayout_3.addWidget(self.use_accelerated_transformers)

        self.label_8 = QLabel(memory_preferences)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(False)
        self.label_8.setFont(font1)
        self.label_8.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_9 = QLabel(memory_preferences)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_9.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_9)

        self.line_8 = QFrame(memory_preferences)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_8)

        self.use_attention_slicing = QCheckBox(memory_preferences)
        self.use_attention_slicing.setObjectName(u"use_attention_slicing")
        self.use_attention_slicing.setFont(font)

        self.verticalLayout_3.addWidget(self.use_attention_slicing)

        self.label_4 = QLabel(memory_preferences)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.line_4 = QFrame(memory_preferences)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.use_lastchannels = QCheckBox(memory_preferences)
        self.use_lastchannels.setObjectName(u"use_lastchannels")
        self.use_lastchannels.setFont(font)

        self.verticalLayout_3.addWidget(self.use_lastchannels)

        self.label_3 = QLabel(memory_preferences)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.line = QFrame(memory_preferences)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.use_enable_sequential_cpu_offload = QCheckBox(memory_preferences)
        self.use_enable_sequential_cpu_offload.setObjectName(u"use_enable_sequential_cpu_offload")
        self.use_enable_sequential_cpu_offload.setFont(font)

        self.verticalLayout_3.addWidget(self.use_enable_sequential_cpu_offload)

        self.label = QLabel(memory_preferences)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label)

        self.line_2 = QFrame(memory_preferences)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.enable_model_cpu_offload = QCheckBox(memory_preferences)
        self.enable_model_cpu_offload.setObjectName(u"enable_model_cpu_offload")
        self.enable_model_cpu_offload.setFont(font)

        self.verticalLayout_3.addWidget(self.enable_model_cpu_offload)

        self.label_2 = QLabel(memory_preferences)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.line_3 = QFrame(memory_preferences)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.use_tf32 = QCheckBox(memory_preferences)
        self.use_tf32.setObjectName(u"use_tf32")
        self.use_tf32.setFont(font)

        self.verticalLayout_3.addWidget(self.use_tf32)

        self.label_5 = QLabel(memory_preferences)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_5)

        self.line_5 = QFrame(memory_preferences)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.use_enable_vae_slicing = QCheckBox(memory_preferences)
        self.use_enable_vae_slicing.setObjectName(u"use_enable_vae_slicing")
        self.use_enable_vae_slicing.setFont(font)

        self.verticalLayout_3.addWidget(self.use_enable_vae_slicing)

        self.label_6 = QLabel(memory_preferences)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_6)

        self.line_6 = QFrame(memory_preferences)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.use_tiled_vae = QCheckBox(memory_preferences)
        self.use_tiled_vae.setObjectName(u"use_tiled_vae")
        self.use_tiled_vae.setFont(font)

        self.verticalLayout_3.addWidget(self.use_tiled_vae)

        self.label_7 = QLabel(memory_preferences)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_7)

        self.line_9 = QFrame(memory_preferences)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_9)

        self.use_tome = QGroupBox(memory_preferences)
        self.use_tome.setObjectName(u"use_tome")
        self.use_tome.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.use_tome)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.use_tome)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.tome_sd_ratio = SliderWidget(self.use_tome)
        self.tome_sd_ratio.setObjectName(u"tome_sd_ratio")
        self.tome_sd_ratio.setMinimumSize(QSize(0, 20))
        self.tome_sd_ratio.setProperty("slider_callback", u"tome_sd_ratio_value_change")
        self.tome_sd_ratio.setProperty("current_value", 1000)
        self.tome_sd_ratio.setProperty("slider_maximum", 1000)
        self.tome_sd_ratio.setProperty("spinbox_maximum", 1.000000000000000)
        self.tome_sd_ratio.setProperty("display_as_float", True)
        self.tome_sd_ratio.setProperty("spinbox_single_step", 0.010000000000000)
        self.tome_sd_ratio.setProperty("spinbox_page_step", 0.100000000000000)
        self.tome_sd_ratio.setProperty("spinbox_minimum", 0.000000000000000)
        self.tome_sd_ratio.setProperty("slider_minimum", 0)

        self.gridLayout_2.addWidget(self.tome_sd_ratio, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.use_tome)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(memory_preferences)
        self.use_enable_vae_slicing.toggled.connect(memory_preferences.action_toggled_vae_slicing)
        self.use_tiled_vae.toggled.connect(memory_preferences.action_toggled_tile_vae)
        self.use_tf32.toggled.connect(memory_preferences.action_toggled_tf32)
        self.use_enable_sequential_cpu_offload.toggled.connect(memory_preferences.action_toggled_sequential_cpu_offload)
        self.use_accelerated_transformers.toggled.connect(memory_preferences.action_toggled_accelerated_transformers)
        self.optimize_memory_button.clicked.connect(memory_preferences.action_button_clicked_optimize_memory_settings)
        self.use_lastchannels.toggled.connect(memory_preferences.action_toggled_last_memory)
        self.use_attention_slicing.toggled.connect(memory_preferences.action_toggled_attention_slicing)
        self.enable_model_cpu_offload.toggled.connect(memory_preferences.action_toggled_model_cpu_offload)

        QMetaObject.connectSlotsByName(memory_preferences)
    # setupUi

    def retranslateUi(self, memory_preferences):
        memory_preferences.setWindowTitle(QCoreApplication.translate("memory_preferences", u"Form", None))
        self.optimize_memory_button.setText(QCoreApplication.translate("memory_preferences", u"Optimize Memory Settings", None))
#if QT_CONFIG(tooltip)
        self.use_accelerated_transformers.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">Optimized and memory-efficient attention implementation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_accelerated_transformers.setText(QCoreApplication.translate("memory_preferences", u"Accelerated Transformers", None))
        self.label_8.setText(QCoreApplication.translate("memory_preferences", u"Faster inference, lower VRAM usage", None))
        self.label_9.setText(QCoreApplication.translate("memory_preferences", u"Keep this checked to take advantage of torch 2.0", None))
#if QT_CONFIG(tooltip)
        self.use_attention_slicing.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">Perform computation in steps instead of all at once.</span></p><p><span style=\" font-weight:400;\">About 10% slower inference times.</span></p><p><span style=\" font-weight:400;\">Uses as little as 3.2 GB of VRAM.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_attention_slicing.setText(QCoreApplication.translate("memory_preferences", u"Attention Slicing", None))
        self.label_4.setText(QCoreApplication.translate("memory_preferences", u"Less VRAM usage, slight inference impact", None))
#if QT_CONFIG(tooltip)
        self.use_lastchannels.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">Alternative way of ordering NCHW tensors in memory preserving dimensions ordering. Channels last tensors ordered in such a way that channels become the densest dimension (aka storing images pixel-per-pixel). </span></p><p><span style=\" font-weight:400;\">Since not all operators currently support channels last format it may result in a worst performance, so it\u2019s better to try it and see if it works for your model.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_lastchannels.setText(QCoreApplication.translate("memory_preferences", u"Channels last memory", None))
        self.label_3.setText(QCoreApplication.translate("memory_preferences", u"May slow inference on some models, speed up on others", None))
#if QT_CONFIG(tooltip)
        self.use_enable_sequential_cpu_offload.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">Use with </span>attention slicing<span style=\" font-weight:400;\"> for lower memory consumption.</span></p><p><span style=\" font-weight:400;\">Offloads the weights to CPU and only load them to GPU when performing the forward pass for memory savings.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_enable_sequential_cpu_offload.setText(QCoreApplication.translate("memory_preferences", u"Sequential CPU offload", None))
        self.label.setText(QCoreApplication.translate("memory_preferences", u"Less VRAM usage, slower inference", None))
#if QT_CONFIG(tooltip)
        self.enable_model_cpu_offload.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">Use with attention slicing for lower memory consumption.</span></p><p><span style=\" font-weight:400;\">Moves whole models to the GPU, instead of handling each model\u2019s constituent </span><span style=\" font-weight:400; font-style:italic;\">modules</span><span style=\" font-weight:400;\">. This results in a negligible impact on inference time (compared with moving the pipeline to </span><span style=\" font-family:'monospace'; font-weight:400;\">cuda</span><span style=\" font-weight:400;\">), while still providing some memory savings.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.enable_model_cpu_offload.setText(QCoreApplication.translate("memory_preferences", u"Model CPU offload", None))
        self.label_2.setText(QCoreApplication.translate("memory_preferences", u"Less VRAM usage, slight inference impact", None))
#if QT_CONFIG(tooltip)
        self.use_tf32.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">On Ampere and later CUDA devices matrix multiplications and convolutions can use the TensorFloat32 (TF32) mode for faster but slightly less accurate computations.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_tf32.setText(QCoreApplication.translate("memory_preferences", u"TF32", None))
        self.label_5.setText(QCoreApplication.translate("memory_preferences", u"faster matrix multiplications on ampere achitecture", None))
#if QT_CONFIG(tooltip)
        self.use_enable_vae_slicing.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">Use with Attention Slicing or Xformers</span></p><p><span style=\" font-weight:400;\">Decode large batches of images with limited VRAM, or to enable batches with 32 images or more.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_enable_vae_slicing.setText(QCoreApplication.translate("memory_preferences", u"Vae Slicing", None))
        self.label_6.setText(QCoreApplication.translate("memory_preferences", u"Work with large batches", None))
#if QT_CONFIG(tooltip)
        self.use_tiled_vae.setToolTip(QCoreApplication.translate("memory_preferences", u"<html><head/><body><p><span style=\" font-weight:400;\">Use with Attention Slicing or Xformers</span></p><p><span style=\" font-weight:400;\">Makes it possible to work with large images on limited VRAM. Splits image into overlapping tiles, decodes tiles, blends outputs to make final image.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.use_tiled_vae.setText(QCoreApplication.translate("memory_preferences", u"Tile vae", None))
        self.label_7.setText(QCoreApplication.translate("memory_preferences", u"Work with large images", None))
#if QT_CONFIG(tooltip)
        self.use_tome.setToolTip(QCoreApplication.translate("memory_preferences", u"Merge redundant tokens for faster inference. May result in slight reduction in image quality.", None))
#endif // QT_CONFIG(tooltip)
        self.use_tome.setTitle(QCoreApplication.translate("memory_preferences", u"ToMe Token Merging", None))
        self.label_10.setText(QCoreApplication.translate("memory_preferences", u"Faster inference, slight image impact", None))
        self.tome_sd_ratio.setProperty("label_text", QCoreApplication.translate("memory_preferences", u"Ratio", None))
        self.tome_sd_ratio.setProperty("settings_property", QCoreApplication.translate("memory_preferences", u"memory_settings.tome_sd_ratio", None))
    # retranslateUi

