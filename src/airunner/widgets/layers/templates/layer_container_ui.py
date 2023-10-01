# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/layers/templates/layer_container.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_layer_container(object):
    def setupUi(self, layer_container):
        layer_container.setObjectName("layer_container")
        layer_container.resize(435, 323)
        self.gridLayout = QtWidgets.QGridLayout(layer_container)
        self.gridLayout.setObjectName("gridLayout")
        self.opacity_widget = SliderWidget(parent=layer_container)
        self.opacity_widget.setObjectName("opacity_widget")
        self.gridLayout.addWidget(self.opacity_widget, 0, 0, 1, 1)
        self.layers = QtWidgets.QScrollArea(parent=layer_container)
        self.layers.setStyleSheet("border-radius: 0px")
        self.layers.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.layers.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.layers.setWidgetResizable(True)
        self.layers.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.layers.setObjectName("layers")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 417, 225))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layers.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.layers, 2, 0, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(parent=layer_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.new_layer_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_layer_button.sizePolicy().hasHeightForWidth())
        self.new_layer_button.setSizePolicy(sizePolicy)
        self.new_layer_button.setMinimumSize(QtCore.QSize(40, 40))
        self.new_layer_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.new_layer_button.setText("")
        icon = QtGui.QIcon.fromTheme("document-new")
        self.new_layer_button.setIcon(icon)
        self.new_layer_button.setIconSize(QtCore.QSize(20, 20))
        self.new_layer_button.setFlat(True)
        self.new_layer_button.setObjectName("new_layer_button")
        self.horizontalLayout_8.addWidget(self.new_layer_button)
        self.layer_up_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_up_button.sizePolicy().hasHeightForWidth())
        self.layer_up_button.setSizePolicy(sizePolicy)
        self.layer_up_button.setMinimumSize(QtCore.QSize(40, 40))
        self.layer_up_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.layer_up_button.setText("")
        icon = QtGui.QIcon.fromTheme("go-up")
        self.layer_up_button.setIcon(icon)
        self.layer_up_button.setIconSize(QtCore.QSize(20, 20))
        self.layer_up_button.setFlat(True)
        self.layer_up_button.setObjectName("layer_up_button")
        self.horizontalLayout_8.addWidget(self.layer_up_button)
        self.layer_down_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_down_button.sizePolicy().hasHeightForWidth())
        self.layer_down_button.setSizePolicy(sizePolicy)
        self.layer_down_button.setMinimumSize(QtCore.QSize(40, 40))
        self.layer_down_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.layer_down_button.setText("")
        icon = QtGui.QIcon.fromTheme("go-down")
        self.layer_down_button.setIcon(icon)
        self.layer_down_button.setIconSize(QtCore.QSize(20, 20))
        self.layer_down_button.setFlat(True)
        self.layer_down_button.setObjectName("layer_down_button")
        self.horizontalLayout_8.addWidget(self.layer_down_button)
        self.merge_layer_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.merge_layer_button.setText("")
        icon = QtGui.QIcon.fromTheme("go-jump")
        self.merge_layer_button.setIcon(icon)
        self.merge_layer_button.setIconSize(QtCore.QSize(20, 20))
        self.merge_layer_button.setFlat(True)
        self.merge_layer_button.setObjectName("merge_layer_button")
        self.horizontalLayout_8.addWidget(self.merge_layer_button)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.delete_layer_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_layer_button.sizePolicy().hasHeightForWidth())
        self.delete_layer_button.setSizePolicy(sizePolicy)
        self.delete_layer_button.setMinimumSize(QtCore.QSize(40, 40))
        self.delete_layer_button.setStyleSheet("border-color: rgb(61, 56, 70);")
        self.delete_layer_button.setText("")
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.delete_layer_button.setIcon(icon)
        self.delete_layer_button.setIconSize(QtCore.QSize(20, 20))
        self.delete_layer_button.setFlat(True)
        self.delete_layer_button.setObjectName("delete_layer_button")
        self.horizontalLayout_8.addWidget(self.delete_layer_button)
        self.gridLayout.addWidget(self.horizontalWidget, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=layer_container)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=layer_container)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.retranslateUi(layer_container)
        self.new_layer_button.clicked.connect(layer_container.action_clicked_button_add_new_layer) # type: ignore
        self.layer_up_button.clicked.connect(layer_container.action_clicked_button_move_layer_up) # type: ignore
        self.layer_down_button.clicked.connect(layer_container.action_clicked_button_move_layer_down) # type: ignore
        self.merge_layer_button.clicked.connect(layer_container.action_clicked_button_merge_selected_layers) # type: ignore
        self.delete_layer_button.clicked.connect(layer_container.action_clicked_button_delete_selected_layers) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(layer_container)

    def retranslateUi(self, layer_container):
        _translate = QtCore.QCoreApplication.translate
        layer_container.setWindowTitle(_translate("layer_container", "Form"))
        self.new_layer_button.setToolTip(_translate("layer_container", "Create a new layer"))
        self.layer_up_button.setToolTip(_translate("layer_container", "Move layer up"))
        self.layer_down_button.setToolTip(_translate("layer_container", "Move layer down"))
        self.merge_layer_button.setToolTip(_translate("layer_container", "Merge selected layers"))
        self.delete_layer_button.setToolTip(_translate("layer_container", "Delete layer"))
from airunner.widgets.slider.slider_widget import SliderWidget
