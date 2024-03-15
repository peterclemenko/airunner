# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/blend_option/templates/blend_option_widget.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 940)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.weight_slider = QtWidgets.QSlider(Form)
        self.weight_slider.setMaximum(100)
        self.weight_slider.setSliderPosition(100)
        self.weight_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.weight_slider.setObjectName("weight_slider")
        self.horizontalLayout.addWidget(self.weight_slider)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.weight_spinbox = QtWidgets.QDoubleSpinBox(Form)
        self.weight_spinbox.setMaximum(1.0)
        self.weight_spinbox.setSingleStep(0.01)
        self.weight_spinbox.setProperty("value", 1.0)
        self.weight_spinbox.setObjectName("weight_spinbox")
        self.horizontalLayout.addWidget(self.weight_spinbox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 2)
        self.image_form = QtWidgets.QFormLayout()
        self.image_form.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.image_form.setObjectName("image_form")
        self.image_container = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_container.sizePolicy().hasHeightForWidth())
        self.image_container.setSizePolicy(sizePolicy)
        self.image_container.setMinimumSize(QtCore.QSize(128, 128))
        self.image_container.setMaximumSize(QtCore.QSize(128, 128))
        self.image_container.setStyleSheet("border: 1px solid black")
        self.image_container.setText("")
        self.image_container.setObjectName("image_container")
        self.image_form.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.image_container)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.layer_combobox = QtWidgets.QComboBox(Form)
        self.layer_combobox.setObjectName("layer_combobox")
        self.verticalLayout.addWidget(self.layer_combobox)
        self.import_image_button = QtWidgets.QPushButton(Form)
        self.import_image_button.setObjectName("import_image_button")
        self.verticalLayout.addWidget(self.import_image_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.image_form.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verticalLayout)
        self.gridLayout_2.addLayout(self.image_form, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 1, 1, 1)
        self.image_or_text_combobox = QtWidgets.QComboBox(Form)
        self.image_or_text_combobox.setObjectName("image_or_text_combobox")
        self.image_or_text_combobox.addItem("")
        self.image_or_text_combobox.addItem("")
        self.gridLayout_2.addWidget(self.image_or_text_combobox, 0, 0, 1, 2)
        self.delete_button = QtWidgets.QPushButton(Form)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout_2.addWidget(self.delete_button, 4, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.import_image_button.setText(_translate("Form", "Import new image"))
        self.image_or_text_combobox.setItemText(0, _translate("Form", "Image"))
        self.image_or_text_combobox.setItemText(1, _translate("Form", "Text"))
        self.delete_button.setText(_translate("Form", "Delete"))
