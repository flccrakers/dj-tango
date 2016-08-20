# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_sideDisplay.ui'
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

class Ui_sideDisplay(object):
    def setupUi(self, sideDisplay):
        sideDisplay.setObjectName(_fromUtf8("sideDisplay"))
        sideDisplay.setWindowModality(QtCore.Qt.NonModal)
        sideDisplay.resize(1327, 1074)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sideDisplay.sizePolicy().hasHeightForWidth())
        sideDisplay.setSizePolicy(sizePolicy)
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
        sideDisplay.setPalette(palette)
        sideDisplay.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        sideDisplay.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../.designer/backup/img/logo-djtango.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sideDisplay.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(sideDisplay)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frameType = QtGui.QFrame(sideDisplay)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameType.sizePolicy().hasHeightForWidth())
        self.frameType.setSizePolicy(sizePolicy)
        self.frameType.setMinimumSize(QtCore.QSize(0, 140))
        self.frameType.setStyleSheet(_fromUtf8("QFrame{\n"
"    background-color: rgb(160,52,77);\n"
"    border: 0px;\n"
"    margin-right: 0px;\n"
"    margin-bottom: 0px;\n"
"    margin-left: 0px;\n"
"    spacing: 0px;\n"
"    padding: 0px;\n"
"}\n"
"QFrame::layout { margin: 0px }"))
        self.frameType.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameType.setFrameShadow(QtGui.QFrame.Plain)
        self.frameType.setLineWidth(0)
        self.frameType.setObjectName(_fromUtf8("frameType"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frameType)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.labelType = QtGui.QLabel(self.frameType)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelType.sizePolicy().hasHeightForWidth())
        self.labelType.setSizePolicy(sizePolicy)
        self.labelType.setMinimumSize(QtCore.QSize(0, 0))
        self.labelType.setStyleSheet(_fromUtf8("QLabel{\n"
"   font-weight: bold;\n"
"    color: white;\n"
"    font-size: 100px;\n"
"    font-family: \"sans\";\n"
"    background-color: \"transparent\";\n"
"    \n"
"}"))
        self.labelType.setScaledContents(False)
        self.labelType.setAlignment(QtCore.Qt.AlignCenter)
        self.labelType.setWordWrap(False)
        self.labelType.setObjectName(_fromUtf8("labelType"))
        self.horizontalLayout_2.addWidget(self.labelType)
        self.PBLayout = QtGui.QVBoxLayout()
        self.PBLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.PBLayout.setContentsMargins(40, 2, 5, 2)
        self.PBLayout.setSpacing(0)
        self.PBLayout.setObjectName(_fromUtf8("PBLayout"))
        self.horizontalLayout_2.addLayout(self.PBLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.frameType)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtGui.QSpacerItem(20, 120, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.labelArtist = QtGui.QLabel(sideDisplay)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelArtist.sizePolicy().hasHeightForWidth())
        self.labelArtist.setSizePolicy(sizePolicy)
        self.labelArtist.setStyleSheet(_fromUtf8("QLabel{\n"
"    margin-top: 30px;\n"
"    margin-left: 20px;\n"
"    margin-bottom: 25px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    font-size: 100px;\n"
"   font-family: \"sans\"\n"
"}"))
        self.labelArtist.setScaledContents(True)
        self.labelArtist.setAlignment(QtCore.Qt.AlignCenter)
        self.labelArtist.setObjectName(_fromUtf8("labelArtist"))
        self.verticalLayout_2.addWidget(self.labelArtist)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.labelTitle = QtGui.QLabel(sideDisplay)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setStyleSheet(_fromUtf8("QLabel{\n"
"    margin-left: 20px;\n"
"    color: white;\n"
"    font-size: 70px;\n"
"    font-family: \"sans\"\n"
"}"))
        self.labelTitle.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelTitle.setScaledContents(True)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setIndent(-1)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.verticalLayout_2.addWidget(self.labelTitle)
        spacerItem4 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frameNext = QtGui.QFrame(sideDisplay)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameNext.sizePolicy().hasHeightForWidth())
        self.frameNext.setSizePolicy(sizePolicy)
        self.frameNext.setMinimumSize(QtCore.QSize(0, 130))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frameNext.setPalette(palette)
        self.frameNext.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frameNext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameNext.setStyleSheet(_fromUtf8("QFrame{\n"
"    background-color: rgb(160,52,77);\n"
"    border: 0px;\n"
"    margin-right: 0px;\n"
"    margin-bottom: 0px;\n"
"    margin-left: 0px;\n"
"    spacing: 0px;\n"
"    padding: 0px;\n"
"}\n"
"QFrame::layout { margin: 0px }"))
        self.frameNext.setLineWidth(0)
        self.frameNext.setObjectName(_fromUtf8("frameNext"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frameNext)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.labelNextTanda = QtGui.QLabel(self.frameNext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNextTanda.sizePolicy().hasHeightForWidth())
        self.labelNextTanda.setSizePolicy(sizePolicy)
        self.labelNextTanda.setMinimumSize(QtCore.QSize(0, 130))
        self.labelNextTanda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelNextTanda.setStyleSheet(_fromUtf8("QLabel{\n"
"    font-family: \"sans\";\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    font-size: 70px;\n"
"}"))
        self.labelNextTanda.setScaledContents(True)
        self.labelNextTanda.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNextTanda.setObjectName(_fromUtf8("labelNextTanda"))
        self.verticalLayout_4.addWidget(self.labelNextTanda)
        self.verticalLayout_3.addWidget(self.frameNext)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(sideDisplay)
        QtCore.QMetaObject.connectSlotsByName(sideDisplay)

    def retranslateUi(self, sideDisplay):
        sideDisplay.setWindowTitle(_translate("sideDisplay", "sideDisplay", None))
        self.labelType.setText(_translate("sideDisplay", "Tango Type", None))
        self.labelArtist.setText(_translate("sideDisplay", "Artiste", None))
        self.labelTitle.setText(_translate("sideDisplay", "Title (year - Author)", None))
        self.labelNextTanda.setText(_translate("sideDisplay", "NEXT TANDA (in X song)   |   VALS", None))

