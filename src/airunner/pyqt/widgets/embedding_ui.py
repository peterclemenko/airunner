# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/embedding.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(230, 62)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.to_negative_prompt_button = QtWidgets.QPushButton(parent=Form)
        self.to_negative_prompt_button.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_negative_prompt_button.setFont(font)
        self.to_negative_prompt_button.setFlat(True)
        self.to_negative_prompt_button.setObjectName("to_negative_prompt_button")
        self.gridLayout_2.addWidget(self.to_negative_prompt_button, 2, 1, 1, 1)
        self.to_prompt_button = QtWidgets.QPushButton(parent=Form)
        self.to_prompt_button.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_prompt_button.setFont(font)
        self.to_prompt_button.setFlat(True)
        self.to_prompt_button.setObjectName("to_prompt_button")
        self.gridLayout_2.addWidget(self.to_prompt_button, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.to_negative_prompt_button.setText(_translate("Form", "Neg Prompt"))
        self.to_prompt_button.setText(_translate("Form", "Prompt"))
        self.label.setText(_translate("Form", "TextLabel"))
