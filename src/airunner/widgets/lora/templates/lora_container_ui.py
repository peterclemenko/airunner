# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/lora/templates/lora_container.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_lora_container(object):
    def setupUi(self, lora_container):
        lora_container.setObjectName("lora_container")
        lora_container.resize(583, 775)
        self.gridLayout = QtWidgets.QGridLayout(lora_container)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(lora_container)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toggleAllLora = QtWidgets.QCheckBox(lora_container)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toggleAllLora.setFont(font)
        self.toggleAllLora.setChecked(False)
        self.toggleAllLora.setTristate(False)
        self.toggleAllLora.setObjectName("toggleAllLora")
        self.horizontalLayout.addWidget(self.toggleAllLora)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.lora_scroll_area = QtWidgets.QScrollArea(lora_container)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lora_scroll_area.setFont(font)
        self.lora_scroll_area.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lora_scroll_area.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.lora_scroll_area.setWidgetResizable(True)
        self.lora_scroll_area.setObjectName("lora_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 565, 724))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lora_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.lora_scroll_area, 1, 0, 1, 1)

        self.retranslateUi(lora_container)
        self.toggleAllLora.toggled['bool'].connect(lora_container.toggle_all) # type: ignore
        self.lineEdit.textEdited['QString'].connect(lora_container.search_text_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(lora_container)

    def retranslateUi(self, lora_container):
        _translate = QtCore.QCoreApplication.translate
        lora_container.setWindowTitle(_translate("lora_container", "Form"))
        self.lineEdit.setPlaceholderText(_translate("lora_container", "Search"))
        self.toggleAllLora.setText(_translate("lora_container", "Toggle all"))
