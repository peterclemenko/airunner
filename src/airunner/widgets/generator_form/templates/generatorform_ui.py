# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/generator_form/templates/generatorform.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_generator_form(object):
    def setupUi(self, generator_form):
        generator_form.setObjectName("generator_form")
        generator_form.resize(361, 946)
        font = QtGui.QFont()
        font.setPointSize(8)
        generator_form.setFont(font)
        generator_form.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.gridLayout_4 = QtWidgets.QGridLayout(generator_form)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.generator_form_tabs = QtWidgets.QTabWidget(parent=generator_form)
        self.generator_form_tabs.setObjectName("generator_form_tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.tab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 341, 904))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(parent=self.scrollAreaWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.prompt = QtWidgets.QPlainTextEdit(parent=self.layoutWidget)
        self.prompt.setObjectName("prompt")
        self.gridLayout_2.addWidget(self.prompt, 1, 0, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.negative_prompt = QtWidgets.QPlainTextEdit(parent=self.layoutWidget1)
        self.negative_prompt.setObjectName("negative_prompt")
        self.verticalLayout_6.addWidget(self.negative_prompt)
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.generate_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.generate_button.setObjectName("generate_button")
        self.horizontalLayout_9.addWidget(self.generate_button)
        self.progress_bar = QtWidgets.QProgressBar(parent=self.scrollAreaWidgetContents)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout_9.addWidget(self.progress_bar)
        self.interrupt_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.interrupt_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.interrupt_button.setObjectName("interrupt_button")
        self.horizontalLayout_9.addWidget(self.interrupt_button)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.generator_form_tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.chat_prompt_widget = ChatPromptWidget(parent=self.tab_2)
        self.chat_prompt_widget.setObjectName("chat_prompt_widget")
        self.gridLayout_5.addWidget(self.chat_prompt_widget, 0, 0, 1, 1)
        self.generator_form_tabs.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.generator_form_tabs, 0, 0, 1, 1)

        self.retranslateUi(generator_form)
        self.generator_form_tabs.setCurrentIndex(0)
        self.pushButton.clicked.connect(generator_form.action_clicked_button_save_prompts) # type: ignore
        self.interrupt_button.clicked.connect(generator_form.handle_interrupt_button_clicked) # type: ignore
        self.generate_button.clicked.connect(generator_form.handle_generate_button_clicked) # type: ignore
        self.prompt.textChanged.connect(generator_form.handle_prompt_changed) # type: ignore
        self.negative_prompt.textChanged.connect(generator_form.handle_negative_prompt_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(generator_form)

    def retranslateUi(self, generator_form):
        _translate = QtCore.QCoreApplication.translate
        generator_form.setWindowTitle(_translate("generator_form", "Form"))
        self.pushButton.setText(_translate("generator_form", "Save Prompts"))
        self.label.setText(_translate("generator_form", "Prompt"))
        self.prompt.setPlaceholderText(_translate("generator_form", "Enter a prompt..."))
        self.label_2.setText(_translate("generator_form", "Negative Prompt"))
        self.negative_prompt.setPlaceholderText(_translate("generator_form", "Enter a negative prompt..."))
        self.generate_button.setText(_translate("generator_form", "Generate"))
        self.interrupt_button.setText(_translate("generator_form", "Interrupt"))
        self.generator_form_tabs.setTabText(self.generator_form_tabs.indexOf(self.tab), _translate("generator_form", "Tab 1"))
        self.generator_form_tabs.setTabText(self.generator_form_tabs.indexOf(self.tab_2), _translate("generator_form", "Tab 2"))
from airunner.widgets.llm.chat_prompt_widget import ChatPromptWidget
