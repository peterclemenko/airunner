# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/breadcrumbs/templates/breadcrumb_container_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_breadcrumb_container_widget(object):
    def setupUi(self, breadcrumb_container_widget):
        breadcrumb_container_widget.setObjectName("breadcrumb_container_widget")
        breadcrumb_container_widget.resize(450, 304)
        self.gridLayout = QtWidgets.QGridLayout(breadcrumb_container_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.breadcrumbs = QtWidgets.QWidget(parent=breadcrumb_container_widget)
        self.breadcrumbs.setObjectName("breadcrumbs")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.breadcrumbs)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.breadcrumb_container = QtWidgets.QHBoxLayout()
        self.breadcrumb_container.setContentsMargins(10, 10, 10, 10)
        self.breadcrumb_container.setObjectName("breadcrumb_container")
        self.gridLayout_2.addLayout(self.breadcrumb_container, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.breadcrumbs, 0, 0, 1, 1)

        self.retranslateUi(breadcrumb_container_widget)
        QtCore.QMetaObject.connectSlotsByName(breadcrumb_container_widget)

    def retranslateUi(self, breadcrumb_container_widget):
        _translate = QtCore.QCoreApplication.translate
        breadcrumb_container_widget.setWindowTitle(_translate("breadcrumb_container_widget", "Form"))
