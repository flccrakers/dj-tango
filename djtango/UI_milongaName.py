# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_milongaName.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogMilongaName(object):
    def setupUi(self, DialogMilongaName):
        DialogMilongaName.setObjectName(_fromUtf8("DialogMilongaName"))
        DialogMilongaName.resize(400, 108)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logo-djtango.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogMilongaName.setWindowIcon(icon)
        DialogMilongaName.setStyleSheet(_fromUtf8("QDialog{\n"
"    background-color: rgb(42,42,42)\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(DialogMilongaName)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DialogMilongaName)
        self.buttonBox.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.lineEditName = QtGui.QLineEdit(DialogMilongaName)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelMilongaName = QtGui.QLabel(DialogMilongaName)
        self.labelMilongaName.setObjectName(_fromUtf8("labelMilongaName"))
        self.gridLayout.addWidget(self.labelMilongaName, 0, 0, 1, 1)

        self.retranslateUi(DialogMilongaName)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogMilongaName.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogMilongaName.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMilongaName)

    def retranslateUi(self, DialogMilongaName):
        DialogMilongaName.setWindowTitle(_translate("DialogMilongaName", "Milonga Name", None))
        self.labelMilongaName.setText(_translate("DialogMilongaName", "Milonga Name", None))

