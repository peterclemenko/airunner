# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/widgets/export_preferences/templates/export_preferences.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_export_preferences(object):
    def setupUi(self, export_preferences):
        export_preferences.setObjectName("export_preferences")
        export_preferences.resize(457, 429)
        self.gridLayout_2 = QtWidgets.QGridLayout(export_preferences)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.actionAuto_export_images = QtWidgets.QCheckBox(parent=export_preferences)
        font = QtGui.QFont()
        font.setBold(True)
        self.actionAuto_export_images.setFont(font)
        self.actionAuto_export_images.setObjectName("actionAuto_export_images")
        self.gridLayout_2.addWidget(self.actionAuto_export_images, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=export_preferences)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=export_preferences)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=export_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.image_path = QtWidgets.QLineEdit(parent=export_preferences)
        self.image_path.setObjectName("image_path")
        self.gridLayout_2.addWidget(self.image_path, 4, 0, 1, 1)
        self.image_path_browse_button = QtWidgets.QPushButton(parent=export_preferences)
        self.image_path_browse_button.setObjectName("image_path_browse_button")
        self.gridLayout_2.addWidget(self.image_path_browse_button, 4, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(parent=export_preferences)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 5, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(parent=export_preferences)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=export_preferences)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 8, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=export_preferences)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.export_metadata = QtWidgets.QCheckBox(parent=export_preferences)
        self.export_metadata.setObjectName("export_metadata")
        self.gridLayout.addWidget(self.export_metadata, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=export_preferences)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.metadata_prompt = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_prompt.setObjectName("metadata_prompt")
        self.gridLayout.addWidget(self.metadata_prompt, 2, 0, 1, 1)
        self.metadata_samples = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_samples.setObjectName("metadata_samples")
        self.gridLayout.addWidget(self.metadata_samples, 2, 1, 1, 1)
        self.metadata_negative_prompt = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_negative_prompt.setObjectName("metadata_negative_prompt")
        self.gridLayout.addWidget(self.metadata_negative_prompt, 3, 0, 1, 1)
        self.metadata_model = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_model.setObjectName("metadata_model")
        self.gridLayout.addWidget(self.metadata_model, 3, 1, 1, 1)
        self.metadata_scale = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_scale.setObjectName("metadata_scale")
        self.gridLayout.addWidget(self.metadata_scale, 4, 0, 1, 1)
        self.metadata_model_branch = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_model_branch.setObjectName("metadata_model_branch")
        self.gridLayout.addWidget(self.metadata_model_branch, 4, 1, 1, 1)
        self.metadata_seed = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_seed.setObjectName("metadata_seed")
        self.gridLayout.addWidget(self.metadata_seed, 5, 0, 1, 1)
        self.metadata_scheduler = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_scheduler.setObjectName("metadata_scheduler")
        self.gridLayout.addWidget(self.metadata_scheduler, 5, 1, 1, 1)
        self.metadata_steps = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_steps.setObjectName("metadata_steps")
        self.gridLayout.addWidget(self.metadata_steps, 6, 0, 1, 1)
        self.metadata_ddim_eta = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_ddim_eta.setObjectName("metadata_ddim_eta")
        self.gridLayout.addWidget(self.metadata_ddim_eta, 6, 1, 1, 1)
        self.metadata_iterations = QtWidgets.QCheckBox(parent=export_preferences)
        self.metadata_iterations.setObjectName("metadata_iterations")
        self.gridLayout.addWidget(self.metadata_iterations, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 9, 0, 1, 2)
        self.image_type_dropdown = QtWidgets.QComboBox(parent=export_preferences)
        self.image_type_dropdown.setObjectName("image_type_dropdown")
        self.gridLayout_2.addWidget(self.image_type_dropdown, 7, 0, 1, 2)

        self.retranslateUi(export_preferences)
        self.actionAuto_export_images.toggled['bool'].connect(export_preferences.action_toggle_automatically_export_images) # type: ignore
        self.image_path.textEdited['QString'].connect(export_preferences.image_export_path_text_edited) # type: ignore
        self.image_path_browse_button.clicked.connect(export_preferences.action_clicked_button_browse) # type: ignore
        self.image_type_dropdown.currentTextChanged['QString'].connect(export_preferences.action_image_type_text_changed) # type: ignore
        self.export_metadata.toggled['bool'].connect(export_preferences.action_toggled_export_metadata) # type: ignore
        self.metadata_prompt.toggled['bool'].connect(export_preferences.action_toggled_prompt) # type: ignore
        self.metadata_negative_prompt.toggled['bool'].connect(export_preferences.action_toggled_negative_prompt) # type: ignore
        self.metadata_scale.toggled['bool'].connect(export_preferences.action_toggled_scale) # type: ignore
        self.metadata_seed.toggled['bool'].connect(export_preferences.action_toggled_seed) # type: ignore
        self.metadata_steps.toggled['bool'].connect(export_preferences.action_toggled_steps) # type: ignore
        self.metadata_iterations.toggled['bool'].connect(export_preferences.action_toggled_iterations) # type: ignore
        self.metadata_samples.toggled['bool'].connect(export_preferences.action_toggled_samples) # type: ignore
        self.metadata_model.toggled['bool'].connect(export_preferences.action_toggled_model) # type: ignore
        self.metadata_model_branch.toggled['bool'].connect(export_preferences.action_toggled_model_branch) # type: ignore
        self.metadata_scheduler.toggled['bool'].connect(export_preferences.action_toggled_scheduler) # type: ignore
        self.metadata_ddim_eta.toggled['bool'].connect(export_preferences.action_toggled_ddim) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(export_preferences)

    def retranslateUi(self, export_preferences):
        _translate = QtCore.QCoreApplication.translate
        export_preferences.setWindowTitle(_translate("export_preferences", "Form"))
        self.actionAuto_export_images.setText(_translate("export_preferences", "Automatically export images"))
        self.label.setText(_translate("export_preferences", "Image export folder"))
        self.label_2.setText(_translate("export_preferences", "Folder to auto export images to"))
        self.image_path_browse_button.setText(_translate("export_preferences", "Browse"))
        self.label_5.setText(_translate("export_preferences", "Image type"))
        self.label_3.setText(_translate("export_preferences", "Metadata"))
        self.export_metadata.setToolTip(_translate("export_preferences", "<html><head/><body><p>Export metadata along with images. </p><p>Only works with PNG files.</p></body></html>"))
        self.export_metadata.setText(_translate("export_preferences", "Export metadata"))
        self.label_4.setText(_translate("export_preferences", "Choose which metadata to include with exported images"))
        self.metadata_prompt.setText(_translate("export_preferences", "Prompt"))
        self.metadata_samples.setText(_translate("export_preferences", "Samples"))
        self.metadata_negative_prompt.setText(_translate("export_preferences", "Negative prompt"))
        self.metadata_model.setText(_translate("export_preferences", "Model"))
        self.metadata_scale.setText(_translate("export_preferences", "Scale"))
        self.metadata_model_branch.setText(_translate("export_preferences", "Model Branch"))
        self.metadata_seed.setText(_translate("export_preferences", "Seed"))
        self.metadata_scheduler.setText(_translate("export_preferences", "Scheduler"))
        self.metadata_steps.setText(_translate("export_preferences", "Steps"))
        self.metadata_ddim_eta.setText(_translate("export_preferences", "DDIM ETA"))
        self.metadata_iterations.setText(_translate("export_preferences", "Iterations"))
