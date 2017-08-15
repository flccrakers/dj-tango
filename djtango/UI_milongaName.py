# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_milongaName.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogMilongaName(object):
    def setupUi(self, DialogMilongaName):
        DialogMilongaName.setObjectName("DialogMilongaName")
        DialogMilongaName.resize(400, 108)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo-djtango.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogMilongaName.setWindowIcon(icon)
        DialogMilongaName.setStyleSheet("QDialog{\n"
"    background-color: rgb(42,42,42)\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(DialogMilongaName)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogMilongaName)
        self.buttonBox.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(DialogMilongaName)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelMilongaName = QtWidgets.QLabel(DialogMilongaName)
        self.labelMilongaName.setObjectName("labelMilongaName")
        self.gridLayout.addWidget(self.labelMilongaName, 0, 0, 1, 1)

        self.retranslateUi(DialogMilongaName)
        self.buttonBox.accepted.connect(DialogMilongaName.accept)
        self.buttonBox.rejected.connect(DialogMilongaName.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMilongaName)

    def retranslateUi(self, DialogMilongaName):
        _translate = QtCore.QCoreApplication.translate
        DialogMilongaName.setWindowTitle(_translate("DialogMilongaName", "Milonga Name"))
        self.labelMilongaName.setText(_translate("DialogMilongaName", "Milonga Name"))

