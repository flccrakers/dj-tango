# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_tapbpm.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tapDialog(object):
    def setupUi(self, tapDialog):
        tapDialog.setObjectName("tapDialog")
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
        tapDialog.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(tapDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(tapDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"    background-color: rgb(42,42,42)\n"
"}")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.labelTypeBmp = QtWidgets.QLabel(tapDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTypeBmp.sizePolicy().hasHeightForWidth())
        self.labelTypeBmp.setSizePolicy(sizePolicy)
        self.labelTypeBmp.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelTypeBmp.setObjectName("labelTypeBmp")
        self.verticalLayout_2.addWidget(self.labelTypeBmp)
        self.labelDone = QtWidgets.QLabel(tapDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDone.sizePolicy().hasHeightForWidth())
        self.labelDone.setSizePolicy(sizePolicy)
        self.labelDone.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelDone.setObjectName("labelDone")
        self.verticalLayout_2.addWidget(self.labelDone)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.lcdNumber = QtWidgets.QLCDNumber(tapDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(390, 0))
        self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"    color: rgb(160,52,77);\n"
"    background-color: rgb(42,42,42);\n"
"}")
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setNumDigits(5)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tapButton = QtWidgets.QPushButton(tapDialog)
        self.tapButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tapButton.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.tapButton.setDefault(False)
        self.tapButton.setFlat(False)
        self.tapButton.setObjectName("tapButton")
        self.verticalLayout.addWidget(self.tapButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous = QtWidgets.QPushButton(tapDialog)
        self.previous.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previous.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(tapDialog)
        self.next.setFocusPolicy(QtCore.Qt.NoFocus)
        self.next.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.cancel = QtWidgets.QPushButton(tapDialog)
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.validate = QtWidgets.QPushButton(tapDialog)
        self.validate.setFocusPolicy(QtCore.Qt.NoFocus)
        self.validate.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.validate.setObjectName("validate")
        self.horizontalLayout.addWidget(self.validate)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(tapDialog)
        QtCore.QMetaObject.connectSlotsByName(tapDialog)

    def retranslateUi(self, tapDialog):
        _translate = QtCore.QCoreApplication.translate
        tapDialog.setWindowTitle(_translate("tapDialog", "Taping the tempo"))
        self.label.setText(_translate("tapDialog", "Tap on space key while the music is playing, when finish tap on enter to save the calculated bpm. Click enter when finished"))
        self.labelTypeBmp.setText(_translate("tapDialog", "By Human"))
        self.labelDone.setText(_translate("tapDialog", "DONE"))
        self.tapButton.setText(_translate("tapDialog", "Tap (hit space)"))
        self.tapButton.setShortcut(_translate("tapDialog", "Space"))
        self.previous.setToolTip(_translate("tapDialog", "Previous (up arrow), will save the bpm"))
        self.previous.setText(_translate("tapDialog", "Previous"))
        self.previous.setShortcut(_translate("tapDialog", "Up"))
        self.next.setToolTip(_translate("tapDialog", "Next (Down arrow), will save the bpm"))
        self.next.setText(_translate("tapDialog", "Next"))
        self.next.setShortcut(_translate("tapDialog", "Down"))
        self.cancel.setToolTip(_translate("tapDialog", "Close the windows without saving"))
        self.cancel.setText(_translate("tapDialog", "Cancel (escape)"))
        self.cancel.setShortcut(_translate("tapDialog", "Esc"))
        self.validate.setToolTip(_translate("tapDialog", "Save the BPM and close the window"))
        self.validate.setText(_translate("tapDialog", "Done (Enter)"))
        self.validate.setShortcut(_translate("tapDialog", "Return"))

