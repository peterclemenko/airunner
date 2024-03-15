# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/active_grid_settings/templates/active_grid_settings.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_active_grid_settings_widget(object):
    def setupUi(self, active_grid_settings_widget):
        active_grid_settings_widget.setObjectName("active_grid_settings_widget")
        active_grid_settings_widget.resize(445, 326)
        self.gridLayout_3 = QtWidgets.QGridLayout(active_grid_settings_widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.active_grid_area_groupbox = QtWidgets.QGroupBox(active_grid_settings_widget)
        self.active_grid_area_groupbox.setCheckable(True)
        self.active_grid_area_groupbox.setChecked(False)
        self.active_grid_area_groupbox.setObjectName("active_grid_area_groupbox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.active_grid_area_groupbox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.active_grid_border_groupbox = QtWidgets.QGroupBox(self.active_grid_area_groupbox)
        self.active_grid_border_groupbox.setCheckable(True)
        self.active_grid_border_groupbox.setChecked(False)
        self.active_grid_border_groupbox.setObjectName("active_grid_border_groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.active_grid_border_groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.active_grid_border_groupbox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.border_opacity_slider_widget = SliderWidget(self.active_grid_border_groupbox)
        self.border_opacity_slider_widget.setProperty("spinbox_single_step", 0.01)
        self.border_opacity_slider_widget.setProperty("slider_page_step", 1)
        self.border_opacity_slider_widget.setProperty("spinbox_page_step", 0.1)
        self.border_opacity_slider_widget.setProperty("display_as_float", True)
        self.border_opacity_slider_widget.setProperty("slider_minimum", 0)
        self.border_opacity_slider_widget.setProperty("slider_maximum", 255)
        self.border_opacity_slider_widget.setProperty("spinbox_minimum", 0.0)
        self.border_opacity_slider_widget.setProperty("spinbox_maximum", 1.0)
        self.border_opacity_slider_widget.setProperty("slider_tick_interval", 1.0)
        self.border_opacity_slider_widget.setProperty("slider_singlestep", 1)
        self.border_opacity_slider_widget.setObjectName("border_opacity_slider_widget")
        self.gridLayout.addWidget(self.border_opacity_slider_widget, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.active_grid_border_groupbox, 1, 0, 1, 1)
        self.active_grid_fill_groupbox = QtWidgets.QGroupBox(self.active_grid_area_groupbox)
        self.active_grid_fill_groupbox.setCheckable(True)
        self.active_grid_fill_groupbox.setChecked(False)
        self.active_grid_fill_groupbox.setObjectName("active_grid_fill_groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.active_grid_fill_groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fill_opacity_slider_widget = SliderWidget(self.active_grid_fill_groupbox)
        self.fill_opacity_slider_widget.setProperty("spinbox_single_step", 0.01)
        self.fill_opacity_slider_widget.setProperty("slider_page_step", 1)
        self.fill_opacity_slider_widget.setProperty("spinbox_page_step", 0.1)
        self.fill_opacity_slider_widget.setProperty("display_as_float", True)
        self.fill_opacity_slider_widget.setProperty("slider_minimum", 0)
        self.fill_opacity_slider_widget.setProperty("slider_maximum", 255)
        self.fill_opacity_slider_widget.setProperty("spinbox_minimum", 0.0)
        self.fill_opacity_slider_widget.setProperty("spinbox_maximum", 1.0)
        self.fill_opacity_slider_widget.setProperty("slider_tick_interval", 1.0)
        self.fill_opacity_slider_widget.setProperty("slider_singlestep", 1)
        self.fill_opacity_slider_widget.setObjectName("fill_opacity_slider_widget")
        self.gridLayout_2.addWidget(self.fill_opacity_slider_widget, 1, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.active_grid_fill_groupbox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.active_grid_fill_groupbox, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.active_grid_area_groupbox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.width_slider_widget = SliderWidget(self.groupBox_3)
        self.width_slider_widget.setProperty("slider_minimum", 64)
        self.width_slider_widget.setProperty("slider_maximum", 4096)
        self.width_slider_widget.setProperty("spinbox_minimum", 64)
        self.width_slider_widget.setProperty("spinbox_maximum", 4096)
        self.width_slider_widget.setProperty("slider_tick_interval", 64)
        self.width_slider_widget.setProperty("slider_single_step", 64)
        self.width_slider_widget.setProperty("slider_page_step", 64)
        self.width_slider_widget.setProperty("spinbox_single_step", 64)
        self.width_slider_widget.setProperty("spinbox_page_step", 64)
        self.width_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.width_slider_widget.setProperty("settings_property", "working_width")
        self.width_slider_widget.setProperty("display_as_float", False)
        self.width_slider_widget.setObjectName("width_slider_widget")
        self.verticalLayout.addWidget(self.width_slider_widget)
        self.height_slider_widget = SliderWidget(self.groupBox_3)
        self.height_slider_widget.setProperty("slider_minimum", 64)
        self.height_slider_widget.setProperty("slider_maximum", 4096)
        self.height_slider_widget.setProperty("spinbox_minimum", 64)
        self.height_slider_widget.setProperty("spinbox_maximum", 4096)
        self.height_slider_widget.setProperty("slider_tick_interval", 64)
        self.height_slider_widget.setProperty("slider_single_step", 64)
        self.height_slider_widget.setProperty("slider_page_step", 64)
        self.height_slider_widget.setProperty("spinbox_single_step", 64)
        self.height_slider_widget.setProperty("spinbox_page_step", 64)
        self.height_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.height_slider_widget.setProperty("display_as_float", False)
        self.height_slider_widget.setObjectName("height_slider_widget")
        self.verticalLayout.addWidget(self.height_slider_widget)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.active_grid_area_groupbox, 0, 0, 1, 1)

        self.retranslateUi(active_grid_settings_widget)
        self.active_grid_border_groupbox.toggled['bool'].connect(active_grid_settings_widget.action_clicked_checkbox_toggle_active_grid_border) # type: ignore
        self.active_grid_fill_groupbox.toggled['bool'].connect(active_grid_settings_widget.action_clicked_checkbox_toggle_active_grid_fill) # type: ignore
        self.active_grid_area_groupbox.toggled['bool'].connect(active_grid_settings_widget.action_clicked_checkbox_toggle_active_grid_area) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(active_grid_settings_widget)

    def retranslateUi(self, active_grid_settings_widget):
        _translate = QtCore.QCoreApplication.translate
        active_grid_settings_widget.setWindowTitle(_translate("active_grid_settings_widget", "Form"))
        self.active_grid_area_groupbox.setTitle(_translate("active_grid_settings_widget", "Active Grid Area"))
        self.active_grid_border_groupbox.setTitle(_translate("active_grid_settings_widget", "Border"))
        self.pushButton.setText(_translate("active_grid_settings_widget", "Choose Color"))
        self.border_opacity_slider_widget.setProperty("label_text", _translate("active_grid_settings_widget", "Border Opacity"))
        self.border_opacity_slider_widget.setProperty("slider_callback", _translate("active_grid_settings_widget", "handle_value_change"))
        self.border_opacity_slider_widget.setProperty("settings_property", _translate("active_grid_settings_widget", "active_grid_settings.border_opacity"))
        self.active_grid_fill_groupbox.setTitle(_translate("active_grid_settings_widget", "Fill"))
        self.fill_opacity_slider_widget.setProperty("label_text", _translate("active_grid_settings_widget", "Fill Opacity"))
        self.fill_opacity_slider_widget.setProperty("slider_callback", _translate("active_grid_settings_widget", "handle_value_change"))
        self.fill_opacity_slider_widget.setProperty("settings_property", _translate("active_grid_settings_widget", "active_grid_settings.fill_opacity"))
        self.pushButton_2.setText(_translate("active_grid_settings_widget", "Choose Color"))
        self.groupBox_3.setTitle(_translate("active_grid_settings_widget", "Size"))
        self.width_slider_widget.setProperty("label_text", _translate("active_grid_settings_widget", "Active Grid Width"))
        self.height_slider_widget.setProperty("label_text", _translate("active_grid_settings_widget", "Active Grid Height"))
        self.height_slider_widget.setProperty("settings_property", _translate("active_grid_settings_widget", "working_height"))
from airunner.widgets.slider.slider_widget import SliderWidget
