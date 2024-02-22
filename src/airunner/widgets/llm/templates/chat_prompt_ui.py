# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/llm/templates/chat_prompt.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_chat_prompt(object):
    def setupUi(self, chat_prompt):
        chat_prompt.setObjectName("chat_prompt")
        chat_prompt.resize(679, 1044)
        self.gridLayout = QtWidgets.QGridLayout(chat_prompt)
        self.gridLayout.setObjectName("gridLayout")
        self.chat_container = QtWidgets.QScrollArea(parent=chat_prompt)
        self.chat_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.chat_container.setWidgetResizable(True)
        self.chat_container.setObjectName("chat_container")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 661, 806))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.conversation = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents)
        self.conversation.setReadOnly(True)
        self.conversation.setObjectName("conversation")
        self.gridLayout_2.addWidget(self.conversation, 1, 0, 1, 1)
        self.action = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.action.setObjectName("action")
        self.gridLayout_2.addWidget(self.action, 0, 0, 1, 1)
        self.chat_container.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.chat_container, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.send_button = QtWidgets.QPushButton(parent=chat_prompt)
        self.send_button.setObjectName("send_button")
        self.horizontalLayout_2.addWidget(self.send_button)
        self.progressBar = QtWidgets.QProgressBar(parent=chat_prompt)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.clear_conversatiion_button = QtWidgets.QPushButton(parent=chat_prompt)
        self.clear_conversatiion_button.setText("")
        icon = QtGui.QIcon.fromTheme("user-trash")
        self.clear_conversatiion_button.setIcon(icon)
        self.clear_conversatiion_button.setObjectName("clear_conversatiion_button")
        self.horizontalLayout_2.addWidget(self.clear_conversatiion_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        self.prompt = QtWidgets.QPlainTextEdit(parent=chat_prompt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prompt.sizePolicy().hasHeightForWidth())
        self.prompt.setSizePolicy(sizePolicy)
        self.prompt.setMinimumSize(QtCore.QSize(0, 150))
        self.prompt.setMaximumSize(QtCore.QSize(16777215, 150))
        self.prompt.setObjectName("prompt")
        self.gridLayout.addWidget(self.prompt, 3, 0, 1, 2)
        self.action1 = QtWidgets.QComboBox(parent=chat_prompt)
        self.action1.setObjectName("action1")
        self.gridLayout.addWidget(self.action1, 2, 0, 1, 2)

        self.retranslateUi(chat_prompt)
        self.send_button.clicked.connect(chat_prompt.action_button_clicked_send) # type: ignore
        self.clear_conversatiion_button.clicked.connect(chat_prompt.action_button_clicked_clear_conversation) # type: ignore
        self.prompt.textChanged.connect(chat_prompt.prompt_text_changed) # type: ignore
        self.action.currentTextChanged['QString'].connect(chat_prompt.llm_action_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(chat_prompt)

    def retranslateUi(self, chat_prompt):
        _translate = QtCore.QCoreApplication.translate
        chat_prompt.setWindowTitle(_translate("chat_prompt", "Form"))
        self.send_button.setToolTip(_translate("chat_prompt", "Send message"))
        self.send_button.setText(_translate("chat_prompt", "Send"))
        self.clear_conversatiion_button.setToolTip(_translate("chat_prompt", "Clear conversation"))
