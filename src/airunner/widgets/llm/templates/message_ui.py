# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/llm/templates/message.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_message(object):
    def setupUi(self, message):
        message.setObjectName("message")
        message.resize(605, 707)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(message.sizePolicy().hasHeightForWidth())
        message.setSizePolicy(sizePolicy)
        message.setMinimumSize(QtCore.QSize(0, 40))
        self.gridLayout = QtWidgets.QGridLayout(message)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_name = QtWidgets.QLabel(parent=message)
        self.user_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.user_name.setObjectName("user_name")
        self.horizontalLayout.addWidget(self.user_name)
        self.content = QtWidgets.QTextEdit(parent=message)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setMinimumSize(QtCore.QSize(0, 40))
        self.content.setStyleSheet("border-radius: 5px; border: 5px solid #1f1f1f; background-color: #1f1f1f; color: #ffffff;")
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.content.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.content.setObjectName("content")
        self.horizontalLayout.addWidget(self.content)
        self.bot_name = QtWidgets.QLabel(parent=message)
        self.bot_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.bot_name.setObjectName("bot_name")
        self.horizontalLayout.addWidget(self.bot_name)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(message)
        QtCore.QMetaObject.connectSlotsByName(message)

    def retranslateUi(self, message):
        _translate = QtCore.QCoreApplication.translate
        message.setWindowTitle(_translate("message", "Form"))
        self.user_name.setText(_translate("message", "TextLabel"))
        self.bot_name.setText(_translate("message", "TextLabel"))
