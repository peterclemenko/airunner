# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/image/templates/folder_widget.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_folder_widget(object):
    def setupUi(self, folder_widget):
        folder_widget.setObjectName("folder_widget")
        folder_widget.resize(94, 93)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(folder_widget.sizePolicy().hasHeightForWidth())
        folder_widget.setSizePolicy(sizePolicy)
        folder_widget.setMaximumSize(QtCore.QSize(94, 93))
        self.gridLayout = QtWidgets.QGridLayout(folder_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=folder_widget)
        self.pushButton.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton.setText("")
        icon = QtGui.QIcon.fromTheme("folder")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=folder_widget)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(folder_widget)
        self.pushButton.clicked.connect(folder_widget.folder_clicked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(folder_widget)

    def retranslateUi(self, folder_widget):
        _translate = QtCore.QCoreApplication.translate
        folder_widget.setWindowTitle(_translate("folder_widget", "Form"))
        self.label.setText(_translate("folder_widget", "TextLabel"))
