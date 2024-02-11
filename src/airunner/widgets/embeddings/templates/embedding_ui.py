# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/embeddings/templates/embedding.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_embedding(object):
    def setupUi(self, embedding):
        embedding.setObjectName("embedding")
        embedding.resize(400, 168)
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
        self.trigger_word_edit = QtWidgets.QLineEdit(parent=self.enabledCheckbox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trigger_word_edit.setFont(font)
        self.trigger_word_edit.setObjectName("trigger_word_edit")
        self.gridLayout.addWidget(self.trigger_word_edit, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.enabledCheckbox, 0, 0, 1, 2)

        self.retranslateUi(embedding)
        self.enabledCheckbox.toggled['bool'].connect(embedding.action_toggled_embedding) # type: ignore
        self.trigger_word_edit.textChanged['QString'].connect(embedding.action_changed_trigger_word) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(embedding)

    def retranslateUi(self, embedding):
        _translate = QtCore.QCoreApplication.translate
        embedding.setWindowTitle(_translate("embedding", "Form"))
        self.enabledCheckbox.setTitle(_translate("embedding", "Embedding name here"))
        self.trigger_word_edit.setToolTip(_translate("embedding", "<html><head/><body><p>Some LoRA require a trigger word to activate.</p><p>Make a note here for your records.</p></body></html>"))
        self.trigger_word_edit.setPlaceholderText(_translate("embedding", "Trigger words (comma separated)"))
