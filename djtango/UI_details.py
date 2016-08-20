# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_details.ui'
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

class Ui_details(object):
    def setupUi(self, details):
        details.setObjectName(_fromUtf8("details"))
        details.setWindowModality(QtCore.Qt.WindowModal)
        details.resize(340, 365)
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
        details.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logo-djtango.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        details.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(details)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelPropTitle = QtGui.QLabel(details)
        self.labelPropTitle.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 18px;\n"
"}"))
        self.labelPropTitle.setObjectName(_fromUtf8("labelPropTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelPropTitle)
        self.lineEditTitle = QtGui.QLineEdit(details)
        self.lineEditTitle.setObjectName(_fromUtf8("lineEditTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditTitle)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        self.labelPropArtist = QtGui.QLabel(details)
        self.labelPropArtist.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 18px;\n"
"}"))
        self.labelPropArtist.setObjectName(_fromUtf8("labelPropArtist"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelPropArtist)
        self.lineEditArtist = QtGui.QLineEdit(details)
        self.lineEditArtist.setObjectName(_fromUtf8("lineEditArtist"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditArtist)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.labelPropAlbum = QtGui.QLabel(details)
        self.labelPropAlbum.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 18px;\n"
"}"))
        self.labelPropAlbum.setObjectName(_fromUtf8("labelPropAlbum"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelPropAlbum)
        self.lineEditAlbum = QtGui.QLineEdit(details)
        self.lineEditAlbum.setObjectName(_fromUtf8("lineEditAlbum"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditAlbum)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.labelPropGenre = QtGui.QLabel(details)
        self.labelPropGenre.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 18px;\n"
"}"))
        self.labelPropGenre.setObjectName(_fromUtf8("labelPropGenre"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.labelPropGenre)
        self.comboBoxTangoType = QtGui.QComboBox(details)
        self.comboBoxTangoType.setObjectName(_fromUtf8("comboBoxTangoType"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.comboBoxTangoType)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtGui.QFormLayout.LabelRole, spacerItem3)
        self.labelPropYear = QtGui.QLabel(details)
        self.labelPropYear.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 18px;\n"
"}"))
        self.labelPropYear.setObjectName(_fromUtf8("labelPropYear"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.labelPropYear)
        self.spinBoxYear = QtGui.QSpinBox(details)
        self.spinBoxYear.setMaximum(99999)
        self.spinBoxYear.setObjectName(_fromUtf8("spinBoxYear"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.spinBoxYear)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textPath = QtGui.QTextEdit(details)
        self.textPath.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textPath.setObjectName(_fromUtf8("textPath"))
        self.verticalLayout_2.addWidget(self.textPath)
        self.checkBoxPlayMusic = QtGui.QCheckBox(details)
        self.checkBoxPlayMusic.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBoxPlayMusic.setStyleSheet(_fromUtf8("QCheckBox{\n"
"    color:white;\n"
"}"))
        self.checkBoxPlayMusic.setObjectName(_fromUtf8("checkBoxPlayMusic"))
        self.verticalLayout_2.addWidget(self.checkBoxPlayMusic)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.previousButton = QtGui.QPushButton(details)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previousButton.setStyleSheet(_fromUtf8("QPushButton#previousButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:disabled {\n"
"     color: grey;\n"
"    background-color: red;\n"
"}\n"
"QPushButton:on {\n"
"        background: red;\n"
"}"))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.horizontalLayout.addWidget(self.previousButton)
        self.nextButton = QtGui.QPushButton(details)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nextButton.setStyleSheet(_fromUtf8("QPushButton#nextButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }"))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.closeButton = QtGui.QPushButton(details)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 119, 70, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 119, 70, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.closeButton.setPalette(palette)
        self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeButton.setStyleSheet(_fromUtf8("QPushButton#closeButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }"))
        self.closeButton.setAutoDefault(False)
        self.closeButton.setDefault(False)
        self.closeButton.setFlat(False)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(details)
        QtCore.QMetaObject.connectSlotsByName(details)

    def retranslateUi(self, details):
        details.setWindowTitle(_translate("details", "Song Properties", None))
        self.labelPropTitle.setText(_translate("details", "Title:", None))
        self.labelPropArtist.setText(_translate("details", "Artist:", None))
        self.labelPropAlbum.setText(_translate("details", "Album:", None))
        self.labelPropGenre.setText(_translate("details", "Tango type:", None))
        self.labelPropYear.setText(_translate("details", "Year:", None))
        self.checkBoxPlayMusic.setText(_translate("details", "Play music when clicking next or previous", None))
        self.previousButton.setText(_translate("details", "Previous", None))
        self.previousButton.setShortcut(_translate("details", "Up", None))
        self.nextButton.setText(_translate("details", "Next", None))
        self.nextButton.setShortcut(_translate("details", "Down", None))
        self.closeButton.setText(_translate("details", "Close", None))
        self.closeButton.setShortcut(_translate("details", "Return, Enter", None))

