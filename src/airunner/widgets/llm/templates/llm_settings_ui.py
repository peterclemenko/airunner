# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/llm/templates/llm_settings.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_llm_settings_widget(object):
    def setupUi(self, llm_settings_widget):
        llm_settings_widget.setObjectName("llm_settings_widget")
        llm_settings_widget.resize(1262, 1059)
        self.gridLayout = QtWidgets.QGridLayout(llm_settings_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=llm_settings_widget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.model = QtWidgets.QComboBox(parent=self.groupBox_7)
        self.model.setObjectName("model")
        self.gridLayout_10.addWidget(self.model, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=llm_settings_widget)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.model_version = QtWidgets.QComboBox(parent=self.groupBox_8)
        self.model_version.setObjectName("model_version")
        self.gridLayout_11.addWidget(self.model_version, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(parent=llm_settings_widget)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.prompt_template = QtWidgets.QComboBox(parent=self.groupBox_14)
        self.prompt_template.setObjectName("prompt_template")
        self.gridLayout_17.addWidget(self.prompt_template, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_14, 2, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=llm_settings_widget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radio_button_2bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_2bit.setObjectName("radio_button_2bit")
        self.horizontalLayout_3.addWidget(self.radio_button_2bit)
        self.radio_button_4bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_4bit.setObjectName("radio_button_4bit")
        self.horizontalLayout_3.addWidget(self.radio_button_4bit)
        self.radio_button_8bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_8bit.setObjectName("radio_button_8bit")
        self.horizontalLayout_3.addWidget(self.radio_button_8bit)
        self.radio_button_16bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_16bit.setObjectName("radio_button_16bit")
        self.horizontalLayout_3.addWidget(self.radio_button_16bit)
        self.radio_button_32bit = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radio_button_32bit.setObjectName("radio_button_32bit")
        self.horizontalLayout_3.addWidget(self.radio_button_32bit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.dtype_description = QtWidgets.QLabel(parent=self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dtype_description.setFont(font)
        self.dtype_description.setObjectName("dtype_description")
        self.gridLayout_9.addWidget(self.dtype_description, 2, 0, 1, 1)
        self.use_gpu_checkbox = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.use_gpu_checkbox.setObjectName("use_gpu_checkbox")
        self.gridLayout_9.addWidget(self.use_gpu_checkbox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 3, 0, 1, 1)
        self.override_parameters = QtWidgets.QGroupBox(parent=llm_settings_widget)
        self.override_parameters.setCheckable(True)
        self.override_parameters.setChecked(True)
        self.override_parameters.setObjectName("override_parameters")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.override_parameters)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton = QtWidgets.QPushButton(parent=self.override_parameters)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 14, 0, 1, 1)
        self.groupBox_19 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_19.setObjectName("groupBox_19")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_19)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.seed = QtWidgets.QLineEdit(parent=self.groupBox_19)
        self.seed.setObjectName("seed")
        self.horizontalLayout_4.addWidget(self.seed)
        self.random_seed = QtWidgets.QCheckBox(parent=self.groupBox_19)
        self.random_seed.setObjectName("random_seed")
        self.horizontalLayout_4.addWidget(self.random_seed)
        self.gridLayout_12.addWidget(self.groupBox_19, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.early_stopping = QtWidgets.QCheckBox(parent=self.override_parameters)
        self.early_stopping.setObjectName("early_stopping")
        self.horizontalLayout_6.addWidget(self.early_stopping)
        self.do_sample = QtWidgets.QCheckBox(parent=self.override_parameters)
        self.do_sample.setObjectName("do_sample")
        self.horizontalLayout_6.addWidget(self.do_sample)
        self.gridLayout_12.addLayout(self.horizontalLayout_6, 8, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_11 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.repetition_penalty = SliderWidget(parent=self.groupBox_11)
        self.repetition_penalty.setProperty("slider_minimum", 1)
        self.repetition_penalty.setProperty("slider_maximum", 10000)
        self.repetition_penalty.setProperty("spinbox_minimum", 0.01)
        self.repetition_penalty.setProperty("spinbox_maximum", 100.0)
        self.repetition_penalty.setProperty("display_as_float", True)
        self.repetition_penalty.setProperty("slider_single_step", 0)
        self.repetition_penalty.setProperty("slider_page_step", 1)
        self.repetition_penalty.setProperty("spinbox_single_step", 1.0)
        self.repetition_penalty.setProperty("spinbox_page_step", 10.0)
        self.repetition_penalty.setObjectName("repetition_penalty")
        self.gridLayout_19.addWidget(self.repetition_penalty, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_11)
        self.groupBox_16 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.min_length = SliderWidget(parent=self.groupBox_16)
        self.min_length.setProperty("slider_minimum", 1)
        self.min_length.setProperty("slider_maximum", 2556)
        self.min_length.setProperty("spinbox_minimum", 1.0)
        self.min_length.setProperty("spinbox_maximum", 2556.0)
        self.min_length.setProperty("display_as_float", False)
        self.min_length.setProperty("slider_single_step", 1)
        self.min_length.setProperty("slider_page_step", 2556)
        self.min_length.setProperty("spinbox_single_step", 1)
        self.min_length.setProperty("spinbox_page_step", 2556)
        self.min_length.setObjectName("min_length")
        self.gridLayout_20.addWidget(self.min_length, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_16)
        self.gridLayout_12.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_20 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.top_p = SliderWidget(parent=self.groupBox_20)
        self.top_p.setProperty("slider_minimum", 1)
        self.top_p.setProperty("slider_maximum", 100)
        self.top_p.setProperty("spinbox_minimum", 0.0)
        self.top_p.setProperty("spinbox_maximum", 1.0)
        self.top_p.setProperty("display_as_float", True)
        self.top_p.setProperty("slider_single_step", 1)
        self.top_p.setProperty("slider_page_step", 10)
        self.top_p.setProperty("spinbox_single_step", 0.01)
        self.top_p.setProperty("spinbox_page_step", 0.1)
        self.top_p.setObjectName("top_p")
        self.gridLayout_24.addWidget(self.top_p, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.groupBox_20)
        self.groupBox_21 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.max_length = SliderWidget(parent=self.groupBox_21)
        self.max_length.setProperty("slider_minimum", 1)
        self.max_length.setProperty("slider_maximum", 2556)
        self.max_length.setProperty("spinbox_minimum", 1.0)
        self.max_length.setProperty("spinbox_maximum", 2556.0)
        self.max_length.setProperty("display_as_float", False)
        self.max_length.setProperty("slider_single_step", 1)
        self.max_length.setProperty("slider_page_step", 2556)
        self.max_length.setProperty("spinbox_single_step", 1)
        self.max_length.setProperty("spinbox_page_step", 2556)
        self.max_length.setObjectName("max_length")
        self.gridLayout_25.addWidget(self.max_length, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.groupBox_21)
        self.gridLayout_12.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.leave_in_vram = QtWidgets.QRadioButton(parent=self.override_parameters)
        self.leave_in_vram.setObjectName("leave_in_vram")
        self.horizontalLayout_12.addWidget(self.leave_in_vram)
        self.move_to_cpu = QtWidgets.QRadioButton(parent=self.override_parameters)
        self.move_to_cpu.setObjectName("move_to_cpu")
        self.horizontalLayout_12.addWidget(self.move_to_cpu)
        self.unload_model = QtWidgets.QRadioButton(parent=self.override_parameters)
        self.unload_model.setObjectName("unload_model")
        self.horizontalLayout_12.addWidget(self.unload_model)
        self.gridLayout_12.addLayout(self.horizontalLayout_12, 12, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.override_parameters)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_12.addWidget(self.label_3, 10, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_17 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.ngram_size = SliderWidget(parent=self.groupBox_17)
        self.ngram_size.setProperty("slider_minimum", 0)
        self.ngram_size.setProperty("slider_maximum", 20)
        self.ngram_size.setProperty("spinbox_minimum", 0.0)
        self.ngram_size.setProperty("spinbox_maximum", 20.0)
        self.ngram_size.setProperty("display_as_float", False)
        self.ngram_size.setProperty("slider_single_step", 1)
        self.ngram_size.setProperty("slider_page_step", 1)
        self.ngram_size.setProperty("spinbox_single_step", 1.0)
        self.ngram_size.setProperty("spinbox_page_step", 1.0)
        self.ngram_size.setObjectName("ngram_size")
        self.gridLayout_21.addWidget(self.ngram_size, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_17)
        self.groupBox_18 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.temperature = SliderWidget(parent=self.groupBox_18)
        self.temperature.setProperty("slider_minimum", 1)
        self.temperature.setProperty("slider_maximum", 20000)
        self.temperature.setProperty("spinbox_minimum", 0.0001)
        self.temperature.setProperty("spinbox_maximum", 2.0)
        self.temperature.setProperty("display_as_float", True)
        self.temperature.setProperty("slider_single_step", 1)
        self.temperature.setProperty("slider_page_step", 10)
        self.temperature.setProperty("spinbox_single_step", 0.01)
        self.temperature.setProperty("spinbox_page_step", 0.1)
        self.temperature.setObjectName("temperature")
        self.gridLayout_22.addWidget(self.temperature, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_18)
        self.gridLayout_12.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_24 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_24.setObjectName("groupBox_24")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.groupBox_24)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.length_penalty = SliderWidget(parent=self.groupBox_24)
        self.length_penalty.setProperty("slider_minimum", -100)
        self.length_penalty.setProperty("slider_maximum", 100)
        self.length_penalty.setProperty("spinbox_minimum", 0.0)
        self.length_penalty.setProperty("spinbox_maximum", 1.0)
        self.length_penalty.setProperty("display_as_float", True)
        self.length_penalty.setProperty("slider_single_step", 1)
        self.length_penalty.setProperty("slider_page_step", 10)
        self.length_penalty.setProperty("spinbox_single_step", 0.01)
        self.length_penalty.setProperty("spinbox_page_step", 0.1)
        self.length_penalty.setObjectName("length_penalty")
        self.gridLayout_28.addWidget(self.length_penalty, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.groupBox_24)
        self.groupBox_25 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_25.setObjectName("groupBox_25")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.groupBox_25)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.num_beams = SliderWidget(parent=self.groupBox_25)
        self.num_beams.setProperty("slider_minimum", 1)
        self.num_beams.setProperty("slider_maximum", 100)
        self.num_beams.setProperty("spinbox_minimum", 0.0)
        self.num_beams.setProperty("spinbox_maximum", 100.0)
        self.num_beams.setProperty("display_as_float", False)
        self.num_beams.setProperty("slider_single_step", 1)
        self.num_beams.setProperty("slider_page_step", 10)
        self.num_beams.setProperty("spinbox_single_step", 0.01)
        self.num_beams.setProperty("spinbox_page_step", 0.1)
        self.num_beams.setObjectName("num_beams")
        self.gridLayout_29.addWidget(self.num_beams, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.groupBox_25)
        self.gridLayout_12.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.override_parameters)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_12.addWidget(self.line, 9, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBox_22 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.sequences = SliderWidget(parent=self.groupBox_22)
        self.sequences.setProperty("slider_minimum", 1)
        self.sequences.setProperty("slider_maximum", 100)
        self.sequences.setProperty("spinbox_minimum", 0.0)
        self.sequences.setProperty("spinbox_maximum", 100.0)
        self.sequences.setProperty("display_as_float", False)
        self.sequences.setProperty("slider_single_step", 1)
        self.sequences.setProperty("slider_page_step", 10)
        self.sequences.setProperty("spinbox_single_step", 0.01)
        self.sequences.setProperty("spinbox_page_step", 0.1)
        self.sequences.setObjectName("sequences")
        self.gridLayout_26.addWidget(self.sequences, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.groupBox_22)
        self.groupBox_23 = QtWidgets.QGroupBox(parent=self.override_parameters)
        self.groupBox_23.setObjectName("groupBox_23")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.groupBox_23)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.top_k = SliderWidget(parent=self.groupBox_23)
        self.top_k.setProperty("slider_minimum", 0)
        self.top_k.setProperty("slider_maximum", 256)
        self.top_k.setProperty("spinbox_minimum", 0.0)
        self.top_k.setProperty("spinbox_maximum", 256.0)
        self.top_k.setProperty("display_as_float", False)
        self.top_k.setProperty("slider_single_step", 1)
        self.top_k.setProperty("slider_page_step", 10)
        self.top_k.setProperty("spinbox_single_step", 1)
        self.top_k.setProperty("spinbox_page_step", 10)
        self.top_k.setObjectName("top_k")
        self.gridLayout_27.addWidget(self.top_k, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.groupBox_23)
        self.gridLayout_12.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.override_parameters)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_12.addWidget(self.label_4, 11, 0, 1, 1)
        self.gridLayout.addWidget(self.override_parameters, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)

        self.retranslateUi(llm_settings_widget)
        self.model_version.setCurrentIndex(-1)
        self.radio_button_2bit.toggled['bool'].connect(llm_settings_widget.toggled_2bit) # type: ignore
        self.radio_button_16bit.toggled['bool'].connect(llm_settings_widget.toggled_16bit) # type: ignore
        self.use_gpu_checkbox.toggled['bool'].connect(llm_settings_widget.use_gpu_toggled) # type: ignore
        self.radio_button_4bit.toggled['bool'].connect(llm_settings_widget.toggled_4bit) # type: ignore
        self.radio_button_8bit.toggled['bool'].connect(llm_settings_widget.toggled_8bit) # type: ignore
        self.radio_button_32bit.toggled['bool'].connect(llm_settings_widget.toggled_32bit) # type: ignore
        self.override_parameters.toggled['bool'].connect(llm_settings_widget.override_parameters_toggled) # type: ignore
        self.seed.textEdited['QString'].connect(llm_settings_widget.seed_changed) # type: ignore
        self.early_stopping.toggled['bool'].connect(llm_settings_widget.early_stopping_toggled) # type: ignore
        self.random_seed.toggled['bool'].connect(llm_settings_widget.random_seed_toggled) # type: ignore
        self.pushButton.clicked.connect(llm_settings_widget.reset_settings_to_default_clicked) # type: ignore
        self.move_to_cpu.toggled['bool'].connect(llm_settings_widget.toggle_move_model_to_cpu) # type: ignore
        self.do_sample.toggled['bool'].connect(llm_settings_widget.do_sample_toggled) # type: ignore
        self.leave_in_vram.toggled['bool'].connect(llm_settings_widget.toggle_leave_model_in_vram) # type: ignore
        self.unload_model.toggled['bool'].connect(llm_settings_widget.toggle_unload_model) # type: ignore
        self.prompt_template.currentTextChanged['QString'].connect(llm_settings_widget.prompt_template_text_changed) # type: ignore
        self.model.currentTextChanged['QString'].connect(llm_settings_widget.model_text_changed) # type: ignore
        self.model_version.currentTextChanged['QString'].connect(llm_settings_widget.model_version_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(llm_settings_widget)
        llm_settings_widget.setTabOrder(self.model, self.model_version)
        llm_settings_widget.setTabOrder(self.model_version, self.use_gpu_checkbox)
        llm_settings_widget.setTabOrder(self.use_gpu_checkbox, self.radio_button_4bit)
        llm_settings_widget.setTabOrder(self.radio_button_4bit, self.radio_button_8bit)
        llm_settings_widget.setTabOrder(self.radio_button_8bit, self.radio_button_16bit)
        llm_settings_widget.setTabOrder(self.radio_button_16bit, self.radio_button_32bit)
        llm_settings_widget.setTabOrder(self.radio_button_32bit, self.seed)
        llm_settings_widget.setTabOrder(self.seed, self.random_seed)

    def retranslateUi(self, llm_settings_widget):
        _translate = QtCore.QCoreApplication.translate
        llm_settings_widget.setWindowTitle(_translate("llm_settings_widget", "Form"))
        self.groupBox_7.setTitle(_translate("llm_settings_widget", "Model Type"))
        self.groupBox_8.setTitle(_translate("llm_settings_widget", "Model Version"))
        self.groupBox_14.setTitle(_translate("llm_settings_widget", "Prompt Template"))
        self.groupBox_6.setTitle(_translate("llm_settings_widget", "DType"))
        self.radio_button_2bit.setText(_translate("llm_settings_widget", "2-bit"))
        self.radio_button_4bit.setText(_translate("llm_settings_widget", "4-bit"))
        self.radio_button_8bit.setText(_translate("llm_settings_widget", "8-bit"))
        self.radio_button_16bit.setText(_translate("llm_settings_widget", "16-bit"))
        self.radio_button_32bit.setText(_translate("llm_settings_widget", "32-bit"))
        self.dtype_description.setText(_translate("llm_settings_widget", "Description"))
        self.use_gpu_checkbox.setText(_translate("llm_settings_widget", "Use GPU"))
        self.override_parameters.setTitle(_translate("llm_settings_widget", "Override Prameters"))
        self.pushButton.setText(_translate("llm_settings_widget", "Reset Settings to Default"))
        self.groupBox_19.setTitle(_translate("llm_settings_widget", "Seed"))
        self.random_seed.setText(_translate("llm_settings_widget", "Random seed"))
        self.early_stopping.setText(_translate("llm_settings_widget", "Early stopping"))
        self.do_sample.setText(_translate("llm_settings_widget", "Do sample"))
        self.groupBox_11.setTitle(_translate("llm_settings_widget", "Repetition penalty"))
        self.repetition_penalty.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.repetition_penalty"))
        self.repetition_penalty.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_16.setTitle(_translate("llm_settings_widget", "Min length"))
        self.min_length.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.min_length"))
        self.min_length.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_20.setTitle(_translate("llm_settings_widget", "Top P"))
        self.top_p.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.top_p"))
        self.top_p.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_21.setTitle(_translate("llm_settings_widget", "Max length"))
        self.max_length.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.max_length"))
        self.max_length.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.leave_in_vram.setText(_translate("llm_settings_widget", "Leave in VRAM"))
        self.move_to_cpu.setText(_translate("llm_settings_widget", "Move to CPU"))
        self.unload_model.setText(_translate("llm_settings_widget", "Unload model"))
        self.label_3.setText(_translate("llm_settings_widget", "Model management"))
        self.groupBox_17.setTitle(_translate("llm_settings_widget", "No repeat ngram size"))
        self.ngram_size.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.ngram_size"))
        self.ngram_size.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_18.setTitle(_translate("llm_settings_widget", "Temperature"))
        self.temperature.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.temperature"))
        self.temperature.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_24.setTitle(_translate("llm_settings_widget", "Length penalty"))
        self.length_penalty.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.length_penalty"))
        self.length_penalty.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_25.setTitle(_translate("llm_settings_widget", "Num beams"))
        self.num_beams.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.num_beams"))
        self.num_beams.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_22.setTitle(_translate("llm_settings_widget", "Sequences to generate"))
        self.sequences.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.sequences"))
        self.sequences.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.groupBox_23.setTitle(_translate("llm_settings_widget", "Top k"))
        self.top_k.setProperty("settings_property", _translate("llm_settings_widget", "llm_generator.top_k"))
        self.top_k.setProperty("slider_callback", _translate("llm_settings_widget", "handle_value_change"))
        self.label_4.setText(_translate("llm_settings_widget", "How to treat model when not in use"))
from airunner.widgets.slider.slider_widget import SliderWidget
