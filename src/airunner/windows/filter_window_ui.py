# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/windows/filter_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_filter_window(object):
    def setupUi(self, filter_window):
        filter_window.setObjectName("filter_window")
        filter_window.resize(352, 94)
        self.gridLayout = QtWidgets.QGridLayout(filter_window)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=filter_window)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=filter_window)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.auto_apply = QtWidgets.QCheckBox(parent=filter_window)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.auto_apply.setFont(font)
        self.auto_apply.setObjectName("auto_apply")
        self.gridLayout.addWidget(self.auto_apply, 2, 0, 1, 1)
        self.content = QtWidgets.QFrame(parent=filter_window)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.content.setFont(font)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.content)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.content, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)

        self.retranslateUi(filter_window)
        self.buttonBox.accepted.connect(filter_window.accept) # type: ignore
        self.buttonBox.rejected.connect(filter_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(filter_window)

    def retranslateUi(self, filter_window):
        _translate = QtCore.QCoreApplication.translate
        filter_window.setWindowTitle(_translate("filter_window", "Dialog"))
        self.label.setText(_translate("filter_window", "Filter Name"))
        self.auto_apply.setText(_translate("filter_window", "Auto Apply Filter"))
