# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/status/templates/status.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_status_widget(object):
    def setupUi(self, status_widget):
        status_widget.setObjectName("status_widget")
        status_widget.resize(700, 44)
        status_widget.setStyleSheet("font-size: 12px")
        self.horizontalLayout = QtWidgets.QHBoxLayout(status_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.system_message = QtWidgets.QLabel(parent=status_widget)
        self.system_message.setObjectName("system_message")
        self.horizontalLayout.addWidget(self.system_message)
        self.line_5 = QtWidgets.QFrame(parent=status_widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.queue_stats = QtWidgets.QLabel(parent=status_widget)
        self.queue_stats.setObjectName("queue_stats")
        self.horizontalLayout.addWidget(self.queue_stats)
        self.nsfw_line = QtWidgets.QFrame(parent=status_widget)
        self.nsfw_line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.nsfw_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.nsfw_line.setObjectName("nsfw_line")
        self.horizontalLayout.addWidget(self.nsfw_line)
        self.nsfw_status = QtWidgets.QLabel(parent=status_widget)
        self.nsfw_status.setObjectName("nsfw_status")
        self.horizontalLayout.addWidget(self.nsfw_status)
        self.line_4 = QtWidgets.QFrame(parent=status_widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.cuda_status = QtWidgets.QLabel(parent=status_widget)
        self.cuda_status.setObjectName("cuda_status")
        self.horizontalLayout.addWidget(self.cuda_status)
        self.line = QtWidgets.QFrame(parent=status_widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.ram_stats = QtWidgets.QLabel(parent=status_widget)
        self.ram_stats.setObjectName("ram_stats")
        self.horizontalLayout.addWidget(self.ram_stats)
        self.line_3 = QtWidgets.QFrame(parent=status_widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.vram_stats = QtWidgets.QLabel(parent=status_widget)
        self.vram_stats.setObjectName("vram_stats")
        self.horizontalLayout.addWidget(self.vram_stats)

        self.retranslateUi(status_widget)
        QtCore.QMetaObject.connectSlotsByName(status_widget)

    def retranslateUi(self, status_widget):
        _translate = QtCore.QCoreApplication.translate
        status_widget.setWindowTitle(_translate("status_widget", "Form"))
        self.system_message.setText(_translate("status_widget", "system message"))
        self.queue_stats.setText(_translate("status_widget", "queue"))
        self.nsfw_status.setText(_translate("status_widget", "nsfw"))
        self.cuda_status.setText(_translate("status_widget", "gpu"))
        self.ram_stats.setText(_translate("status_widget", "ram"))
        self.vram_stats.setText(_translate("status_widget", "vram"))
