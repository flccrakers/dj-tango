# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_askDelete.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAskDelete(object):
    def setupUi(self, DialogAskDelete):
        DialogAskDelete.setObjectName("DialogAsDelete")
        DialogAskDelete.resize(400, 108)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo-djtango.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAskDelete.setWindowIcon(icon)
        DialogAskDelete.setStyleSheet("QDialog{\n"
"    background-color: rgb(42,42,42)\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(DialogAskDelete)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogAskDelete)
        self.buttonBox.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        #self.lineEditName = QtWidgets.QLineEdit(DialogAskDelete)
        #self.lineEditName.setObjectName("lineEditName")
        #self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelMilongaName = QtWidgets.QLabel(DialogAskDelete)
        self.labelMilongaName.setObjectName("labelDeleteMilonga")
        self.labelMilongaName.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}")
        self.gridLayout.addWidget(self.labelMilongaName, 0, 0, 1, 1)

        self.retranslateUi(DialogAskDelete)
        self.buttonBox.accepted.connect(DialogAskDelete.accept)
        self.buttonBox.rejected.connect(DialogAskDelete.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAskDelete)

    def retranslateUi(self, DialogAskDelete):
        _translate = QtCore.QCoreApplication.translate
        DialogAskDelete.setWindowTitle(_translate("DialogAskDelete", "Delete a Milonga"))
        self.labelMilongaName.setText(_translate("DialogAskDelete", "Are you sure you want to delete this milonga ?"))

