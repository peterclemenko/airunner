# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/image/templates/image_panel_widget.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_image_panel_widget(object):
    def setupUi(self, image_panel_widget):
        image_panel_widget.setObjectName("image_panel_widget")
        image_panel_widget.resize(558, 286)
        self.gridLayout = QtWidgets.QGridLayout(image_panel_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(image_panel_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 556, 284))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(image_panel_widget)
        QtCore.QMetaObject.connectSlotsByName(image_panel_widget)

    def retranslateUi(self, image_panel_widget):
        _translate = QtCore.QCoreApplication.translate
        image_panel_widget.setWindowTitle(_translate("image_panel_widget", "Form"))
