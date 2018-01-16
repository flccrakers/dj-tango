# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_sideDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sideDisplay(object):
    def setupUi(self, sideDisplay):
        sideDisplay.setObjectName("sideDisplay")
        sideDisplay.setWindowModality(QtCore.Qt.NonModal)
        sideDisplay.setEnabled(True)
        sideDisplay.resize(1337, 1092)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/backup/img/logo-djtango.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sideDisplay.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(sideDisplay)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frameType = QtWidgets.QFrame(sideDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameType.sizePolicy().hasHeightForWidth())
        self.frameType.setSizePolicy(sizePolicy)
        self.frameType.setMinimumSize(QtCore.QSize(0, 140))
        self.frameType.setStyleSheet("QFrame{\n"
"    background-color: rgb(160,52,77);\n"
"    border: 0px;\n"
"    margin-right: 0px;\n"
"    margin-bottom: 0px;\n"
"    margin-left: 0px;\n"
"    spacing: 0px;\n"
"    padding: 0px;\n"
"}\n"
"QFrame::layout { margin: 0px }")
        self.frameType.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameType.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameType.setLineWidth(0)
        self.frameType.setObjectName("frameType")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameType)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.labelType = QtWidgets.QLabel(self.frameType)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelType.sizePolicy().hasHeightForWidth())
        self.labelType.setSizePolicy(sizePolicy)
        self.labelType.setMinimumSize(QtCore.QSize(0, 0))
        self.labelType.setStyleSheet("QLabel{\n"
"   font-weight: bold;\n"
"    color: white;\n"
"    font-size: 100px;\n"
"    font-family: \"sans\";\n"
"    background-color: \"transparent\";\n"
"    \n"
"}")
        self.labelType.setScaledContents(False)
        self.labelType.setAlignment(QtCore.Qt.AlignCenter)
        self.labelType.setWordWrap(False)
        self.labelType.setObjectName("labelType")
        self.horizontalLayout_2.addWidget(self.labelType)
        self.PBLayout = QtWidgets.QVBoxLayout()
        self.PBLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.PBLayout.setContentsMargins(40, 2, 5, 2)
        self.PBLayout.setSpacing(0)
        self.PBLayout.setObjectName("PBLayout")
        self.horizontalLayout_2.addLayout(self.PBLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.frameType)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.labelArtist = QtWidgets.QLabel(sideDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelArtist.sizePolicy().hasHeightForWidth())
        self.labelArtist.setSizePolicy(sizePolicy)
        self.labelArtist.setStyleSheet("QLabel{\n"
"    margin-top: 30px;\n"
"    margin-left: 20px;\n"
"    margin-bottom: 25px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    font-size: 100px;\n"
"   font-family: \"sans\"\n"
"}")
        self.labelArtist.setScaledContents(True)
        self.labelArtist.setAlignment(QtCore.Qt.AlignCenter)
        self.labelArtist.setObjectName("labelArtist")
        self.verticalLayout_2.addWidget(self.labelArtist)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.labelTitle = QtWidgets.QLabel(sideDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setStyleSheet("QLabel{\n"
"    margin-left: 20px;\n"
"    color: white;\n"
"    font-size: 70px;\n"
"    font-family: \"sans\"\n"
"}")
        self.labelTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelTitle.setScaledContents(True)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setIndent(-1)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_2.addWidget(self.labelTitle)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.labelSinger = QtWidgets.QLabel(sideDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSinger.sizePolicy().hasHeightForWidth())
        self.labelSinger.setSizePolicy(sizePolicy)
        self.labelSinger.setStyleSheet("QLabel{\n"
"    margin-left: 20px;\n"
"    color: white;\n"
"    font-size: 70px;\n"
"    font-family: \"sans\"\n"
"}")
        self.labelSinger.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSinger.setObjectName("labelSinger")
        self.verticalLayout_2.addWidget(self.labelSinger)
        spacerItem5 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameNext = QtWidgets.QFrame(sideDisplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
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
        self.frameNext.setStyleSheet("QFrame{\n"
"    background-color: rgb(160,52,77);\n"
"    border: 0px;\n"
"    margin-right: 0px;\n"
"    margin-bottom: 0px;\n"
"    margin-left: 0px;\n"
"    spacing: 0px;\n"
"    padding: 0px;\n"
"}\n"
"QFrame::layout { margin: 0px }")
        self.frameNext.setLineWidth(0)
        self.frameNext.setObjectName("frameNext")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameNext)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelNextTanda = QtWidgets.QLabel(self.frameNext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNextTanda.sizePolicy().hasHeightForWidth())
        self.labelNextTanda.setSizePolicy(sizePolicy)
        self.labelNextTanda.setMinimumSize(QtCore.QSize(0, 130))
        self.labelNextTanda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelNextTanda.setStyleSheet("QLabel{\n"
"    font-family: \"sans\";\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    font-size: 70px;\n"
"}")
        self.labelNextTanda.setScaledContents(True)
        self.labelNextTanda.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNextTanda.setObjectName("labelNextTanda")
        self.verticalLayout_4.addWidget(self.labelNextTanda)
        self.verticalLayout_3.addWidget(self.frameNext)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(sideDisplay)
        QtCore.QMetaObject.connectSlotsByName(sideDisplay)

    def retranslateUi(self, sideDisplay):
        _translate = QtCore.QCoreApplication.translate
        sideDisplay.setWindowTitle(_translate("sideDisplay", "sideDisplay"))
        self.labelType.setText(_translate("sideDisplay", "Tango Type"))
        self.labelArtist.setText(_translate("sideDisplay", "Orchesta"))
        self.labelTitle.setText(_translate("sideDisplay", "Title (year - Author)"))
        self.labelSinger.setText(_translate("sideDisplay", "Singer:"))
        self.labelNextTanda.setText(_translate("sideDisplay", "NEXT TANDA (in X song)   |   VALS"))

