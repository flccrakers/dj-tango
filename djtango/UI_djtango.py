# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/UI_djtango.ui'
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

class Ui_AudioPlayerDialog(object):
    def setupUi(self, AudioPlayerDialog):
        AudioPlayerDialog.setObjectName(_fromUtf8("AudioPlayerDialog"))
        AudioPlayerDialog.resize(1029, 599)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/logo-djtango.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AudioPlayerDialog.setWindowIcon(icon)
        AudioPlayerDialog.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(AudioPlayerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 300))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTypeSong = QtGui.QLabel(self.centralwidget)
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
        self.labelTypeSong.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    font-size: 40px;    \n"
"}"))
        self.labelTypeSong.setTextFormat(QtCore.Qt.AutoText)
        self.labelTypeSong.setScaledContents(False)
        self.labelTypeSong.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTypeSong.setObjectName(_fromUtf8("labelTypeSong"))
        self.horizontalLayout.addWidget(self.labelTypeSong)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelTitle = QtGui.QLabel(self.centralwidget)
        self.labelTitle.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    font-size: 22px;    \n"
"}"))
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelArtist = QtGui.QLabel(self.centralwidget)
        self.labelArtist.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}"))
        self.labelArtist.setObjectName(_fromUtf8("labelArtist"))
        self.horizontalLayout_3.addWidget(self.labelArtist)
        self.labelSep = QtGui.QLabel(self.centralwidget)
        self.labelSep.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    font-style: bold;\n"
"}"))
        self.labelSep.setObjectName(_fromUtf8("labelSep"))
        self.horizontalLayout_3.addWidget(self.labelSep)
        self.labelAlbum = QtGui.QLabel(self.centralwidget)
        self.labelAlbum.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-style: italic;\n"
"}"))
        self.labelAlbum.setObjectName(_fromUtf8("labelAlbum"))
        self.horizontalLayout_3.addWidget(self.labelAlbum)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.timeLabel = QtGui.QLabel(self.centralwidget)
        self.timeLabel.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    \n"
"}"))
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.horizontalLayout.addWidget(self.timeLabel)
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setStyleSheet(_fromUtf8("Phonon::SeekSlider::groove:horizontal{\n"
"    border: 1px solid white;\n"
"   height: 10px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: #2a2a2a;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"Phonon::SeekSlider::handle:horizontal {\n"
"    background: white;\n"
"    border: 3px solid #a0344d;\n"
"      width: 5px;\n"
"    \n"
"    margin: -2px -2px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 10px;\n"
"}\n"
"Phonon::SeekSlider::sub-page:horizontal {\n"
"    background: #a0344d; \n"
"    /*height: 8px;*/\n"
"    border: 1px solid white;\n"
"} \n"
"\n"
""))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayout.addWidget(self.seekSlider)
        self.playToolButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playToolButton.sizePolicy().hasHeightForWidth())
        self.playToolButton.setSizePolicy(sizePolicy)
        self.playToolButton.setMinimumSize(QtCore.QSize(0, 40))
        self.playToolButton.setMaximumSize(QtCore.QSize(40, 40))
        self.playToolButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.playToolButton.setStyleSheet(_fromUtf8("QPushButton#playToolButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/play-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playToolButton.setIcon(icon1)
        self.playToolButton.setIconSize(QtCore.QSize(40, 40))
        self.playToolButton.setObjectName(_fromUtf8("playToolButton"))
        self.horizontalLayout.addWidget(self.playToolButton)
        self.stopToolButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopToolButton.sizePolicy().hasHeightForWidth())
        self.stopToolButton.setSizePolicy(sizePolicy)
        self.stopToolButton.setMaximumSize(QtCore.QSize(40, 40))
        self.stopToolButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stopToolButton.setStyleSheet(_fromUtf8("QPushButton#stopToolButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
" "))
        self.stopToolButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/stop-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopToolButton.setIcon(icon2)
        self.stopToolButton.setIconSize(QtCore.QSize(40, 40))
        self.stopToolButton.setObjectName(_fromUtf8("stopToolButton"))
        self.horizontalLayout.addWidget(self.stopToolButton)
        spacerItem4 = QtGui.QSpacerItem(30, 21, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem5 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButtonRandom = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRandom.sizePolicy().hasHeightForWidth())
        self.pushButtonRandom.setSizePolicy(sizePolicy)
        self.pushButtonRandom.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRandom.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        self.pushButtonRandom.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/random-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRandom.setIcon(icon3)
        self.pushButtonRandom.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonRandom.setObjectName(_fromUtf8("pushButtonRandom"))
        self.horizontalLayout_5.addWidget(self.pushButtonRandom)
        self.pushButtonClearFilter = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClearFilter.sizePolicy().hasHeightForWidth())
        self.pushButtonClearFilter.setSizePolicy(sizePolicy)
        self.pushButtonClearFilter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonClearFilter.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        self.pushButtonClearFilter.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/clear-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClearFilter.setIcon(icon4)
        self.pushButtonClearFilter.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonClearFilter.setObjectName(_fromUtf8("pushButtonClearFilter"))
        self.horizontalLayout_5.addWidget(self.pushButtonClearFilter)
        self.comboBoxArtist = QtGui.QComboBox(self.centralwidget)
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.comboBoxArtist.setPalette(palette)
        self.comboBoxArtist.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBoxArtist.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBoxArtist.setStyleSheet(_fromUtf8("QComboBox\n"
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
"}"))
        self.comboBoxArtist.setEditable(True)
        self.comboBoxArtist.setObjectName(_fromUtf8("comboBoxArtist"))
        self.horizontalLayout_5.addWidget(self.comboBoxArtist)
        self.comboBoxAlbum = QtGui.QComboBox(self.centralwidget)
        self.comboBoxAlbum.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBoxAlbum.setStyleSheet(_fromUtf8("QComboBox\n"
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
"}"))
        self.comboBoxAlbum.setObjectName(_fromUtf8("comboBoxAlbum"))
        self.horizontalLayout_5.addWidget(self.comboBoxAlbum)
        self.comboBoxGenre = QtGui.QComboBox(self.centralwidget)
        self.comboBoxGenre.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBoxGenre.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBoxGenre.setStyleSheet(_fromUtf8("QComboBox\n"
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
"}"))
        self.comboBoxGenre.setFrame(True)
        self.comboBoxGenre.setObjectName(_fromUtf8("comboBoxGenre"))
        self.horizontalLayout_5.addWidget(self.comboBoxGenre)
        self.lineEditFilter = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFilter.sizePolicy().hasHeightForWidth())
        self.lineEditFilter.setSizePolicy(sizePolicy)
        self.lineEditFilter.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditFilter.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditFilter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditFilter.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    color:white;\n"
"    background:rgb(42,42,42);\n"
"    border-style: none;\n"
"\n"
"}"))
        self.lineEditFilter.setObjectName(_fromUtf8("lineEditFilter"))
        self.horizontalLayout_5.addWidget(self.lineEditFilter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.milongaSource = QtGui.QTableView(self.centralwidget)
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
        self.milongaSource.setStyleSheet(_fromUtf8("QTableView{\n"
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
""))
        self.milongaSource.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.milongaSource.setTabKeyNavigation(False)
        self.milongaSource.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.milongaSource.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.milongaSource.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.milongaSource.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.milongaSource.setShowGrid(False)
        self.milongaSource.setGridStyle(QtCore.Qt.NoPen)
        self.milongaSource.setSortingEnabled(True)
        self.milongaSource.setWordWrap(False)
        self.milongaSource.setCornerButtonEnabled(False)
        self.milongaSource.setObjectName(_fromUtf8("milongaSource"))
        self.milongaSource.horizontalHeader().setStretchLastSection(True)
        self.milongaSource.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.milongaSource)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.pushButtonHideDest = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonHideDest.sizePolicy().hasHeightForWidth())
        self.pushButtonHideDest.setSizePolicy(sizePolicy)
        self.pushButtonHideDest.setMaximumSize(QtCore.QSize(10, 16777215))
        self.pushButtonHideDest.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.pushButtonHideDest.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonHideDest.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"    border: none;\n"
" }\n"
""))
        self.pushButtonHideDest.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/hide-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonHideDest.setIcon(icon5)
        self.pushButtonHideDest.setIconSize(QtCore.QSize(10, 80))
        self.pushButtonHideDest.setObjectName(_fromUtf8("pushButtonHideDest"))
        self.horizontalLayout_4.addWidget(self.pushButtonHideDest)
        self.pushButtonHideSource = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonHideSource.sizePolicy().hasHeightForWidth())
        self.pushButtonHideSource.setSizePolicy(sizePolicy)
        self.pushButtonHideSource.setMaximumSize(QtCore.QSize(10, 16777215))
        self.pushButtonHideSource.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.pushButtonHideSource.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonHideSource.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
"    border: none;\n"
" }\n"
""))
        self.pushButtonHideSource.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/hide-left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonHideSource.setIcon(icon6)
        self.pushButtonHideSource.setIconSize(QtCore.QSize(10, 80))
        self.pushButtonHideSource.setObjectName(_fromUtf8("pushButtonHideSource"))
        self.horizontalLayout_4.addWidget(self.pushButtonHideSource)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButtonMilongaClear = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMilongaClear.sizePolicy().hasHeightForWidth())
        self.pushButtonMilongaClear.setSizePolicy(sizePolicy)
        self.pushButtonMilongaClear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonMilongaClear.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        self.pushButtonMilongaClear.setText(_fromUtf8(""))
        self.pushButtonMilongaClear.setIcon(icon4)
        self.pushButtonMilongaClear.setIconSize(QtCore.QSize(24, 28))
        self.pushButtonMilongaClear.setObjectName(_fromUtf8("pushButtonMilongaClear"))
        self.horizontalLayout_6.addWidget(self.pushButtonMilongaClear)
        self.labelMilongaName = QtGui.QLabel(self.centralwidget)
        self.labelMilongaName.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}"))
        self.labelMilongaName.setObjectName(_fromUtf8("labelMilongaName"))
        self.horizontalLayout_6.addWidget(self.labelMilongaName)
        self.pushButtonLoadMilonga = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLoadMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonLoadMilonga.setSizePolicy(sizePolicy)
        self.pushButtonLoadMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonLoadMilonga.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        self.pushButtonLoadMilonga.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/load-milonga-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLoadMilonga.setIcon(icon7)
        self.pushButtonLoadMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonLoadMilonga.setObjectName(_fromUtf8("pushButtonLoadMilonga"))
        self.horizontalLayout_6.addWidget(self.pushButtonLoadMilonga)
        self.pushButtonInfoMilonga = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInfoMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonInfoMilonga.setSizePolicy(sizePolicy)
        self.pushButtonInfoMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonInfoMilonga.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        self.pushButtonInfoMilonga.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/info-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonInfoMilonga.setIcon(icon8)
        self.pushButtonInfoMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonInfoMilonga.setObjectName(_fromUtf8("pushButtonInfoMilonga"))
        self.horizontalLayout_6.addWidget(self.pushButtonInfoMilonga)
        self.pushButtonSaveMilonga = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSaveMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonSaveMilonga.setSizePolicy(sizePolicy)
        self.pushButtonSaveMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonSaveMilonga.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        self.pushButtonSaveMilonga.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/save-milonga-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSaveMilonga.setIcon(icon9)
        self.pushButtonSaveMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonSaveMilonga.setObjectName(_fromUtf8("pushButtonSaveMilonga"))
        self.horizontalLayout_6.addWidget(self.pushButtonSaveMilonga)
        self.pushButtonDeleteMilonga = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteMilonga.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteMilonga.setSizePolicy(sizePolicy)
        self.pushButtonDeleteMilonga.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonDeleteMilonga.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2a2a2a;\n"
"    color: white;\n"
" }\n"
""))
        self.pushButtonDeleteMilonga.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/trash-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDeleteMilonga.setIcon(icon10)
        self.pushButtonDeleteMilonga.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonDeleteMilonga.setObjectName(_fromUtf8("pushButtonDeleteMilonga"))
        self.horizontalLayout_6.addWidget(self.pushButtonDeleteMilonga)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.labelSizeDuration = QtGui.QLabel(self.centralwidget)
        self.labelSizeDuration.setStyleSheet(_fromUtf8("QLabel{\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}"))
        self.labelSizeDuration.setObjectName(_fromUtf8("labelSizeDuration"))
        self.verticalLayout_8.addWidget(self.labelSizeDuration)
        self.milongaDest = QtGui.QTableView(self.centralwidget)
        self.milongaDest.setFocusPolicy(QtCore.Qt.NoFocus)
        self.milongaDest.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.milongaDest.setStyleSheet(_fromUtf8("QTableView{\n"
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
""))
        self.milongaDest.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.milongaDest.setProperty("showDropIndicator", True)
        self.milongaDest.setDragEnabled(True)
        self.milongaDest.setDragDropOverwriteMode(True)
        self.milongaDest.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.milongaDest.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.milongaDest.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.milongaDest.setShowGrid(False)
        self.milongaDest.setWordWrap(False)
        self.milongaDest.setCornerButtonEnabled(False)
        self.milongaDest.setObjectName(_fromUtf8("milongaDest"))
        self.verticalLayout_8.addWidget(self.milongaDest)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        AudioPlayerDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AudioPlayerDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdition = QtGui.QMenu(self.menubar)
        self.menuEdition.setObjectName(_fromUtf8("menuEdition"))
        self.menuDisplay = QtGui.QMenu(self.menubar)
        self.menuDisplay.setObjectName(_fromUtf8("menuDisplay"))
        AudioPlayerDialog.setMenuBar(self.menubar)
        self.actionPreferences = QtGui.QAction(AudioPlayerDialog)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionFullscreen = QtGui.QAction(AudioPlayerDialog)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setObjectName(_fromUtf8("actionFullscreen"))
        self.actionDisplay_side_screen = QtGui.QAction(AudioPlayerDialog)
        self.actionDisplay_side_screen.setCheckable(True)
        self.actionDisplay_side_screen.setSoftKeyRole(QtGui.QAction.SelectSoftKey)
        self.actionDisplay_side_screen.setIconVisibleInMenu(True)
        self.actionDisplay_side_screen.setObjectName(_fromUtf8("actionDisplay_side_screen"))
        self.actionImport_file = QtGui.QAction(AudioPlayerDialog)
        self.actionImport_file.setObjectName(_fromUtf8("actionImport_file"))
        self.actionImport_directory = QtGui.QAction(AudioPlayerDialog)
        self.actionImport_directory.setObjectName(_fromUtf8("actionImport_directory"))
        self.actionEdit_details_of_current_song = QtGui.QAction(AudioPlayerDialog)
        self.actionEdit_details_of_current_song.setObjectName(_fromUtf8("actionEdit_details_of_current_song"))
        self.actionLoad_BPM_from_ID3_Tag = QtGui.QAction(AudioPlayerDialog)
        self.actionLoad_BPM_from_ID3_Tag.setObjectName(_fromUtf8("actionLoad_BPM_from_ID3_Tag"))
        self.actionTap_yourself_BPM = QtGui.QAction(AudioPlayerDialog)
        self.actionTap_yourself_BPM.setObjectName(_fromUtf8("actionTap_yourself_BPM"))
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
        AudioPlayerDialog.setWindowTitle(_translate("AudioPlayerDialog", "DjTango", None))
        self.labelTypeSong.setText(_translate("AudioPlayerDialog", "-", None))
        self.labelTitle.setText(_translate("AudioPlayerDialog", "TextLabel", None))
        self.labelArtist.setText(_translate("AudioPlayerDialog", "NA", None))
        self.labelSep.setText(_translate("AudioPlayerDialog", "-", None))
        self.labelAlbum.setText(_translate("AudioPlayerDialog", "NA", None))
        self.timeLabel.setText(_translate("AudioPlayerDialog", "-", None))
        self.playToolButton.setToolTip(_translate("AudioPlayerDialog", "play / pause", None))
        self.playToolButton.setShortcut(_translate("AudioPlayerDialog", "Space", None))
        self.stopToolButton.setToolTip(_translate("AudioPlayerDialog", "stop", None))
        self.pushButtonClearFilter.setToolTip(_translate("AudioPlayerDialog", "clear the filters", None))
        self.lineEditFilter.setToolTip(_translate("AudioPlayerDialog", "Enter some text and type enter to filter", None))
        self.pushButtonMilongaClear.setToolTip(_translate("AudioPlayerDialog", "clear the milonga table (will not be saved)", None))
        self.labelMilongaName.setText(_translate("AudioPlayerDialog", "- No Milonga -", None))
        self.pushButtonLoadMilonga.setToolTip(_translate("AudioPlayerDialog", "Load Milonga", None))
        self.pushButtonLoadMilonga.setShortcut(_translate("AudioPlayerDialog", "Ctrl+O", None))
        self.pushButtonInfoMilonga.setToolTip(_translate("AudioPlayerDialog", "Give infos about milonga", None))
        self.pushButtonSaveMilonga.setToolTip(_translate("AudioPlayerDialog", "Save Milonga", None))
        self.pushButtonSaveMilonga.setShortcut(_translate("AudioPlayerDialog", "Ctrl+S", None))
        self.pushButtonDeleteMilonga.setToolTip(_translate("AudioPlayerDialog", "Delete this Milonga", None))
        self.labelSizeDuration.setText(_translate("AudioPlayerDialog", "0 song    |    duration : 00:00    |    Milonga will end at 12:35", None))
        self.menuFile.setTitle(_translate("AudioPlayerDialog", "File", None))
        self.menuEdition.setTitle(_translate("AudioPlayerDialog", "Edition", None))
        self.menuDisplay.setTitle(_translate("AudioPlayerDialog", "Display", None))
        self.actionPreferences.setText(_translate("AudioPlayerDialog", "Preferences", None))
        self.actionFullscreen.setText(_translate("AudioPlayerDialog", "Fullscreen", None))
        self.actionFullscreen.setShortcut(_translate("AudioPlayerDialog", "F11", None))
        self.actionDisplay_side_screen.setText(_translate("AudioPlayerDialog", "Display side screen", None))
        self.actionDisplay_side_screen.setShortcut(_translate("AudioPlayerDialog", "Ctrl+F11", None))
        self.actionImport_file.setText(_translate("AudioPlayerDialog", "Import file(s)", None))
        self.actionImport_directory.setText(_translate("AudioPlayerDialog", "Import directory", None))
        self.actionEdit_details_of_current_song.setText(_translate("AudioPlayerDialog", "Edit details of selected song(s)", None))
        self.actionLoad_BPM_from_ID3_Tag.setText(_translate("AudioPlayerDialog", "Load BPM from ID3 Tag", None))
        self.actionTap_yourself_BPM.setText(_translate("AudioPlayerDialog", "Tap yourself BPM", None))

from PyQt4 import phonon
import djtango_rc
