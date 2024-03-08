# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/brush/templates/brush_widget.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_brush_widget(object):
    def setupUi(self, brush_widget):
        brush_widget.setObjectName("brush_widget")
        brush_widget.resize(400, 364)
        self.gridLayout = QtWidgets.QGridLayout(brush_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.brush_size_slider = SliderWidget(parent=brush_widget)
        self.brush_size_slider.setProperty("slider_minimum", 1)
        self.brush_size_slider.setProperty("slider_maximum", 100)
        self.brush_size_slider.setProperty("spinbox_minimum", 1)
        self.brush_size_slider.setProperty("spinbox_maximum", 100)
        self.brush_size_slider.setProperty("slider_tick_interval", 1)
        self.brush_size_slider.setProperty("slider_single_step", 1)
        self.brush_size_slider.setProperty("slider_page_step", 10)
        self.brush_size_slider.setProperty("spinbox_single_step", 1)
        self.brush_size_slider.setProperty("spinbox_page_step", 10)
        self.brush_size_slider.setProperty("slider_callback", "handle_value_change")
        self.brush_size_slider.setProperty("settings_property", "brush_settings.size")
        self.brush_size_slider.setProperty("display_as_float", False)
        self.brush_size_slider.setObjectName("brush_size_slider")
        self.gridLayout.addWidget(self.brush_size_slider, 1, 0, 1, 1)
        self.strength_slider = SliderWidget(parent=brush_widget)
        self.strength_slider.setProperty("slider_minimum", 1)
        self.strength_slider.setProperty("slider_maximum", 100)
        self.strength_slider.setProperty("spinbox_minimum", 1)
        self.strength_slider.setProperty("spinbox_maximum", 100.0)
        self.strength_slider.setProperty("slider_tick_interval", 1)
        self.strength_slider.setProperty("slider_single_step", 1)
        self.strength_slider.setProperty("slider_page_step", 10)
        self.strength_slider.setProperty("spinbox_single_step", 0.1)
        self.strength_slider.setProperty("spinbox_page_step", 0.2)
        self.strength_slider.setProperty("slider_callback", "handle_value_change")
        self.strength_slider.setProperty("settings_property", "generator_settings.strength")
        self.strength_slider.setProperty("display_as_float", True)
        self.strength_slider.setObjectName("strength_slider")
        self.gridLayout.addWidget(self.strength_slider, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=brush_widget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setContentsMargins(6, 9, 6, 6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.primary_color_button = QtWidgets.QToolButton(parent=self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.primary_color_button.sizePolicy().hasHeightForWidth())
        self.primary_color_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.primary_color_button.setFont(font)
        self.primary_color_button.setText("")
        self.primary_color_button.setObjectName("primary_color_button")
        self.gridLayout_3.addWidget(self.primary_color_button, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 5, 0, 1, 1)
        self.controlnet_conditioning_scale = SliderWidget(parent=brush_widget)
        self.controlnet_conditioning_scale.setProperty("slider_minimum", 0)
        self.controlnet_conditioning_scale.setProperty("slider_maximum", 100)
        self.controlnet_conditioning_scale.setProperty("spinbox_minimum", 0)
        self.controlnet_conditioning_scale.setProperty("spinbox_maximum", 1.0)
        self.controlnet_conditioning_scale.setProperty("slider_tick_interval", 1)
        self.controlnet_conditioning_scale.setProperty("slider_single_step", 1)
        self.controlnet_conditioning_scale.setProperty("slider_page_step", 2)
        self.controlnet_conditioning_scale.setProperty("spinbox_single_step", 0.1)
        self.controlnet_conditioning_scale.setProperty("spinbox_page_step", 0.2)
        self.controlnet_conditioning_scale.setProperty("slider_callback", "handle_value_change")
        self.controlnet_conditioning_scale.setProperty("settings_property", "generator_settings.controlnet_image_settings.conditioning_scale")
        self.controlnet_conditioning_scale.setProperty("display_as_float", True)
        self.controlnet_conditioning_scale.setObjectName("controlnet_conditioning_scale")
        self.gridLayout.addWidget(self.controlnet_conditioning_scale, 3, 0, 1, 1)
        self.controlnet_guidance_scale = SliderWidget(parent=brush_widget)
        self.controlnet_guidance_scale.setProperty("slider_minimum", 1)
        self.controlnet_guidance_scale.setProperty("slider_maximum", 10000)
        self.controlnet_guidance_scale.setProperty("spinbox_minimum", 1)
        self.controlnet_guidance_scale.setProperty("spinbox_maximum", 100.0)
        self.controlnet_guidance_scale.setProperty("slider_tick_interval", 1)
        self.controlnet_guidance_scale.setProperty("slider_single_step", 1)
        self.controlnet_guidance_scale.setProperty("slider_page_step", 10)
        self.controlnet_guidance_scale.setProperty("spinbox_single_step", 0.1)
        self.controlnet_guidance_scale.setProperty("spinbox_page_step", 0.2)
        self.controlnet_guidance_scale.setProperty("slider_callback", "handle_value_change")
        self.controlnet_guidance_scale.setProperty("settings_property", "generator_settings.controlnet_image_settings.guidance_scale")
        self.controlnet_guidance_scale.setProperty("display_as_float", True)
        self.controlnet_guidance_scale.setObjectName("controlnet_guidance_scale")
        self.gridLayout.addWidget(self.controlnet_guidance_scale, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.controlnet = QtWidgets.QComboBox(parent=brush_widget)
        self.controlnet.setObjectName("controlnet")
        self.gridLayout.addWidget(self.controlnet, 0, 0, 1, 1)

        self.retranslateUi(brush_widget)
        self.primary_color_button.clicked.connect(brush_widget.color_button_clicked) # type: ignore
        self.controlnet.currentTextChanged['QString'].connect(brush_widget.controlnet_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(brush_widget)

    def retranslateUi(self, brush_widget):
        _translate = QtCore.QCoreApplication.translate
        brush_widget.setWindowTitle(_translate("brush_widget", "Form"))
        self.brush_size_slider.setProperty("label_text", _translate("brush_widget", "Brush Size"))
        self.strength_slider.setProperty("label_text", _translate("brush_widget", "Strength"))
        self.groupBox_4.setTitle(_translate("brush_widget", "Brush color"))
        self.controlnet_conditioning_scale.setProperty("label_text", _translate("brush_widget", "Controlnet Conditioning Scale"))
        self.controlnet_guidance_scale.setProperty("label_text", _translate("brush_widget", "Controlnet Guidance Scale"))
from airunner.widgets.slider.slider_widget import SliderWidget
