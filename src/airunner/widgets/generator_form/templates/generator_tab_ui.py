# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/generator_form/templates/generator_tab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_generator_tab(object):
    def setupUi(self, generator_tab):
        generator_tab.setObjectName("generator_tab")
        generator_tab.resize(330, 972)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(generator_tab.sizePolicy().hasHeightForWidth())
        generator_tab.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(generator_tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.generator_tabs = QtWidgets.QTabWidget(parent=generator_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generator_tabs.sizePolicy().hasHeightForWidth())
        self.generator_tabs.setSizePolicy(sizePolicy)
        self.generator_tabs.setObjectName("generator_tabs")
        self.tab_stablediffusion = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion.setSizePolicy(sizePolicy)
        self.tab_stablediffusion.setObjectName("tab_stablediffusion")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_stablediffusion)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_widget_stablediffusion = QtWidgets.QTabWidget(parent=self.tab_stablediffusion)
        self.tab_widget_stablediffusion.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tab_widget_stablediffusion.setObjectName("tab_widget_stablediffusion")
        self.tab_stablediffusion_txt2img = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion_txt2img.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion_txt2img.setSizePolicy(sizePolicy)
        self.tab_stablediffusion_txt2img.setObjectName("tab_stablediffusion_txt2img")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_stablediffusion_txt2img)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.generator_form_stablediffusion_txt2img = GeneratorForm(parent=self.tab_stablediffusion_txt2img)
        self.generator_form_stablediffusion_txt2img.setObjectName("generator_form_stablediffusion_txt2img")
        self.gridLayout_7.addWidget(self.generator_form_stablediffusion_txt2img, 0, 0, 1, 1)
        self.tab_widget_stablediffusion.addTab(self.tab_stablediffusion_txt2img, "")
        self.tab_stablediffusion_outpaint = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion_outpaint.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion_outpaint.setSizePolicy(sizePolicy)
        self.tab_stablediffusion_outpaint.setObjectName("tab_stablediffusion_outpaint")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_stablediffusion_outpaint)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.generator_form_stablediffusion_outpaint = GeneratorForm(parent=self.tab_stablediffusion_outpaint)
        self.generator_form_stablediffusion_outpaint.setObjectName("generator_form_stablediffusion_outpaint")
        self.gridLayout_10.addWidget(self.generator_form_stablediffusion_outpaint, 0, 0, 1, 1)
        self.tab_widget_stablediffusion.addTab(self.tab_stablediffusion_outpaint, "")
        self.tab_stablediffusion_depth2img = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion_depth2img.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion_depth2img.setSizePolicy(sizePolicy)
        self.tab_stablediffusion_depth2img.setObjectName("tab_stablediffusion_depth2img")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_stablediffusion_depth2img)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.generator_form_stablediffusion_depth2img = GeneratorForm(parent=self.tab_stablediffusion_depth2img)
        self.generator_form_stablediffusion_depth2img.setObjectName("generator_form_stablediffusion_depth2img")
        self.gridLayout_11.addWidget(self.generator_form_stablediffusion_depth2img, 0, 0, 1, 1)
        self.tab_widget_stablediffusion.addTab(self.tab_stablediffusion_depth2img, "")
        self.tab_stablediffusion_pix2pix = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion_pix2pix.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion_pix2pix.setSizePolicy(sizePolicy)
        self.tab_stablediffusion_pix2pix.setObjectName("tab_stablediffusion_pix2pix")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_stablediffusion_pix2pix)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.generator_form_stablediffusion_pix2pix = GeneratorForm(parent=self.tab_stablediffusion_pix2pix)
        self.generator_form_stablediffusion_pix2pix.setObjectName("generator_form_stablediffusion_pix2pix")
        self.gridLayout_12.addWidget(self.generator_form_stablediffusion_pix2pix, 0, 0, 1, 1)
        self.tab_widget_stablediffusion.addTab(self.tab_stablediffusion_pix2pix, "")
        self.tab_stablediffusion_upscale = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion_upscale.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion_upscale.setSizePolicy(sizePolicy)
        self.tab_stablediffusion_upscale.setObjectName("tab_stablediffusion_upscale")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_stablediffusion_upscale)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.generator_form_stablediffusion_upscale = GeneratorForm(parent=self.tab_stablediffusion_upscale)
        self.generator_form_stablediffusion_upscale.setObjectName("generator_form_stablediffusion_upscale")
        self.gridLayout_5.addWidget(self.generator_form_stablediffusion_upscale, 0, 0, 1, 1)
        self.tab_widget_stablediffusion.addTab(self.tab_stablediffusion_upscale, "")
        self.tab_stablediffusion_superresolution = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion_superresolution.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion_superresolution.setSizePolicy(sizePolicy)
        self.tab_stablediffusion_superresolution.setObjectName("tab_stablediffusion_superresolution")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_stablediffusion_superresolution)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.generator_form_stablediffusion_superresolution = GeneratorForm(parent=self.tab_stablediffusion_superresolution)
        self.generator_form_stablediffusion_superresolution.setObjectName("generator_form_stablediffusion_superresolution")
        self.gridLayout_6.addWidget(self.generator_form_stablediffusion_superresolution, 0, 0, 1, 1)
        self.tab_widget_stablediffusion.addTab(self.tab_stablediffusion_superresolution, "")
        self.tab_stablediffusion_txt2vid = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_stablediffusion_txt2vid.sizePolicy().hasHeightForWidth())
        self.tab_stablediffusion_txt2vid.setSizePolicy(sizePolicy)
        self.tab_stablediffusion_txt2vid.setObjectName("tab_stablediffusion_txt2vid")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_stablediffusion_txt2vid)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.generator_form_txt2vid = GeneratorForm(parent=self.tab_stablediffusion_txt2vid)
        self.generator_form_txt2vid.setObjectName("generator_form_txt2vid")
        self.gridLayout_13.addWidget(self.generator_form_txt2vid, 0, 0, 1, 1)
        self.tab_widget_stablediffusion.addTab(self.tab_stablediffusion_txt2vid, "")
        self.gridLayout.addWidget(self.tab_widget_stablediffusion, 0, 0, 1, 1)
        self.generator_tabs.addTab(self.tab_stablediffusion, "")
        self.tab_kandinsky = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_kandinsky.sizePolicy().hasHeightForWidth())
        self.tab_kandinsky.setSizePolicy(sizePolicy)
        self.tab_kandinsky.setObjectName("tab_kandinsky")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_kandinsky)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tab_widget_kandinsky = QtWidgets.QTabWidget(parent=self.tab_kandinsky)
        self.tab_widget_kandinsky.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tab_widget_kandinsky.setObjectName("tab_widget_kandinsky")
        self.tab_kandinsky_txt2img = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_kandinsky_txt2img.sizePolicy().hasHeightForWidth())
        self.tab_kandinsky_txt2img.setSizePolicy(sizePolicy)
        self.tab_kandinsky_txt2img.setObjectName("tab_kandinsky_txt2img")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_kandinsky_txt2img)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.generator_form_kandinsky_txt2img = GeneratorForm(parent=self.tab_kandinsky_txt2img)
        self.generator_form_kandinsky_txt2img.setObjectName("generator_form_kandinsky_txt2img")
        self.gridLayout_8.addWidget(self.generator_form_kandinsky_txt2img, 0, 0, 1, 1)
        self.tab_widget_kandinsky.addTab(self.tab_kandinsky_txt2img, "")
        self.tab_kandinsky_outpaint = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_kandinsky_outpaint.sizePolicy().hasHeightForWidth())
        self.tab_kandinsky_outpaint.setSizePolicy(sizePolicy)
        self.tab_kandinsky_outpaint.setObjectName("tab_kandinsky_outpaint")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_kandinsky_outpaint)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.generator_form_kandinsky_outpaint = GeneratorForm(parent=self.tab_kandinsky_outpaint)
        self.generator_form_kandinsky_outpaint.setObjectName("generator_form_kandinsky_outpaint")
        self.gridLayout_14.addWidget(self.generator_form_kandinsky_outpaint, 0, 0, 1, 1)
        self.tab_widget_kandinsky.addTab(self.tab_kandinsky_outpaint, "")
        self.gridLayout_3.addWidget(self.tab_widget_kandinsky, 0, 0, 1, 1)
        self.generator_tabs.addTab(self.tab_kandinsky, "")
        self.tab_shape = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_shape.sizePolicy().hasHeightForWidth())
        self.tab_shape.setSizePolicy(sizePolicy)
        self.tab_shape.setObjectName("tab_shape")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_shape)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tab_widget_shape = QtWidgets.QTabWidget(parent=self.tab_shape)
        self.tab_widget_shape.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tab_widget_shape.setObjectName("tab_widget_shape")
        self.tab_shape_txt2img = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_shape_txt2img.sizePolicy().hasHeightForWidth())
        self.tab_shape_txt2img.setSizePolicy(sizePolicy)
        self.tab_shape_txt2img.setObjectName("tab_shape_txt2img")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_shape_txt2img)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.generator_form_shape_txt2img = GeneratorForm(parent=self.tab_shape_txt2img)
        self.generator_form_shape_txt2img.setObjectName("generator_form_shape_txt2img")
        self.gridLayout_9.addWidget(self.generator_form_shape_txt2img, 0, 0, 1, 1)
        self.tab_widget_shape.addTab(self.tab_shape_txt2img, "")
        self.gridLayout_4.addWidget(self.tab_widget_shape, 0, 0, 1, 1)
        self.generator_tabs.addTab(self.tab_shape, "")
        self.gridLayout_2.addWidget(self.generator_tabs, 0, 0, 1, 1)

        self.retranslateUi(generator_tab)
        self.generator_tabs.setCurrentIndex(0)
        self.tab_widget_stablediffusion.setCurrentIndex(2)
        self.tab_widget_kandinsky.setCurrentIndex(1)
        self.tab_widget_shape.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(generator_tab)

    def retranslateUi(self, generator_tab):
        _translate = QtCore.QCoreApplication.translate
        generator_tab.setWindowTitle(_translate("generator_tab", "Form"))
        self.tab_stablediffusion_txt2img.setProperty("generator_section", _translate("generator_tab", "txt2img"))
        self.tab_stablediffusion_txt2img.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.generator_form_stablediffusion_txt2img.setProperty("generator_section", _translate("generator_tab", "txt2img"))
        self.generator_form_stablediffusion_txt2img.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.tab_widget_stablediffusion.setTabText(self.tab_widget_stablediffusion.indexOf(self.tab_stablediffusion_txt2img), _translate("generator_tab", "txt2img / img2img"))
        self.tab_stablediffusion_outpaint.setProperty("generator_section", _translate("generator_tab", "outpaint"))
        self.tab_stablediffusion_outpaint.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.generator_form_stablediffusion_outpaint.setProperty("generator_section", _translate("generator_tab", "outpaint"))
        self.generator_form_stablediffusion_outpaint.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.tab_widget_stablediffusion.setTabText(self.tab_widget_stablediffusion.indexOf(self.tab_stablediffusion_outpaint), _translate("generator_tab", "inpaint / outapint"))
        self.tab_stablediffusion_depth2img.setProperty("generator_section", _translate("generator_tab", "depth2img"))
        self.tab_stablediffusion_depth2img.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.generator_form_stablediffusion_depth2img.setProperty("generator_section", _translate("generator_tab", "depth2img"))
        self.generator_form_stablediffusion_depth2img.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.tab_widget_stablediffusion.setTabText(self.tab_widget_stablediffusion.indexOf(self.tab_stablediffusion_depth2img), _translate("generator_tab", "depth2img"))
        self.tab_stablediffusion_pix2pix.setProperty("generator_section", _translate("generator_tab", "pix2pix"))
        self.tab_stablediffusion_pix2pix.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.generator_form_stablediffusion_pix2pix.setProperty("generator_section", _translate("generator_tab", "pix2pix"))
        self.generator_form_stablediffusion_pix2pix.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.tab_widget_stablediffusion.setTabText(self.tab_widget_stablediffusion.indexOf(self.tab_stablediffusion_pix2pix), _translate("generator_tab", "pix2pix"))
        self.tab_stablediffusion_upscale.setProperty("generator_section", _translate("generator_tab", "upscale"))
        self.tab_stablediffusion_upscale.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.generator_form_stablediffusion_upscale.setProperty("generator_section", _translate("generator_tab", "upscale"))
        self.generator_form_stablediffusion_upscale.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.tab_widget_stablediffusion.setTabText(self.tab_widget_stablediffusion.indexOf(self.tab_stablediffusion_upscale), _translate("generator_tab", "upscale"))
        self.tab_stablediffusion_superresolution.setProperty("generator_section", _translate("generator_tab", "superresolution"))
        self.tab_stablediffusion_superresolution.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.generator_form_stablediffusion_superresolution.setProperty("generator_section", _translate("generator_tab", "superresolution"))
        self.generator_form_stablediffusion_superresolution.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.tab_widget_stablediffusion.setTabText(self.tab_widget_stablediffusion.indexOf(self.tab_stablediffusion_superresolution), _translate("generator_tab", "superresolution"))
        self.tab_stablediffusion_txt2vid.setProperty("generator_section", _translate("generator_tab", "txt2vid"))
        self.tab_stablediffusion_txt2vid.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.generator_form_txt2vid.setProperty("generator_section", _translate("generator_tab", "txt2vid"))
        self.generator_form_txt2vid.setProperty("generator_name", _translate("generator_tab", "stablediffusion"))
        self.tab_widget_stablediffusion.setTabText(self.tab_widget_stablediffusion.indexOf(self.tab_stablediffusion_txt2vid), _translate("generator_tab", "txt2vid"))
        self.generator_tabs.setTabText(self.generator_tabs.indexOf(self.tab_stablediffusion), _translate("generator_tab", "Stable Diffusion"))
        self.tab_kandinsky_txt2img.setProperty("generator_section", _translate("generator_tab", "txt2img"))
        self.tab_kandinsky_txt2img.setProperty("generator_name", _translate("generator_tab", "kandinsky"))
        self.generator_form_kandinsky_txt2img.setProperty("generator_section", _translate("generator_tab", "txt2img"))
        self.generator_form_kandinsky_txt2img.setProperty("generator_name", _translate("generator_tab", "kandinsky"))
        self.tab_widget_kandinsky.setTabText(self.tab_widget_kandinsky.indexOf(self.tab_kandinsky_txt2img), _translate("generator_tab", "txt2img/img2img"))
        self.tab_kandinsky_outpaint.setProperty("generator_section", _translate("generator_tab", "outpaint"))
        self.tab_kandinsky_outpaint.setProperty("generator_name", _translate("generator_tab", "kandinsky"))
        self.generator_form_kandinsky_outpaint.setProperty("generator_section", _translate("generator_tab", "outpaint"))
        self.generator_form_kandinsky_outpaint.setProperty("generator_name", _translate("generator_tab", "kandinsky"))
        self.tab_widget_kandinsky.setTabText(self.tab_widget_kandinsky.indexOf(self.tab_kandinsky_outpaint), _translate("generator_tab", "inpaint / outapint"))
        self.generator_tabs.setTabText(self.generator_tabs.indexOf(self.tab_kandinsky), _translate("generator_tab", "Kandinsky"))
        self.tab_shape_txt2img.setProperty("generator_section", _translate("generator_tab", "txt2img"))
        self.tab_shape_txt2img.setProperty("generator_name", _translate("generator_tab", "shape"))
        self.generator_form_shape_txt2img.setProperty("generator_section", _translate("generator_tab", "txt2img"))
        self.generator_form_shape_txt2img.setProperty("generator_name", _translate("generator_tab", "shape"))
        self.tab_widget_shape.setTabText(self.tab_widget_shape.indexOf(self.tab_shape_txt2img), _translate("generator_tab", "txt2img/img2img"))
        self.generator_tabs.setTabText(self.generator_tabs.indexOf(self.tab_shape), _translate("generator_tab", "Shap-e"))
from airunner.widgets.generator_form.generator_form_widget import GeneratorForm
