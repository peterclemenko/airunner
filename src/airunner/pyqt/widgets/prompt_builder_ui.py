# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/pyqt/widgets/prompt_builder.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 315)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 315))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.weights = QtWidgets.QGridLayout()
        self.weights.setObjectName("weights")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.weights.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.weights.addWidget(self.label_3, 1, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.weights.addWidget(self.label_7, 0, 2, 1, 1)
        self.text_prompt_weight_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.text_prompt_weight_label.setFont(font)
        self.text_prompt_weight_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.text_prompt_weight_label.setObjectName("text_prompt_weight_label")
        self.weights.addWidget(self.text_prompt_weight_label, 1, 1, 1, 1)
        self.auto_prompt_weight_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.auto_prompt_weight_label.setFont(font)
        self.auto_prompt_weight_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.auto_prompt_weight_label.setObjectName("auto_prompt_weight_label")
        self.weights.addWidget(self.auto_prompt_weight_label, 1, 3, 1, 1)
        self.negative_auto_prompt_weight_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.negative_auto_prompt_weight_label.setFont(font)
        self.negative_auto_prompt_weight_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.negative_auto_prompt_weight_label.setObjectName("negative_auto_prompt_weight_label")
        self.weights.addWidget(self.negative_auto_prompt_weight_label, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.weights.addWidget(self.label_6, 2, 0, 1, 1)
        self.prompt_weight_distribution_slider = QtWidgets.QSlider(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prompt_weight_distribution_slider.sizePolicy().hasHeightForWidth())
        self.prompt_weight_distribution_slider.setSizePolicy(sizePolicy)
        self.prompt_weight_distribution_slider.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prompt_weight_distribution_slider.setFont(font)
        self.prompt_weight_distribution_slider.setMaximum(100)
        self.prompt_weight_distribution_slider.setPageStep(1)
        self.prompt_weight_distribution_slider.setProperty("value", 50)
        self.prompt_weight_distribution_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.prompt_weight_distribution_slider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.prompt_weight_distribution_slider.setTickInterval(1)
        self.prompt_weight_distribution_slider.setObjectName("prompt_weight_distribution_slider")
        self.weights.addWidget(self.prompt_weight_distribution_slider, 1, 2, 1, 1)
        self.negative_text_prompt_weight_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.negative_text_prompt_weight_label.setFont(font)
        self.negative_text_prompt_weight_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.negative_text_prompt_weight_label.setObjectName("negative_text_prompt_weight_label")
        self.weights.addWidget(self.negative_text_prompt_weight_label, 2, 1, 1, 1)
        self.negative_prompt_weight_distribution_slider = QtWidgets.QSlider(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.negative_prompt_weight_distribution_slider.sizePolicy().hasHeightForWidth())
        self.negative_prompt_weight_distribution_slider.setSizePolicy(sizePolicy)
        self.negative_prompt_weight_distribution_slider.setMinimumSize(QtCore.QSize(50, 0))
        self.negative_prompt_weight_distribution_slider.setMaximum(100)
        self.negative_prompt_weight_distribution_slider.setPageStep(1)
        self.negative_prompt_weight_distribution_slider.setProperty("value", 50)
        self.negative_prompt_weight_distribution_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.negative_prompt_weight_distribution_slider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.negative_prompt_weight_distribution_slider.setTickInterval(1)
        self.negative_prompt_weight_distribution_slider.setObjectName("negative_prompt_weight_distribution_slider")
        self.weights.addWidget(self.negative_prompt_weight_distribution_slider, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.weights.addWidget(self.label_5, 2, 4, 1, 1)
        self.gridLayout.addLayout(self.weights, 2, 0, 1, 1)
        self.tabs = QtWidgets.QTabWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabs.setFont(font)
        self.tabs.setStyleSheet("")
        self.tabs.setObjectName("tabs")
        self.basic = QtWidgets.QWidget()
        self.basic.setObjectName("basic")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.basic)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(parent=self.basic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.basic_category = QtWidgets.QComboBox(parent=self.basic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basic_category.sizePolicy().hasHeightForWidth())
        self.basic_category.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.basic_category.setFont(font)
        self.basic_category.setObjectName("basic_category")
        self.verticalLayout_2.addWidget(self.basic_category)
        self.label_9 = QtWidgets.QLabel(parent=self.basic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.basic_prompt = QtWidgets.QComboBox(parent=self.basic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basic_prompt.sizePolicy().hasHeightForWidth())
        self.basic_prompt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.basic_prompt.setFont(font)
        self.basic_prompt.setObjectName("basic_prompt")
        self.verticalLayout_2.addWidget(self.basic_prompt)
        self.label_10 = QtWidgets.QLabel(parent=self.basic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.basic_style = QtWidgets.QComboBox(parent=self.basic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basic_style.sizePolicy().hasHeightForWidth())
        self.basic_style.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.basic_style.setFont(font)
        self.basic_style.setObjectName("basic_style")
        self.verticalLayout_2.addWidget(self.basic_style)
        self.basic_randomize_checkbox = QtWidgets.QCheckBox(parent=self.basic)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.basic_randomize_checkbox.setFont(font)
        self.basic_randomize_checkbox.setObjectName("basic_randomize_checkbox")
        self.verticalLayout_2.addWidget(self.basic_randomize_checkbox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabs.addTab(self.basic, "")
        self.advanced = QtWidgets.QWidget()
        self.advanced.setObjectName("advanced")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.advanced)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.advanced_category = QtWidgets.QComboBox(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advanced_category.sizePolicy().hasHeightForWidth())
        self.advanced_category.setSizePolicy(sizePolicy)
        self.advanced_category.setMinimumSize(QtCore.QSize(80, 22))
        self.advanced_category.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.advanced_category.setFont(font)
        self.advanced_category.setObjectName("advanced_category")
        self.verticalLayout_8.addWidget(self.advanced_category)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.advanced_prompt = QtWidgets.QComboBox(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advanced_prompt.sizePolicy().hasHeightForWidth())
        self.advanced_prompt.setSizePolicy(sizePolicy)
        self.advanced_prompt.setMinimumSize(QtCore.QSize(80, 22))
        self.advanced_prompt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.advanced_prompt.setFont(font)
        self.advanced_prompt.setObjectName("advanced_prompt")
        self.verticalLayout_9.addWidget(self.advanced_prompt)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.advanced_style = QtWidgets.QComboBox(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advanced_style.sizePolicy().hasHeightForWidth())
        self.advanced_style.setSizePolicy(sizePolicy)
        self.advanced_style.setMinimumSize(QtCore.QSize(80, 22))
        self.advanced_style.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.advanced_style.setFont(font)
        self.advanced_style.setObjectName("advanced_style")
        self.verticalLayout_10.addWidget(self.advanced_style)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.reset_weights_button = QtWidgets.QPushButton(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_weights_button.sizePolicy().hasHeightForWidth())
        self.reset_weights_button.setSizePolicy(sizePolicy)
        self.reset_weights_button.setMinimumSize(QtCore.QSize(20, 0))
        self.reset_weights_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.reset_weights_button.setFont(font)
        self.reset_weights_button.setObjectName("reset_weights_button")
        self.horizontalLayout_4.addWidget(self.reset_weights_button)
        self.clear_values_button = QtWidgets.QPushButton(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_values_button.sizePolicy().hasHeightForWidth())
        self.clear_values_button.setSizePolicy(sizePolicy)
        self.clear_values_button.setMinimumSize(QtCore.QSize(20, 0))
        self.clear_values_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.clear_values_button.setFont(font)
        self.clear_values_button.setObjectName("clear_values_button")
        self.horizontalLayout_4.addWidget(self.clear_values_button)
        self.values_to_random_button = QtWidgets.QPushButton(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.values_to_random_button.sizePolicy().hasHeightForWidth())
        self.values_to_random_button.setSizePolicy(sizePolicy)
        self.values_to_random_button.setMinimumSize(QtCore.QSize(20, 0))
        self.values_to_random_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.values_to_random_button.setFont(font)
        self.values_to_random_button.setObjectName("values_to_random_button")
        self.horizontalLayout_4.addWidget(self.values_to_random_button)
        self.randomize_values_button = QtWidgets.QPushButton(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.randomize_values_button.sizePolicy().hasHeightForWidth())
        self.randomize_values_button.setSizePolicy(sizePolicy)
        self.randomize_values_button.setMinimumSize(QtCore.QSize(20, 0))
        self.randomize_values_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.randomize_values_button.setFont(font)
        self.randomize_values_button.setObjectName("randomize_values_button")
        self.horizontalLayout_4.addWidget(self.randomize_values_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.advanced)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(250, 120))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scroll_grid = QtWidgets.QWidget()
        self.scroll_grid.setGeometry(QtCore.QRect(0, 0, 406, 118))
        self.scroll_grid.setObjectName("scroll_grid")
        self.scrollArea.setWidget(self.scroll_grid)
        self.gridLayout_2.addWidget(self.scrollArea, 8, 0, 1, 2)
        self.tabs.addTab(self.advanced, "")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Text Prompt"))
        self.label_3.setText(_translate("Form", "Auto Prompt"))
        self.label_7.setText(_translate("Form", "Weight distribution"))
        self.text_prompt_weight_label.setText(_translate("Form", "0.50"))
        self.auto_prompt_weight_label.setText(_translate("Form", "0.50"))
        self.negative_auto_prompt_weight_label.setText(_translate("Form", "0.5"))
        self.label_6.setText(_translate("Form", "Negative Prompt"))
        self.negative_text_prompt_weight_label.setText(_translate("Form", "0.5"))
        self.label_5.setText(_translate("Form", "Auto Neg Prompt"))
        self.label_8.setText(_translate("Form", "Category"))
        self.label_9.setText(_translate("Form", "Prompt"))
        self.label_10.setText(_translate("Form", "Style"))
        self.basic_randomize_checkbox.setText(_translate("Form", "Randomize settings"))
        self.tabs.setTabText(self.tabs.indexOf(self.basic), _translate("Form", "Basic"))
        self.label_2.setText(_translate("Form", "Category"))
        self.label.setText(_translate("Form", "Prompt"))
        self.label_11.setText(_translate("Form", "Style"))
        self.reset_weights_button.setText(_translate("Form", "Reset Weights"))
        self.clear_values_button.setText(_translate("Form", "Clear Values"))
        self.values_to_random_button.setText(_translate("Form", "Values to Random"))
        self.randomize_values_button.setText(_translate("Form", "Randomize values"))
        self.tabs.setTabText(self.tabs.indexOf(self.advanced), _translate("Form", "Advanced"))
