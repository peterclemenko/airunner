# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/toolbar.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(94, 543)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.side_toolbar_container = QtWidgets.QFrame(parent=Form)
        self.side_toolbar_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.side_toolbar_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.side_toolbar_container.setObjectName("side_toolbar_container")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.side_toolbar_container)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.active_grid_area_button = QtWidgets.QPushButton(parent=self.side_toolbar_container)
        self.active_grid_area_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.active_grid_area_button.sizePolicy().hasHeightForWidth())
        self.active_grid_area_button.setSizePolicy(sizePolicy)
        self.active_grid_area_button.setMinimumSize(QtCore.QSize(0, 0))
        self.active_grid_area_button.setMaximumSize(QtCore.QSize(40, 40))
        self.active_grid_area_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.active_grid_area_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/../../src/icons/038-drag.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.active_grid_area_button.setIcon(icon)
        self.active_grid_area_button.setIconSize(QtCore.QSize(24, 24))
        self.active_grid_area_button.setCheckable(True)
        self.active_grid_area_button.setChecked(False)
        self.active_grid_area_button.setAutoExclusive(False)
        self.active_grid_area_button.setFlat(True)
        self.active_grid_area_button.setObjectName("active_grid_area_button")
        self.gridLayout_2.addWidget(self.active_grid_area_button, 1, 0, 1, 1)
        self.nsfw_button = QtWidgets.QPushButton(parent=self.side_toolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nsfw_button.sizePolicy().hasHeightForWidth())
        self.nsfw_button.setSizePolicy(sizePolicy)
        self.nsfw_button.setMinimumSize(QtCore.QSize(0, 0))
        self.nsfw_button.setMaximumSize(QtCore.QSize(40, 40))
        self.nsfw_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.nsfw_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/../../src/icons/039-18.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.nsfw_button.setIcon(icon1)
        self.nsfw_button.setIconSize(QtCore.QSize(24, 24))
        self.nsfw_button.setCheckable(True)
        self.nsfw_button.setChecked(False)
        self.nsfw_button.setFlat(True)
        self.nsfw_button.setObjectName("nsfw_button")
        self.gridLayout_2.addWidget(self.nsfw_button, 9, 0, 1, 1)
        self.grid_button = QtWidgets.QPushButton(parent=self.side_toolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_button.sizePolicy().hasHeightForWidth())
        self.grid_button.setSizePolicy(sizePolicy)
        self.grid_button.setMinimumSize(QtCore.QSize(0, 0))
        self.grid_button.setMaximumSize(QtCore.QSize(40, 40))
        self.grid_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.grid_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/../../src/icons/032-pixels.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.grid_button.setIcon(icon2)
        self.grid_button.setIconSize(QtCore.QSize(24, 24))
        self.grid_button.setCheckable(True)
        self.grid_button.setFlat(True)
        self.grid_button.setObjectName("grid_button")
        self.gridLayout_2.addWidget(self.grid_button, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 0, 1, 1)
        self.focus_button = QtWidgets.QPushButton(parent=self.side_toolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.focus_button.sizePolicy().hasHeightForWidth())
        self.focus_button.setSizePolicy(sizePolicy)
        self.focus_button.setMinimumSize(QtCore.QSize(0, 0))
        self.focus_button.setMaximumSize(QtCore.QSize(40, 40))
        self.focus_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.focus_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/../../src/icons/037-focus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.focus_button.setIcon(icon3)
        self.focus_button.setIconSize(QtCore.QSize(24, 24))
        self.focus_button.setFlat(True)
        self.focus_button.setObjectName("focus_button")
        self.gridLayout_2.addWidget(self.focus_button, 5, 0, 1, 1)
        self.eraser_button = QtWidgets.QPushButton(parent=self.side_toolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraser_button.sizePolicy().hasHeightForWidth())
        self.eraser_button.setSizePolicy(sizePolicy)
        self.eraser_button.setMinimumSize(QtCore.QSize(0, 0))
        self.eraser_button.setMaximumSize(QtCore.QSize(40, 40))
        self.eraser_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.eraser_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/../../src/icons/014-eraser.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.eraser_button.setIcon(icon4)
        self.eraser_button.setIconSize(QtCore.QSize(24, 24))
        self.eraser_button.setCheckable(True)
        self.eraser_button.setChecked(False)
        self.eraser_button.setFlat(True)
        self.eraser_button.setObjectName("eraser_button")
        self.gridLayout_2.addWidget(self.eraser_button, 3, 0, 1, 1)
        self.brush_button = QtWidgets.QPushButton(parent=self.side_toolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brush_button.sizePolicy().hasHeightForWidth())
        self.brush_button.setSizePolicy(sizePolicy)
        self.brush_button.setMinimumSize(QtCore.QSize(0, 0))
        self.brush_button.setMaximumSize(QtCore.QSize(40, 40))
        self.brush_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/../../src/icons/011-pencil.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.brush_button.setIcon(icon5)
        self.brush_button.setIconSize(QtCore.QSize(24, 24))
        self.brush_button.setCheckable(True)
        self.brush_button.setFlat(True)
        self.brush_button.setObjectName("brush_button")
        self.gridLayout_2.addWidget(self.brush_button, 2, 0, 1, 1)
        self.move_button = QtWidgets.QPushButton(parent=self.side_toolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.move_button.sizePolicy().hasHeightForWidth())
        self.move_button.setSizePolicy(sizePolicy)
        self.move_button.setMaximumSize(QtCore.QSize(40, 40))
        self.move_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/../../src/icons/013-move-selector.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.move_button.setIcon(icon6)
        self.move_button.setIconSize(QtCore.QSize(24, 24))
        self.move_button.setCheckable(True)
        self.move_button.setFlat(True)
        self.move_button.setObjectName("move_button")
        self.gridLayout_2.addWidget(self.move_button, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.side_toolbar_container, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.active_grid_area_button.setToolTip(_translate("Form", "Active Grid Area"))
        self.active_grid_area_button.setShortcut(_translate("Form", "M"))
        self.nsfw_button.setToolTip(_translate("Form", "Toggle NSFW Filter"))
        self.grid_button.setToolTip(_translate("Form", "Toggle Grid"))
        self.grid_button.setShortcut(_translate("Form", "G"))
        self.focus_button.setToolTip(_translate("Form", "Recenter Canvas"))
        self.eraser_button.setToolTip(_translate("Form", "Eraser"))
        self.eraser_button.setShortcut(_translate("Form", "E"))
        self.brush_button.setToolTip(_translate("Form", "Pen"))
        self.brush_button.setStyleSheet(_translate("Form", "border-color: rgb(61, 56, 70);"))
        self.brush_button.setShortcut(_translate("Form", "B"))
        self.move_button.setStyleSheet(_translate("Form", "border-color: rgb(61, 56, 70);"))
