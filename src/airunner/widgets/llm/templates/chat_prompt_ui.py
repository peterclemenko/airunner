# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/llm/templates/chat_prompt.ui'
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
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.chat_prompt_splitter = QtWidgets.QSplitter(parent=chat_prompt)
        self.chat_prompt_splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.chat_prompt_splitter.setChildrenCollapsible(False)
        self.chat_prompt_splitter.setObjectName("chat_prompt_splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.chat_prompt_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat_container = QtWidgets.QScrollArea(parent=self.verticalLayoutWidget)
        self.chat_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.chat_container.setWidgetResizable(True)
        self.chat_container.setObjectName("chat_container")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 659, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.conversation = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents)
        self.conversation.setReadOnly(True)
        self.conversation.setObjectName("conversation")
        self.gridLayout_2.addWidget(self.conversation, 0, 0, 1, 1)
        self.chat_container.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.chat_container)
        self.prompt = QtWidgets.QPlainTextEdit(parent=self.chat_prompt_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prompt.sizePolicy().hasHeightForWidth())
        self.prompt.setSizePolicy(sizePolicy)
        self.prompt.setMinimumSize(QtCore.QSize(0, 150))
        self.prompt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.prompt.setObjectName("prompt")
        self.gridLayout.addWidget(self.chat_prompt_splitter, 1, 0, 1, 1)
        self.action = QtWidgets.QComboBox(parent=chat_prompt)
        self.action.setObjectName("action")
        self.gridLayout.addWidget(self.action, 2, 0, 1, 1)

        self.retranslateUi(chat_prompt)
        self.prompt.textChanged.connect(chat_prompt.prompt_text_changed) # type: ignore
        self.action.currentTextChanged['QString'].connect(chat_prompt.llm_action_changed) # type: ignore
        self.send_button.clicked.connect(chat_prompt.action_button_clicked_send) # type: ignore
        self.clear_conversatiion_button.clicked.connect(chat_prompt.action_button_clicked_clear_conversation) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(chat_prompt)

    def retranslateUi(self, chat_prompt):
        _translate = QtCore.QCoreApplication.translate
        chat_prompt.setWindowTitle(_translate("chat_prompt", "Form"))
        self.send_button.setToolTip(_translate("chat_prompt", "Send message"))
        self.send_button.setText(_translate("chat_prompt", "Send"))
        self.clear_conversatiion_button.setToolTip(_translate("chat_prompt", "Clear conversation"))
