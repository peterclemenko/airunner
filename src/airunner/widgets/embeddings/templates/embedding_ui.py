# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/embeddings/templates/embedding.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_embedding(object):
    def setupUi(self, embedding):
        embedding.setObjectName("embedding")
        embedding.resize(371, 90)
        self.gridLayout_2 = QtWidgets.QGridLayout(embedding)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.enabledCheckbox = QtWidgets.QGroupBox(parent=embedding)
        self.enabledCheckbox.setCheckable(True)
        self.enabledCheckbox.setChecked(False)
        self.enabledCheckbox.setObjectName("enabledCheckbox")
        self.gridLayout = QtWidgets.QGridLayout(self.enabledCheckbox)
        self.gridLayout.setObjectName("gridLayout")
        self.to_prompt_button = QtWidgets.QPushButton(parent=self.enabledCheckbox)
        self.to_prompt_button.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_prompt_button.setFont(font)
        self.to_prompt_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.to_prompt_button.setIcon(icon)
        self.to_prompt_button.setFlat(False)
        self.to_prompt_button.setObjectName("to_prompt_button")
        self.gridLayout.addWidget(self.to_prompt_button, 1, 0, 1, 1)
        self.to_negative_prompt_button = QtWidgets.QPushButton(parent=self.enabledCheckbox)
        self.to_negative_prompt_button.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.to_negative_prompt_button.setFont(font)
        self.to_negative_prompt_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.to_negative_prompt_button.setIcon(icon)
        self.to_negative_prompt_button.setFlat(False)
        self.to_negative_prompt_button.setObjectName("to_negative_prompt_button")
        self.gridLayout.addWidget(self.to_negative_prompt_button, 1, 1, 1, 1)
        self.tags = QtWidgets.QLabel(parent=self.enabledCheckbox)
        self.tags.setObjectName("tags")
        self.gridLayout.addWidget(self.tags, 0, 0, 1, 2)
        self.copy_button = QtWidgets.QPushButton(parent=self.enabledCheckbox)
        self.copy_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.copy_button.setText("")
        icon = QtGui.QIcon.fromTheme("edit-copy")
        self.copy_button.setIcon(icon)
        self.copy_button.setObjectName("copy_button")
        self.gridLayout.addWidget(self.copy_button, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.enabledCheckbox, 0, 0, 1, 2)

        self.retranslateUi(embedding)
        self.to_prompt_button.clicked.connect(embedding.action_clicked_button_to_prompt) # type: ignore
        self.to_negative_prompt_button.clicked.connect(embedding.action_clicked_button_to_negative_prompt) # type: ignore
        self.enabledCheckbox.toggled['bool'].connect(embedding.action_toggled_embedding) # type: ignore
        self.copy_button.clicked.connect(embedding.action_clicked_copy) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(embedding)

    def retranslateUi(self, embedding):
        _translate = QtCore.QCoreApplication.translate
        embedding.setWindowTitle(_translate("embedding", "Form"))
        self.enabledCheckbox.setTitle(_translate("embedding", "Embedding name here"))
        self.to_prompt_button.setText(_translate("embedding", "Prompt"))
        self.to_negative_prompt_button.setText(_translate("embedding", "Negative"))
        self.tags.setText(_translate("embedding", "Tags"))
