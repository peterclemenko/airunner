# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/model_manager/templates/custom.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_custom_model_widget(object):
    def setupUi(self, custom_model_widget):
        custom_model_widget.setObjectName("custom_model_widget")
        custom_model_widget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(custom_model_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.custom_scroll_area = QtWidgets.QScrollArea(parent=custom_model_widget)
        self.custom_scroll_area.setWidgetResizable(True)
        self.custom_scroll_area.setObjectName("custom_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 228))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.custom_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.custom_scroll_area, 1, 0, 1, 1)
        self.scan_for_models_button = QtWidgets.QPushButton(parent=custom_model_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scan_for_models_button.setFont(font)
        self.scan_for_models_button.setObjectName("scan_for_models_button")
        self.gridLayout.addWidget(self.scan_for_models_button, 2, 0, 1, 1)
        self.toggle_all = QtWidgets.QCheckBox(parent=custom_model_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.toggle_all.setFont(font)
        self.toggle_all.setObjectName("toggle_all")
        self.gridLayout.addWidget(self.toggle_all, 0, 0, 1, 1)

        self.retranslateUi(custom_model_widget)
        self.scan_for_models_button.clicked.connect(custom_model_widget.action_button_clicked_scan_for_models) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(custom_model_widget)

    def retranslateUi(self, custom_model_widget):
        _translate = QtCore.QCoreApplication.translate
        custom_model_widget.setWindowTitle(_translate("custom_model_widget", "Form"))
        self.scan_for_models_button.setText(_translate("custom_model_widget", "Scan for models"))
        self.toggle_all.setText(_translate("custom_model_widget", "Toggle all"))
