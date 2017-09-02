# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_preferences.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_preferences(object):
    def setupUi(self, preferences):
        preferences.setObjectName("preferences")
        preferences.setWindowModality(QtCore.Qt.ApplicationModal)
        preferences.resize(340, 497)
        preferences.setStyleSheet("QDialog{\n"
"    background-color: rgb(42,42,42)\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(preferences)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPropTitle = QtWidgets.QLabel(preferences)
        self.labelPropTitle.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}")
        self.labelPropTitle.setObjectName("labelPropTitle")
        self.horizontalLayout.addWidget(self.labelPropTitle)
        self.lineEditSongDir = QtWidgets.QLineEdit(preferences)
        self.lineEditSongDir.setEnabled(False)
        self.lineEditSongDir.setReadOnly(True)
        self.lineEditSongDir.setObjectName("lineEditSongDir")
        self.horizontalLayout.addWidget(self.lineEditSongDir)
        self.pushButtonSelectPath = QtWidgets.QPushButton(preferences)
        self.pushButtonSelectPath.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.pushButtonSelectPath.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/search-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelectPath.setIcon(icon)
        self.pushButtonSelectPath.setObjectName("pushButtonSelectPath")
        self.horizontalLayout.addWidget(self.pushButtonSelectPath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelPropFadoutTime = QtWidgets.QLabel(preferences)
        self.labelPropFadoutTime.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}")
        self.labelPropFadoutTime.setObjectName("labelPropFadoutTime")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelPropFadoutTime)
        self.spinBoxFadeOut = QtWidgets.QSpinBox(preferences)
        self.spinBoxFadeOut.setProperty("value", 4)
        self.spinBoxFadeOut.setObjectName("spinBoxFadeOut")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxFadeOut)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.labelPropCortinaDuration = QtWidgets.QLabel(preferences)
        self.labelPropCortinaDuration.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelPropCortinaDuration.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}")
        self.labelPropCortinaDuration.setObjectName("labelPropCortinaDuration")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelPropCortinaDuration)
        self.spinBoxCortinaDuration = QtWidgets.QSpinBox(preferences)
        self.spinBoxCortinaDuration.setMaximum(240)
        self.spinBoxCortinaDuration.setProperty("value", 30)
        self.spinBoxCortinaDuration.setObjectName("spinBoxCortinaDuration")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBoxCortinaDuration)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.checkBoxWriteTags = QtWidgets.QCheckBox(preferences)
        self.checkBoxWriteTags.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBoxWriteTags.setStyleSheet("QCheckBox{\n"
"    border: none;\n"
"   color: white;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(42,42,42);       \n"
"    border: 1px solid white;\n"
"    image: url(../gui/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(160,52,77);      \n"
"      border: 1px solid white;  \n"
"}")
        self.checkBoxWriteTags.setObjectName("checkBoxWriteTags")
        self.verticalLayout.addWidget(self.checkBoxWriteTags)
        self.checkBoxNormalize = QtWidgets.QCheckBox(preferences)
        self.checkBoxNormalize.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBoxNormalize.setStyleSheet("QCheckBox{\n"
"    border: none;\n"
"   color: white;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(42,42,42);       \n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(160,52,77);      \n"
"      border: 1px solid white;  \n"
"}")
        self.checkBoxNormalize.setObjectName("checkBoxNormalize")
        self.verticalLayout.addWidget(self.checkBoxNormalize)
        self.line = QtWidgets.QFrame(preferences)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(preferences)
        self.label_3.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.listWidgetTangoType = QtWidgets.QListWidget(preferences)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetTangoType.sizePolicy().hasHeightForWidth())
        self.listWidgetTangoType.setSizePolicy(sizePolicy)
        self.listWidgetTangoType.setMaximumSize(QtCore.QSize(170, 200))
        self.listWidgetTangoType.setObjectName("listWidgetTangoType")
        self.verticalLayout_4.addWidget(self.listWidgetTangoType)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEditTangoType = QtWidgets.QLineEdit(preferences)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTangoType.sizePolicy().hasHeightForWidth())
        self.lineEditTangoType.setSizePolicy(sizePolicy)
        self.lineEditTangoType.setMinimumSize(QtCore.QSize(100, 27))
        self.lineEditTangoType.setMaximumSize(QtCore.QSize(200, 27))
        self.lineEditTangoType.setAcceptDrops(False)
        self.lineEditTangoType.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditTangoType.setObjectName("lineEditTangoType")
        self.horizontalLayout_6.addWidget(self.lineEditTangoType)
        self.addTypeButton = QtWidgets.QPushButton(preferences)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTypeButton.sizePolicy().hasHeightForWidth())
        self.addTypeButton.setSizePolicy(sizePolicy)
        self.addTypeButton.setStyleSheet("QPushButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }")
        self.addTypeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/plus-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTypeButton.setIcon(icon1)
        self.addTypeButton.setObjectName("addTypeButton")
        self.horizontalLayout_6.addWidget(self.addTypeButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.removeTypeButton = QtWidgets.QPushButton(preferences)
        self.removeTypeButton.setStyleSheet("QPushButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }")
        self.removeTypeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/minus-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeTypeButton.setIcon(icon2)
        self.removeTypeButton.setObjectName("removeTypeButton")
        self.horizontalLayout_5.addWidget(self.removeTypeButton)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(preferences)
        self.label_4.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 14px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.selectColorButton = QtWidgets.QPushButton(preferences)
        self.selectColorButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectColorButton.setStyleSheet("QPushButton{\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }")
        self.selectColorButton.setText("")
        self.selectColorButton.setObjectName("selectColorButton")
        self.verticalLayout_5.addWidget(self.selectColorButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(preferences)
        self.buttonBox.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(preferences)
        self.buttonBox.accepted.connect(preferences.accept)
        self.buttonBox.rejected.connect(preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(preferences)

    def retranslateUi(self, preferences):
        _translate = QtCore.QCoreApplication.translate
        preferences.setWindowTitle(_translate("preferences", "Dialog"))
        self.labelPropTitle.setText(_translate("preferences", "Song dir"))
        self.lineEditSongDir.setToolTip(_translate("preferences", "<html><head/><body><p>This is the place where your song are stored on your computer. Click to edit the path.</p></body></html>"))
        self.lineEditSongDir.setWhatsThis(_translate("preferences", "This is the place where your song are stored on your computer. You can add more than one dir, separate by a coma."))
        self.labelPropFadoutTime.setText(_translate("preferences", "FadOut time (in sec)"))
        self.spinBoxFadeOut.setToolTip(_translate("preferences", "The time of the Fadout duration."))
        self.labelPropCortinaDuration.setText(_translate("preferences", "Cortina duration (in sec)"))
        self.checkBoxWriteTags.setToolTip(_translate("preferences", "Each time you will change a data, the tag of the file will be updated, if the file format allow it"))
        self.checkBoxWriteTags.setText(_translate("preferences", "Always write Tags when updating a songs"))
        self.checkBoxNormalize.setToolTip(_translate("preferences", "<html><head/><body><p>If you check this, eachtime you will make a change on one of your file, the file name and path will be update to respcet the following rules : </p><p>YYYY<span style=\" font-weight:600;\">-</span>Name of song<span style=\" font-weight:600;\">-</span>Artist<span style=\" font-weight:600;\">-</span>Album<span style=\" font-weight:600;\">-</span>Type.ext</p><p><span style=\" color:#ff0004;\">Be aware that this will completly change the organisation of your directory !</span></p></body></html>"))
        self.checkBoxNormalize.setText(_translate("preferences", "Normalize file name and dir"))
        self.label_3.setText(_translate("preferences", "Tango type"))
        self.addTypeButton.setToolTip(_translate("preferences", "Add a Tango type"))
        self.removeTypeButton.setToolTip(_translate("preferences", "Remove a Tango type"))
        self.label_4.setText(_translate("preferences", "Tango Color"))

import djtango_rc
