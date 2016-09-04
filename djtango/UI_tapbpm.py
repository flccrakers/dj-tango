# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_tapbpm.ui'
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

class Ui_tapDialog(object):
    def setupUi(self, tapDialog):
        tapDialog.setObjectName(_fromUtf8("tapDialog"))
        tapDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        tapDialog.resize(531, 229)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
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
        tapDialog.setPalette(palette)
        tapDialog.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(tapDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(tapDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"    background-color: rgb(42,42,42)\n"
"}"))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.labelTypeBmp = QtGui.QLabel(tapDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTypeBmp.sizePolicy().hasHeightForWidth())
        self.labelTypeBmp.setSizePolicy(sizePolicy)
        self.labelTypeBmp.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelTypeBmp.setObjectName(_fromUtf8("labelTypeBmp"))
        self.verticalLayout_2.addWidget(self.labelTypeBmp)
        self.labelDone = QtGui.QLabel(tapDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDone.sizePolicy().hasHeightForWidth())
        self.labelDone.setSizePolicy(sizePolicy)
        self.labelDone.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelDone.setObjectName(_fromUtf8("labelDone"))
        self.verticalLayout_2.addWidget(self.labelDone)
        spacerItem1 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.lcdNumber = QtGui.QLCDNumber(tapDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(390, 0))
        self.lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(160,52,77);\n"
"    background-color: rgb(42,42,42);\n"
"}"))
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setNumDigits(5)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tapButton = QtGui.QPushButton(tapDialog)
        self.tapButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tapButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.tapButton.setDefault(False)
        self.tapButton.setFlat(False)
        self.tapButton.setObjectName(_fromUtf8("tapButton"))
        self.verticalLayout.addWidget(self.tapButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previous = QtGui.QPushButton(tapDialog)
        self.previous.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previous.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.previous.setObjectName(_fromUtf8("previous"))
        self.horizontalLayout.addWidget(self.previous)
        self.next = QtGui.QPushButton(tapDialog)
        self.next.setFocusPolicy(QtCore.Qt.NoFocus)
        self.next.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout.addWidget(self.next)
        self.cancel = QtGui.QPushButton(tapDialog)
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)
        self.validate = QtGui.QPushButton(tapDialog)
        self.validate.setFocusPolicy(QtCore.Qt.NoFocus)
        self.validate.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.validate.setObjectName(_fromUtf8("validate"))
        self.horizontalLayout.addWidget(self.validate)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(tapDialog)
        QtCore.QMetaObject.connectSlotsByName(tapDialog)

    def retranslateUi(self, tapDialog):
        tapDialog.setWindowTitle(_translate("tapDialog", "Taping the tempo", None))
        self.label.setText(_translate("tapDialog", "Tap on space key while the music is playing, when finish tap on enter to save the calculated bpm. Click enter when finished", None))
        self.labelTypeBmp.setText(_translate("tapDialog", "By Human", None))
        self.labelDone.setText(_translate("tapDialog", "DONE", None))
        self.tapButton.setText(_translate("tapDialog", "Tap (hit space)", None))
        self.tapButton.setShortcut(_translate("tapDialog", "Space", None))
        self.previous.setToolTip(_translate("tapDialog", "Previous (up arrow), will save the bpm", None))
        self.previous.setText(_translate("tapDialog", "Previous", None))
        self.previous.setShortcut(_translate("tapDialog", "Up", None))
        self.next.setToolTip(_translate("tapDialog", "Next (Down arrow), will save the bpm", None))
        self.next.setText(_translate("tapDialog", "Next", None))
        self.next.setShortcut(_translate("tapDialog", "Down", None))
        self.cancel.setToolTip(_translate("tapDialog", "Close the windows without saving", None))
        self.cancel.setText(_translate("tapDialog", "Cancel (escape)", None))
        self.cancel.setShortcut(_translate("tapDialog", "Esc", None))
        self.validate.setToolTip(_translate("tapDialog", "Save the BPM and close the window", None))
        self.validate.setText(_translate("tapDialog", "Done (Enter)", None))
        self.validate.setShortcut(_translate("tapDialog", "Return", None))

