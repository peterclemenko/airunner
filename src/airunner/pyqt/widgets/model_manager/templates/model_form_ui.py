# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/model_manager/templates/model_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_model_form_widget(object):
    def setupUi(self, model_form_widget):
        model_form_widget.setObjectName("model_form_widget")
        model_form_widget.resize(465, 335)
        self.gridLayout_3 = QtWidgets.QGridLayout(model_form_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.model_name = QtWidgets.QLineEdit(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.model_name.setFont(font)
        self.model_name.setObjectName("model_name")
        self.gridLayout_3.addWidget(self.model_name, 1, 0, 1, 1)
        self.path_label = QtWidgets.QLabel(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.gridLayout_3.addWidget(self.path_label, 2, 0, 1, 1)
        self.path_line_edit = QtWidgets.QLineEdit(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.path_line_edit.setFont(font)
        self.path_line_edit.setObjectName("path_line_edit")
        self.gridLayout_3.addWidget(self.path_line_edit, 3, 0, 1, 1)
        self.branch_label = QtWidgets.QLabel(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.branch_label.setFont(font)
        self.branch_label.setObjectName("branch_label")
        self.gridLayout_3.addWidget(self.branch_label, 4, 0, 1, 1)
        self.branch_line_edit = QtWidgets.QLineEdit(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.branch_line_edit.setFont(font)
        self.branch_line_edit.setObjectName("branch_line_edit")
        self.gridLayout_3.addWidget(self.branch_line_edit, 5, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.versions = QtWidgets.QComboBox(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.versions.setFont(font)
        self.versions.setObjectName("versions")
        self.gridLayout_2.addWidget(self.versions, 1, 0, 1, 1)
        self.category = QtWidgets.QComboBox(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.category.setFont(font)
        self.category.setObjectName("category")
        self.gridLayout_2.addWidget(self.category, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 6, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.pipeline_action = QtWidgets.QComboBox(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pipeline_action.setFont(font)
        self.pipeline_action.setObjectName("pipeline_action")
        self.gridLayout.addWidget(self.pipeline_action, 1, 0, 1, 1)
        self.pipeline_class_line_edit = QtWidgets.QLineEdit(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pipeline_class_line_edit.setFont(font)
        self.pipeline_class_line_edit.setObjectName("pipeline_class_line_edit")
        self.gridLayout.addWidget(self.pipeline_class_line_edit, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 7, 0, 1, 1)
        self.enabled = QtWidgets.QCheckBox(parent=model_form_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.enabled.setFont(font)
        self.enabled.setObjectName("enabled")
        self.gridLayout_3.addWidget(self.enabled, 8, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 9, 0, 1, 1)

        self.retranslateUi(model_form_widget)
        QtCore.QMetaObject.connectSlotsByName(model_form_widget)

    def retranslateUi(self, model_form_widget):
        _translate = QtCore.QCoreApplication.translate
        model_form_widget.setWindowTitle(_translate("model_form_widget", "Form"))
        self.label_5.setText(_translate("model_form_widget", "Name"))
        self.model_name.setPlaceholderText(_translate("model_form_widget", "Name"))
        self.path_label.setText(_translate("model_form_widget", "Path"))
        self.path_line_edit.setPlaceholderText(_translate("model_form_widget", "Path"))
        self.branch_label.setText(_translate("model_form_widget", "Branch"))
        self.branch_line_edit.setPlaceholderText(_translate("model_form_widget", "Branch"))
        self.label_7.setText(_translate("model_form_widget", "Version"))
        self.label.setText(_translate("model_form_widget", "Category"))
        self.label_2.setText(_translate("model_form_widget", "Pipeline Action"))
        self.label_3.setText(_translate("model_form_widget", "Pipeline Class"))
        self.pipeline_class_line_edit.setPlaceholderText(_translate("model_form_widget", "Pipeline class"))
        self.enabled.setText(_translate("model_form_widget", "Enabled"))
