# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/gif/templates/gif_panel.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_gif_panel_widget(object):
    def setupUi(self, gif_panel_widget):
        gif_panel_widget.setObjectName("gif_panel_widget")
        gif_panel_widget.resize(402, 430)
        self.gridLayout = QtWidgets.QGridLayout(gif_panel_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=gif_panel_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 428))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(gif_panel_widget)
        QtCore.QMetaObject.connectSlotsByName(gif_panel_widget)

    def retranslateUi(self, gif_panel_widget):
        _translate = QtCore.QCoreApplication.translate
        gif_panel_widget.setWindowTitle(_translate("gif_panel_widget", "Form"))
