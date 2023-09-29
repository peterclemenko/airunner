# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/model_manager/templates/model_manager.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_model_manager(object):
    def setupUi(self, model_manager):
        model_manager.setObjectName("model_manager")
        model_manager.resize(300, 405)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(model_manager.sizePolicy().hasHeightForWidth())
        model_manager.setSizePolicy(sizePolicy)
        model_manager.setMinimumSize(QtCore.QSize(0, 405))
        font = QtGui.QFont()
        font.setPointSize(9)
        model_manager.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(model_manager)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs = QtWidgets.QTabWidget(parent=model_manager)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabs.setFont(font)
        self.tabs.setStyleSheet("")
        self.tabs.setTabsClosable(False)
        self.tabs.setTabBarAutoHide(False)
        self.tabs.setObjectName("tabs")
        self.default_tab = QtWidgets.QWidget()
        self.default_tab.setObjectName("default_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.default_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = DefaultModelWidget(parent=self.default_tab)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.tabs.addTab(self.default_tab, "")
        self.custom_tab = QtWidgets.QWidget()
        self.custom_tab.setObjectName("custom_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.custom_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = CustomModelWidget(parent=self.custom_tab)
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.tabs.addTab(self.custom_tab, "")
        self.import_tab = QtWidgets.QWidget()
        self.import_tab.setObjectName("import_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.import_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_3 = ImportWidget(parent=self.import_tab)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 1, 1)
        self.tabs.addTab(self.import_tab, "")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)

        self.retranslateUi(model_manager)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(model_manager)

    def retranslateUi(self, model_manager):
        _translate = QtCore.QCoreApplication.translate
        model_manager.setWindowTitle(_translate("model_manager", "Form"))
        self.tabs.setTabText(self.tabs.indexOf(self.default_tab), _translate("model_manager", "Default"))
        self.tabs.setTabText(self.tabs.indexOf(self.custom_tab), _translate("model_manager", "Custom"))
        self.tabs.setTabText(self.tabs.indexOf(self.import_tab), _translate("model_manager", "Import"))
from airunner.pyqt.widgets.model_manager.custom_widget import CustomModelWidget
from airunner.pyqt.widgets.model_manager.default_widget import DefaultModelWidget
from airunner.pyqt.widgets.model_manager.import_widget import ImportWidget
