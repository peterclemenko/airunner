# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/canvas_plus/templates/canvas_plus.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_canvas(object):
    def setupUi(self, canvas):
        canvas.setObjectName("canvas")
        canvas.resize(323, 311)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(canvas.sizePolicy().hasHeightForWidth())
        canvas.setSizePolicy(sizePolicy)
        canvas.setMinimumSize(QtCore.QSize(66, 66))
        canvas.setStyleSheet("b")
        self.gridLayout = QtWidgets.QGridLayout(canvas)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.central_widget = QtWidgets.QWidget(parent=canvas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setMinimumSize(QtCore.QSize(200, 200))
        self.central_widget.setStyleSheet("")
        self.central_widget.setObjectName("central_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.canvas_container = QtWidgets.QGraphicsView(parent=self.central_widget)
        self.canvas_container.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.canvas_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.canvas_container.setObjectName("canvas_container")
        self.gridLayout_2.addWidget(self.canvas_container, 0, 0, 1, 1)
        self.canvas_position = QtWidgets.QLabel(parent=self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_position.sizePolicy().hasHeightForWidth())
        self.canvas_position.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.canvas_position.setFont(font)
        self.canvas_position.setStyleSheet("")
        self.canvas_position.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.canvas_position.setObjectName("canvas_position")
        self.gridLayout_2.addWidget(self.canvas_position, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.central_widget, 0, 0, 1, 1)

        self.retranslateUi(canvas)
        QtCore.QMetaObject.connectSlotsByName(canvas)

    def retranslateUi(self, canvas):
        _translate = QtCore.QCoreApplication.translate
        canvas.setWindowTitle(_translate("canvas", "Form"))
        self.canvas_position.setText(_translate("canvas", "TextLabel"))
