# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_djtango.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AudioPlayerDialog(object):
    def setupUi(self, AudioPlayerDialog):
        AudioPlayerDialog.setObjectName("AudioPlayerDialog")
        AudioPlayerDialog.resize(959, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AudioPlayerDialog.sizePolicy().hasHeightForWidth())
        AudioPlayerDialog.setSizePolicy(sizePolicy)
        AudioPlayerDialog.setMinimumSize(QtCore.QSize(300, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        AudioPlayerDialog.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/logo-djtango.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AudioPlayerDialog.setWindowIcon(icon)
        AudioPlayerDialog.setAutoFillBackground(True)
        AudioPlayerDialog.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(AudioPlayerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 300))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTypeSong = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.labelTypeSong.setPalette(palette)
        self.labelTypeSong.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 40px;    \n"
"}")
        self.labelTypeSong.setTextFormat(QtCore.Qt.AutoText)
        self.labelTypeSong.setScaledContents(False)
        self.labelTypeSong.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTypeSong.setObjectName("labelTypeSong")
        self.horizontalLayout.addWidget(self.labelTypeSong)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 22px;    \n"
"}")
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelArtist = QtWidgets.QLabel(self.centralwidget)
        self.labelArtist.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.labelArtist.setObjectName("labelArtist")
        self.horizontalLayout_3.addWidget(self.labelArtist)
        self.labelSep = QtWidgets.QLabel(self.centralwidget)
        self.labelSep.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-style: bold;\n"
"}")
        self.labelSep.setObjectName("labelSep")
        self.horizontalLayout_3.addWidget(self.labelSep)
        self.labelAlbum = QtWidgets.QLabel(self.centralwidget)
        self.labelAlbum.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-style: italic;\n"
"}")
        self.labelAlbum.setObjectName("labelAlbum")
        self.horizontalLayout_3.addWidget(self.labelAlbum)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.checkBoxLetCortinaUntilEnd = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxLetCortinaUntilEnd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBoxLetCortinaUntilEnd.setStyleSheet("QCheckBox{\n"
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
        self.checkBoxLetCortinaUntilEnd.setObjectName("checkBoxLetCortinaUntilEnd")
        self.horizontalLayout.addWidget(self.checkBoxLetCortinaUntilEnd)
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    \n"
"}")
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.songSlider = QtWidgets.QSlider(self.centralwidget)
        self.songSlider.setStyleSheet("QSlider::groove:horizontal{\n"
"    border: 1px solid white;\n"
"   height: 10px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: #2a2a2a;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: white;\n"
"    border: 3px solid #a0344d;\n"
"      width: 5px;\n"
"    \n"
"    margin: -2px -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 10px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #a0344d; \n"
"    /*height: 8px;*/\n"
"    border: 1px solid white;\n"
"} \n"
"\n"
"")
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("songSlider")
        self.horizontalLayout.addWidget(self.songSlider)
        self.playToolButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playToolButton.sizePolicy().hasHeightForWidth())
        self.playToolButton.setSizePolicy(sizePolicy)
        self.playToolButton.setMinimumSize(QtCore.QSize(0, 40))
        self.playToolButton.setMaximumSize(QtCore.QSize(40, 40))
        self.playToolButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.playToolButton.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playToolButton.setIcon(icon1)
        self.playToolButton.setIconSize(QtCore.QSize(40, 40))
        self.playToolButton.setObjectName("playToolButton")
        self.horizontalLayout.addWidget(self.playToolButton)
        self.stopToolButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopToolButton.sizePolicy().hasHeightForWidth())
        self.stopToolButton.setSizePolicy(sizePolicy)
        self.stopToolButton.setMaximumSize(QtCore.QSize(40, 40))
        self.stopToolButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stopToolButton.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.stopToolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/stop-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopToolButton.setIcon(icon2)
        self.stopToolButton.setIconSize(QtCore.QSize(40, 40))
        self.stopToolButton.setObjectName("stopToolButton")
        self.horizontalLayout.addWidget(self.stopToolButton)
        spacerItem4 = QtWidgets.QSpacerItem(30, 21, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButtonRandom = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRandom.sizePolicy().hasHeightForWidth())
        self.pushButtonRandom.setSizePolicy(sizePolicy)
        self.pushButtonRandom.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRandom.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonRandom.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/img/ic_shuffle_white_24dp_1x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRandom.setIcon(icon3)
        self.pushButtonRandom.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonRandom.setObjectName("pushButtonRandom")
        self.horizontalLayout_5.addWidget(self.pushButtonRandom)
        self.pushButtonClearFilter = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClearFilter.sizePolicy().hasHeightForWidth())
        self.pushButtonClearFilter.setSizePolicy(sizePolicy)
        self.pushButtonClearFilter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonClearFilter.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonClearFilter.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/img/clear-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClearFilter.setIcon(icon4)
        self.pushButtonClearFilter.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonClearFilter.setObjectName("pushButtonClearFilter")
        self.horizontalLayout_5.addWidget(self.pushButtonClearFilter)
        self.comboBoxArtist = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxArtist.setMaximumSize(QtCore.QSize(250, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.comboBoxArtist.setPalette(palette)
        self.comboBoxArtist.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBoxArtist.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBoxArtist.setStyleSheet("QComboBox\n"
"{\n"
"    color:white;\n"
"    padding:1px;\n"
"    background-color:rgba(160,52,77,80);\n"
"    border-style: none;\n"
"}\n"
"QComboBox QListView\n"
"{\n"
"    border-style: none;\n"
"    background-color:rgba(42,42,42)\n"
"    \n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border:1px;\n"
"    border-color:white;\n"
"    border-left-style:solid;\n"
"    border-top-style: none;\n"
"    border-bottom-style: none;\n"
"    border-right-style: none;\n"
"\n"
"   \n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(./djtango/img/arrow-bottom.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-style: none;\n"
"}")
        self.comboBoxArtist.setEditable(False)
        self.comboBoxArtist.setObjectName("comboBoxArtist")
        self.horizontalLayout_5.addWidget(self.comboBoxArtist)
        self.comboBoxAlbum = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxAlbum.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBoxAlbum.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBoxAlbum.setStyleSheet("QComboBox\n"
"{\n"
"    color:white;\n"
"    padding:1px;\n"
"    background-color:rgba(160,52,77,80);\n"
"    border-style: none;\n"
"}\n"
"QComboBox QListView\n"
"{\n"
"    border-style: none;\n"
"    background-color:rgba(42,42,42)\n"
"    \n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border:1px;\n"
"    border-color:white;\n"
"    border-left-style:solid;\n"
"    border-top-style: none;\n"
"    border-bottom-style: none;\n"
"    border-right-style: none;\n"
"\n"
"   \n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(./djtango/img/arrow-bottom.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-style: none;\n"
"}")
        self.comboBoxAlbum.setObjectName("comboBoxAlbum")
        self.horizontalLayout_5.addWidget(self.comboBoxAlbum)
        self.comboBoxGenre = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxGenre.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBoxGenre.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBoxGenre.setStyleSheet("QComboBox\n"
"{\n"
"    color:white;\n"
"    padding:1px;\n"
"    background-color:rgba(160,52,77,80);\n"
"    border-style: none;\n"
"}\n"
"QComboBox QListView\n"
"{\n"
"    border-style: none;\n"
"    background-color:rgba(42,42,42)\n"
"    \n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border:1px;\n"
"    border-color:white;\n"
"    border-left-style:solid;\n"
"    border-top-style: none;\n"
"    border-bottom-style: none;\n"
"    border-right-style: none;\n"
"\n"
"   \n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(./djtango/img/arrow-bottom.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-style: none;\n"
"}")
        self.comboBoxGenre.setFrame(True)
        self.comboBoxGenre.setObjectName("comboBoxGenre")
        self.horizontalLayout_5.addWidget(self.comboBoxGenre)
        self.lineEditFilter = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFilter.sizePolicy().hasHeightForWidth())
        self.lineEditFilter.setSizePolicy(sizePolicy)
        self.lineEditFilter.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditFilter.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditFilter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditFilter.setStyleSheet("QLineEdit{\n"
"    color:white;\n"
"    background:rgb(42,42,42);\n"
"    border-style: none;\n"
"\n"
"}")
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout_5.addWidget(self.lineEditFilter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.labelsongNB_source = QtWidgets.QLabel(self.centralwidget)
        self.labelsongNB_source.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.labelsongNB_source.setObjectName("labelsongNB_source")
        self.verticalLayout_7.addWidget(self.labelsongNB_source)
        self.milongaSource = QtWidgets.QTableView(self.centralwidget)
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
        self.milongaSource.setPalette(palette)
        self.milongaSource.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.milongaSource.setStyleSheet("QTableView{\n"
"    color:white;\n"
"    font-size: 12px;\n"
"    background: rgb(42, 42, 42);\n"
"    \n"
"}\n"
"QHeaderView::section{\n"
"    color:white;\n"
"    background: rgb(42, 42, 42);\n"
"}\n"
"\n"
"\n"
"QHeaderView{\n"
"    color:white;\n"
"    background: rgb(42, 42, 42);\n"
"}\n"
"")
        self.milongaSource.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.milongaSource.setTabKeyNavigation(False)
        self.milongaSource.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.milongaSource.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.milongaSource.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.milongaSource.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.milongaSource.setShowGrid(False)
        self.milongaSource.setGridStyle(QtCore.Qt.NoPen)
        self.milongaSource.setSortingEnabled(True)
        self.milongaSource.setWordWrap(False)
        self.milongaSource.setCornerButtonEnabled(False)
        self.milongaSource.setObjectName("milongaSource")
        self.milongaSource.horizontalHeader().setStretchLastSection(True)
        self.milongaSource.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.milongaSource)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.pushButtonHideDest = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonHideDest.sizePolicy().hasHeightForWidth())
        self.pushButtonHideDest.setSizePolicy(sizePolicy)
        self.pushButtonHideDest.setMaximumSize(QtCore.QSize(10, 16777215))
        self.pushButtonHideDest.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.pushButtonHideDest.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonHideDest.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"    border: none;\n"
" }\n"
"")
        self.pushButtonHideDest.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/img/hide-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonHideDest.setIcon(icon5)
        self.pushButtonHideDest.setIconSize(QtCore.QSize(10, 80))
        self.pushButtonHideDest.setObjectName("pushButtonHideDest")
        self.horizontalLayout_4.addWidget(self.pushButtonHideDest)
        self.pushButtonHideSource = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonHideSource.sizePolicy().hasHeightForWidth())
        self.pushButtonHideSource.setSizePolicy(sizePolicy)
        self.pushButtonHideSource.setMaximumSize(QtCore.QSize(10, 16777215))
        self.pushButtonHideSource.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.pushButtonHideSource.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonHideSource.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"    border: none;\n"
" }\n"
"")
        self.pushButtonHideSource.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/img/hide-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonHideSource.setIcon(icon6)
        self.pushButtonHideSource.setIconSize(QtCore.QSize(10, 80))
        self.pushButtonHideSource.setObjectName("pushButtonHideSource")
        self.horizontalLayout_4.addWidget(self.pushButtonHideSource)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonMilongaClear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMilongaClear.sizePolicy().hasHeightForWidth())
        self.pushButtonMilongaClear.setSizePolicy(sizePolicy)
        self.pushButtonMilongaClear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonMilongaClear.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonMilongaClear.setText("")
        self.pushButtonMilongaClear.setIcon(icon4)
        self.pushButtonMilongaClear.setIconSize(QtCore.QSize(24, 28))
        self.pushButtonMilongaClear.setObjectName("pushButtonMilongaClear")
        self.horizontalLayout_6.addWidget(self.pushButtonMilongaClear)
        self.labelMilongaName = QtWidgets.QLabel(self.centralwidget)
        self.labelMilongaName.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.labelMilongaName.setObjectName("labelMilongaName")
        self.horizontalLayout_6.addWidget(self.labelMilongaName)
        self.pushButtonLoadMilonga = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLoadMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonLoadMilonga.setSizePolicy(sizePolicy)
        self.pushButtonLoadMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonLoadMilonga.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonLoadMilonga.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/img/ic_folder_white_24dp_1x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLoadMilonga.setIcon(icon7)
        self.pushButtonLoadMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonLoadMilonga.setObjectName("pushButtonLoadMilonga")
        self.horizontalLayout_6.addWidget(self.pushButtonLoadMilonga)
        self.pushButtonInfoMilonga = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInfoMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonInfoMilonga.setSizePolicy(sizePolicy)
        self.pushButtonInfoMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInfoMilonga.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonInfoMilonga.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/img/ic_info_white_24dp_1x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonInfoMilonga.setIcon(icon8)
        self.pushButtonInfoMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonInfoMilonga.setObjectName("pushButtonInfoMilonga")
        self.horizontalLayout_6.addWidget(self.pushButtonInfoMilonga)
        self.pushButtonSaveMilongaAs = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSaveMilongaAs.sizePolicy().hasHeightForWidth())
        self.pushButtonSaveMilongaAs.setSizePolicy(sizePolicy)
        self.pushButtonSaveMilongaAs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonSaveMilongaAs.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonSaveMilongaAs.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/img/ic_save_white_24dp_1x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSaveMilongaAs.setIcon(icon9)
        self.pushButtonSaveMilongaAs.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonSaveMilongaAs.setObjectName("pushButtonSaveMilongaAs")
        self.horizontalLayout_6.addWidget(self.pushButtonSaveMilongaAs)
        self.pushButtonSaveMilonga = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSaveMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonSaveMilonga.setSizePolicy(sizePolicy)
        self.pushButtonSaveMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonSaveMilonga.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonSaveMilonga.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/img/save-milonga-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSaveMilonga.setIcon(icon10)
        self.pushButtonSaveMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonSaveMilonga.setObjectName("pushButtonSaveMilonga")
        self.horizontalLayout_6.addWidget(self.pushButtonSaveMilonga)
        self.pushButtonDeleteMilonga = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteMilonga.setSizePolicy(sizePolicy)
        self.pushButtonDeleteMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonDeleteMilonga.setStyleSheet("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
"QPushButton:hover{\n"
"  border-radius: 4px;\n"
"  border: 1px solid rgba(160,52,77,70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgba(160,52,77,100);\n"
"}\n"
"\n"
"")
        self.pushButtonDeleteMilonga.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/img/ic_delete_white_24dp_1x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDeleteMilonga.setIcon(icon11)
        self.pushButtonDeleteMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonDeleteMilonga.setObjectName("pushButtonDeleteMilonga")
        self.horizontalLayout_6.addWidget(self.pushButtonDeleteMilonga)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.labelSizeDuration = QtWidgets.QLabel(self.centralwidget)
        self.labelSizeDuration.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.labelSizeDuration.setObjectName("labelSizeDuration")
        self.verticalLayout_8.addWidget(self.labelSizeDuration)
        self.milongaDest = QtWidgets.QTableView(self.centralwidget)
        self.milongaDest.setFocusPolicy(QtCore.Qt.NoFocus)
        self.milongaDest.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.milongaDest.setStyleSheet("QTableView{\n"
"    color:white;\n"
"    font-size: 12px;\n"
"    background: rgb(42, 42, 42);\n"
"    \n"
"}\n"
"QHeaderView::section{\n"
"    color:white;\n"
"    background: rgb(42, 42, 42);\n"
"}\n"
"\n"
"\n"
"QHeaderView{\n"
"    color:white;\n"
"    background: rgb(42, 42, 42);\n"
"}\n"
"")
        self.milongaDest.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.milongaDest.setProperty("showDropIndicator", True)
        self.milongaDest.setDragEnabled(True)
        self.milongaDest.setDragDropOverwriteMode(True)
        self.milongaDest.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.milongaDest.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.milongaDest.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.milongaDest.setShowGrid(False)
        self.milongaDest.setWordWrap(False)
        self.milongaDest.setCornerButtonEnabled(False)
        self.milongaDest.setObjectName("milongaDest")
        self.verticalLayout_8.addWidget(self.milongaDest)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        AudioPlayerDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AudioPlayerDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdition = QtWidgets.QMenu(self.menubar)
        self.menuEdition.setObjectName("menuEdition")
        self.menuDisplay = QtWidgets.QMenu(self.menubar)
        self.menuDisplay.setObjectName("menuDisplay")
        AudioPlayerDialog.setMenuBar(self.menubar)
        self.actionPreferences = QtWidgets.QAction(AudioPlayerDialog)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionFullscreen = QtWidgets.QAction(AudioPlayerDialog)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionDisplay_side_screen = QtWidgets.QAction(AudioPlayerDialog)
        self.actionDisplay_side_screen.setCheckable(True)
        self.actionDisplay_side_screen.setIconVisibleInMenu(True)
        self.actionDisplay_side_screen.setObjectName("actionDisplay_side_screen")
        self.actionImport_file = QtWidgets.QAction(AudioPlayerDialog)
        self.actionImport_file.setObjectName("actionImport_file")
        self.actionImport_directory = QtWidgets.QAction(AudioPlayerDialog)
        self.actionImport_directory.setObjectName("actionImport_directory")
        self.actionEdit_details_of_current_song = QtWidgets.QAction(AudioPlayerDialog)
        self.actionEdit_details_of_current_song.setObjectName("actionEdit_details_of_current_song")
        self.actionLoad_BPM_from_ID3_Tag = QtWidgets.QAction(AudioPlayerDialog)
        self.actionLoad_BPM_from_ID3_Tag.setObjectName("actionLoad_BPM_from_ID3_Tag")
        self.actionTap_yourself_BPM = QtWidgets.QAction(AudioPlayerDialog)
        self.actionTap_yourself_BPM.setObjectName("actionTap_yourself_BPM")
        self.menuFile.addAction(self.actionImport_file)
        self.menuFile.addAction(self.actionImport_directory)
        self.menuEdition.addAction(self.actionPreferences)
        self.menuEdition.addSeparator()
        self.menuEdition.addAction(self.actionEdit_details_of_current_song)
        self.menuEdition.addAction(self.actionLoad_BPM_from_ID3_Tag)
        self.menuEdition.addAction(self.actionTap_yourself_BPM)
        self.menuDisplay.addAction(self.actionFullscreen)
        self.menuDisplay.addAction(self.actionDisplay_side_screen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())

        self.retranslateUi(AudioPlayerDialog)
        QtCore.QMetaObject.connectSlotsByName(AudioPlayerDialog)

    def retranslateUi(self, AudioPlayerDialog):
        _translate = QtCore.QCoreApplication.translate
        AudioPlayerDialog.setWindowTitle(_translate("AudioPlayerDialog", "DjTango"))
        self.labelTypeSong.setText(_translate("AudioPlayerDialog", "-"))
        self.labelTitle.setText(_translate("AudioPlayerDialog", "TextLabel"))
        self.labelArtist.setText(_translate("AudioPlayerDialog", "NA"))
        self.labelSep.setText(_translate("AudioPlayerDialog", "-"))
        self.labelAlbum.setText(_translate("AudioPlayerDialog", "NA"))
        self.checkBoxLetCortinaUntilEnd.setText(_translate("AudioPlayerDialog", "End Cort."))
        self.timeLabel.setText(_translate("AudioPlayerDialog", "-"))
        self.playToolButton.setToolTip(_translate("AudioPlayerDialog", "play / pause"))
        self.playToolButton.setShortcut(_translate("AudioPlayerDialog", "Space"))
        self.stopToolButton.setToolTip(_translate("AudioPlayerDialog", "stop"))
        self.pushButtonClearFilter.setToolTip(_translate("AudioPlayerDialog", "clear the filters"))
        self.lineEditFilter.setToolTip(_translate("AudioPlayerDialog", "Enter some text and type enter to filter"))
        self.labelsongNB_source.setText(_translate("AudioPlayerDialog", "0 song"))
        self.pushButtonMilongaClear.setToolTip(_translate("AudioPlayerDialog", "clear the milonga table (will not be saved)"))
        self.labelMilongaName.setText(_translate("AudioPlayerDialog", "- No Milonga -"))
        self.pushButtonLoadMilonga.setToolTip(_translate("AudioPlayerDialog", "Load Milonga"))
        self.pushButtonLoadMilonga.setShortcut(_translate("AudioPlayerDialog", "Ctrl+O"))
        self.pushButtonInfoMilonga.setToolTip(_translate("AudioPlayerDialog", "Give infos about milonga"))
        self.pushButtonSaveMilongaAs.setToolTip(_translate("AudioPlayerDialog", "save Milanga as"))
        self.pushButtonSaveMilonga.setToolTip(_translate("AudioPlayerDialog", "Save Milonga"))
        self.pushButtonSaveMilonga.setShortcut(_translate("AudioPlayerDialog", "Ctrl+S"))
        self.pushButtonDeleteMilonga.setToolTip(_translate("AudioPlayerDialog", "Delete this Milonga"))
        self.labelSizeDuration.setText(_translate("AudioPlayerDialog", "0 song    |    duration : 00:00    |    Milonga will end at 12:35"))
        self.menuFile.setTitle(_translate("AudioPlayerDialog", "File"))
        self.menuEdition.setTitle(_translate("AudioPlayerDialog", "Edition"))
        self.menuDisplay.setTitle(_translate("AudioPlayerDialog", "Display"))
        self.actionPreferences.setText(_translate("AudioPlayerDialog", "Preferences"))
        self.actionFullscreen.setText(_translate("AudioPlayerDialog", "Fullscreen"))
        self.actionFullscreen.setShortcut(_translate("AudioPlayerDialog", "F11"))
        self.actionDisplay_side_screen.setText(_translate("AudioPlayerDialog", "Display side screen"))
        self.actionDisplay_side_screen.setShortcut(_translate("AudioPlayerDialog", "Ctrl+F11"))
        self.actionImport_file.setText(_translate("AudioPlayerDialog", "Import file(s)"))
        self.actionImport_directory.setText(_translate("AudioPlayerDialog", "Import directory"))
        self.actionEdit_details_of_current_song.setText(_translate("AudioPlayerDialog", "Edit details of selected song(s)"))
        self.actionLoad_BPM_from_ID3_Tag.setText(_translate("AudioPlayerDialog", "Load BPM from ID3 Tag"))
        self.actionTap_yourself_BPM.setText(_translate("AudioPlayerDialog", "Tap yourself BPM"))

import djtango_rc
