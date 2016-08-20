# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_properties.ui'
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

class Ui_property(object):
    def setupUi(self, property):
        property.setObjectName(_fromUtf8("property"))
        property.setWindowModality(QtCore.Qt.ApplicationModal)
        property.resize(340, 365)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        property.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logo-djtango.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        property.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(property)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(property)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(property)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(property)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(property)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(property)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit = QtGui.QLineEdit(property)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(property)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(property)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.comboBox = QtGui.QComboBox(property)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.lineEdit_4 = QtGui.QLineEdit(property)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtGui.QFormLayout.LabelRole, spacerItem3)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previousPushButton = QtGui.QPushButton(property)
        self.previousPushButton.setObjectName(_fromUtf8("previousPushButton"))
        self.horizontalLayout.addWidget(self.previousPushButton)
        self.pushButton_3 = QtGui.QPushButton(property)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(property)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(property)
        QtCore.QMetaObject.connectSlotsByName(property)

    def retranslateUi(self, property):
        property.setWindowTitle(_translate("property", "Song Properties", None))
        self.label.setText(_translate("property", "TextLabel", None))
        self.label_2.setText(_translate("property", "TextLabel", None))
        self.label_3.setText(_translate("property", "TextLabel", None))
        self.label_4.setText(_translate("property", "TextLabel", None))
        self.label_5.setText(_translate("property", "TextLabel", None))
        self.previousPushButton.setText(_translate("property", "Previous", None))
        self.pushButton_3.setText(_translate("property", "Next", None))
        self.pushButton_2.setText(_translate("property", "Close", None))