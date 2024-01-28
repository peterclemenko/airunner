# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/llm/templates/llm_widget.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_llm_widget(object):
    def setupUi(self, llm_widget):
        llm_widget.setObjectName("llm_widget")
        llm_widget.resize(622, 974)
        self.gridLayout = QtWidgets.QGridLayout(llm_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=llm_widget)
        self.tabWidget.setObjectName("tabWidget")
        self.chat = QtWidgets.QWidget()
        self.chat.setObjectName("chat")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.chat)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.chat_prompt_widget = ChatPromptWidget(parent=self.chat)
        self.chat_prompt_widget.setObjectName("chat_prompt_widget")
        self.gridLayout_8.addWidget(self.chat_prompt_widget, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("user-available")
        self.tabWidget.addTab(self.chat, icon, "")
        self.preferences = QtWidgets.QWidget()
        self.preferences.setObjectName("preferences")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.preferences)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.llm_preferences_widget = LLMPreferencesWidget(parent=self.preferences)
        self.llm_preferences_widget.setObjectName("llm_preferences_widget")
        self.gridLayout_2.addWidget(self.llm_preferences_widget, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("preferences-desktop")
        self.tabWidget.addTab(self.preferences, icon, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.settings)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.llm_settings_widget = LLMSettingsWidget(parent=self.settings)
        self.llm_settings_widget.setObjectName("llm_settings_widget")
        self.gridLayout_5.addWidget(self.llm_settings_widget, 0, 0, 1, 1)
        icon = QtGui.QIcon.fromTheme("preferences-other")
        self.tabWidget.addTab(self.settings, icon, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(llm_widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(llm_widget)

    def retranslateUi(self, llm_widget):
        _translate = QtCore.QCoreApplication.translate
        llm_widget.setWindowTitle(_translate("llm_widget", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chat), _translate("llm_widget", "Chat"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preferences), _translate("llm_widget", "Preferences"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("llm_widget", "Settings"))
from airunner.widgets.llm.chat_prompt_widget import ChatPromptWidget
from airunner.widgets.llm.llm_preferences_widget import LLMPreferencesWidget
from airunner.widgets.llm.llm_settings_widget import LLMSettingsWidget
