# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_preferences.ui'
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

class Ui_preferences(object):
    def setupUi(self, preferences):
        preferences.setObjectName(_fromUtf8("preferences"))
        preferences.setWindowModality(QtCore.Qt.ApplicationModal)
        preferences.resize(340, 497)
        preferences.setStyleSheet(_fromUtf8("QDialog{\n"
"    background-color: rgb(42,42,42)\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(preferences)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelPropTitle = QtGui.QLabel(preferences)
        self.labelPropTitle.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}"))
        self.labelPropTitle.setObjectName(_fromUtf8("labelPropTitle"))
        self.horizontalLayout.addWidget(self.labelPropTitle)
        self.lineEditSongDir = QtGui.QLineEdit(preferences)
        self.lineEditSongDir.setEnabled(False)
        self.lineEditSongDir.setReadOnly(True)
        self.lineEditSongDir.setObjectName(_fromUtf8("lineEditSongDir"))
        self.horizontalLayout.addWidget(self.lineEditSongDir)
        self.pushButtonSelectPath = QtGui.QPushButton(preferences)
        self.pushButtonSelectPath.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.pushButtonSelectPath.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/search-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelectPath.setIcon(icon)
        self.pushButtonSelectPath.setObjectName(_fromUtf8("pushButtonSelectPath"))
        self.horizontalLayout.addWidget(self.pushButtonSelectPath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.labelPropFadoutTime = QtGui.QLabel(preferences)
        self.labelPropFadoutTime.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}"))
        self.labelPropFadoutTime.setObjectName(_fromUtf8("labelPropFadoutTime"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelPropFadoutTime)
        self.spinBoxFadeOut = QtGui.QSpinBox(preferences)
        self.spinBoxFadeOut.setProperty("value", 4)
        self.spinBoxFadeOut.setObjectName(_fromUtf8("spinBoxFadeOut"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBoxFadeOut)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_3.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem)
        self.labelPropCortinaDuration = QtGui.QLabel(preferences)
        self.labelPropCortinaDuration.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelPropCortinaDuration.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}"))
        self.labelPropCortinaDuration.setObjectName(_fromUtf8("labelPropCortinaDuration"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelPropCortinaDuration)
        self.spinBoxCortinaDuration = QtGui.QSpinBox(preferences)
        self.spinBoxCortinaDuration.setMaximum(240)
        self.spinBoxCortinaDuration.setProperty("value", 30)
        self.spinBoxCortinaDuration.setObjectName(_fromUtf8("spinBoxCortinaDuration"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinBoxCortinaDuration)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.checkBoxWriteTags = QtGui.QCheckBox(preferences)
        self.checkBoxWriteTags.setStyleSheet(_fromUtf8("QCheckBox{\n"
"    color:red;\n"
"    font-size: 14px;\n"
"}"))
        self.checkBoxWriteTags.setObjectName(_fromUtf8("checkBoxWriteTags"))
        self.verticalLayout.addWidget(self.checkBoxWriteTags)
        self.checkBoxNormalize = QtGui.QCheckBox(preferences)
        self.checkBoxNormalize.setObjectName(_fromUtf8("checkBoxNormalize"))
        self.verticalLayout.addWidget(self.checkBoxNormalize)
        self.line = QtGui.QFrame(preferences)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(preferences)
        self.label_3.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.listWidgetTangoType = QtGui.QListWidget(preferences)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetTangoType.sizePolicy().hasHeightForWidth())
        self.listWidgetTangoType.setSizePolicy(sizePolicy)
        self.listWidgetTangoType.setMaximumSize(QtCore.QSize(170, 200))
        self.listWidgetTangoType.setObjectName(_fromUtf8("listWidgetTangoType"))
        self.verticalLayout_4.addWidget(self.listWidgetTangoType)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lineEditTangoType = QtGui.QLineEdit(preferences)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTangoType.sizePolicy().hasHeightForWidth())
        self.lineEditTangoType.setSizePolicy(sizePolicy)
        self.lineEditTangoType.setMinimumSize(QtCore.QSize(100, 27))
        self.lineEditTangoType.setMaximumSize(QtCore.QSize(200, 27))
        self.lineEditTangoType.setAcceptDrops(False)
        self.lineEditTangoType.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditTangoType.setObjectName(_fromUtf8("lineEditTangoType"))
        self.horizontalLayout_6.addWidget(self.lineEditTangoType)
        self.addTypeButton = QtGui.QPushButton(preferences)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTypeButton.sizePolicy().hasHeightForWidth())
        self.addTypeButton.setSizePolicy(sizePolicy)
        self.addTypeButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }"))
        self.addTypeButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/plus-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTypeButton.setIcon(icon1)
        self.addTypeButton.setObjectName(_fromUtf8("addTypeButton"))
        self.horizontalLayout_6.addWidget(self.addTypeButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.removeTypeButton = QtGui.QPushButton(preferences)
        self.removeTypeButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }"))
        self.removeTypeButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/minus-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeTypeButton.setIcon(icon2)
        self.removeTypeButton.setObjectName(_fromUtf8("removeTypeButton"))
        self.horizontalLayout_5.addWidget(self.removeTypeButton)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(preferences)
        self.label_4.setStyleSheet(_fromUtf8("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.selectColorButton = QtGui.QPushButton(preferences)
        self.selectColorButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectColorButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }"))
        self.selectColorButton.setText(_fromUtf8(""))
        self.selectColorButton.setObjectName(_fromUtf8("selectColorButton"))
        self.verticalLayout_5.addWidget(self.selectColorButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(preferences)
        self.buttonBox.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}"))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(preferences)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(preferences)

    def retranslateUi(self, preferences):
        preferences.setWindowTitle(_translate("preferences", "Dialog", None))
        self.labelPropTitle.setText(_translate("preferences", "Song dir", None))
        self.lineEditSongDir.setToolTip(_translate("preferences", "<html><head/><body><p>This is the place where your song are stored on your computer. Click to edit the path.</p></body></html>", None))
        self.lineEditSongDir.setWhatsThis(_translate("preferences", "This is the place where your song are stored on your computer. You can add more than one dir, separate by a coma.", None))
        self.labelPropFadoutTime.setText(_translate("preferences", "FadOut time (in sec)", None))
        self.spinBoxFadeOut.setToolTip(_translate("preferences", "The time of the Fadout duration.", None))
        self.labelPropCortinaDuration.setText(_translate("preferences", "Cortina duration (in sec)", None))
        self.checkBoxWriteTags.setToolTip(_translate("preferences", "Each time you will change a data, the tag of the file will be updated, if the file format allow it", None))
        self.checkBoxWriteTags.setText(_translate("preferences", "Always write Tags when updating a songs", None))
        self.checkBoxNormalize.setToolTip(_translate("preferences", "<html><head/><body><p>If you check this, eachtime you will make a change on one of your file, the file name and path will be update to respcet the following rules : </p><p>YYYY<span style=\" font-weight:600;\">-</span>Name of song<span style=\" font-weight:600;\">-</span>Artist<span style=\" font-weight:600;\">-</span>Album<span style=\" font-weight:600;\">-</span>Type.ext</p><p><span style=\" color:#ff0004;\">Be aware that this will completly change the organisation of your directory !</span></p></body></html>", None))
        self.checkBoxNormalize.setText(_translate("preferences", "Normalize file name and dir", None))
        self.label_3.setText(_translate("preferences", "Tango type", None))
        self.addTypeButton.setToolTip(_translate("preferences", "Add a Tango type", None))
        self.removeTypeButton.setToolTip(_translate("preferences", "Remove a Tango type", None))
        self.label_4.setText(_translate("preferences", "Tango Color", None))

import djtango_rc
