# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/keyboard_shortcuts/templates/keyboard_shortcut_widget.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_keyboard_shortcut_widget(object):
    def setupUi(self, keyboard_shortcut_widget):
        keyboard_shortcut_widget.setObjectName("keyboard_shortcut_widget")
        keyboard_shortcut_widget.resize(400, 43)
        self.horizontalLayout = QtWidgets.QHBoxLayout(keyboard_shortcut_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=keyboard_shortcut_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_edit = QtWidgets.QLineEdit(parent=keyboard_shortcut_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_edit.setFont(font)
        self.line_edit.setReadOnly(True)
        self.line_edit.setObjectName("line_edit")
        self.horizontalLayout.addWidget(self.line_edit)

        self.retranslateUi(keyboard_shortcut_widget)
        QtCore.QMetaObject.connectSlotsByName(keyboard_shortcut_widget)

    def retranslateUi(self, keyboard_shortcut_widget):
        _translate = QtCore.QCoreApplication.translate
        keyboard_shortcut_widget.setWindowTitle(_translate("keyboard_shortcut_widget", "Form"))
        self.label.setText(_translate("keyboard_shortcut_widget", "TextLabel"))
