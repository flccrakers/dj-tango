#!/usr/bin/python3
# -*- coding:Utf-8 -*-
import pdb
from djtango.UI_djtango import Ui_AudioPlayerDialog
from djtango.UI_details import Ui_details
from djtango.UI_infos import Ui_infos
from djtango.UI_preferences import Ui_preferences
from djtango.UI_selectmilonga import Ui_selectmilonga
from djtango.UI_milongaName import Ui_DialogMilongaName
from djtango.UI_askDelete import Ui_DialogAskDelete
from djtango.UI_sideDisplay import Ui_sideDisplay
from djtango.UI_tapbpm import Ui_tapDialog
from djtango.UI_infosMilonga import Ui_infosMilonga
from djtango.form import Ui_Form
from djtango.tangosong import TangoSong
from djtango.dirsong import dirSong
from djtango.data import djDataConnection
from djtango.circularprogressbar import QRoundProgressBar
from djtango import tableModels
from djtango import utils
from djtango.dirscanningthread import dirScan

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import QApplication
# from PyQt5.Qt import QList
from PyQt5.Qt import QDesktopWidget
from PyQt5.Qt import QThread
from PyQt5.Qt import pyqtSignal
# from PyQt5.Qt import SIGNAL
from PyQt5.Qt import QFileDialog
from PyQt5.Qt import QIcon
from PyQt5.Qt import QAction
from PyQt5.Qt import QAbstractTableModel
from PyQt5.Qt import QAbstractItemView
from PyQt5.Qt import QHeaderView
from PyQt5.Qt import QColorDialog
from PyQt5.Qt import QSortFilterProxyModel
from mutagen.mp3 import MP3

from PyQt5.QtMultimedia import (QMediaPlayer, QMediaContent)

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui

import os, sys, time, threading, operator, re, audioread, platform

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class InfoThreading(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self)
        self.exiting = False
        self.timelaps = 5

    def __del__(self):
        # print ("exiting")
        self.exiting = True
        self.wait()

    def render(self, timelaps):
        self.timelaps = timelaps
        self.start()

    def run(self):
        now = time.time()
        # time.sleep(1)
        while time.time() - now < self.timelaps:
            time.sleep(1)


class MyTimer:
    def __init__(self, tempo, target, args=[], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)

    def start(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()


class AudioPlayerDialog(QMainWindow, QObject):
    tangoListUpdated = pyqtSignal(dirSong)
    workingOnNewfileStatus = pyqtSignal(bool)

    def __init__(self):
        QMainWindow.__init__(self)

        self.bpm = 0

        self.tapTable = []
        self.info_thread = InfoThreading()

        self.mediaSource = None

        self.djhome = os.path.join(os.path.expanduser("~"), ".djtango")
        print('DJ_HOME_PATH: ' + self.djhome)

        self.addedEffects = {}
        self.effectsDict = {}
        self.curTango = None
        self.curLibraryRow = 0
        self.djData = djDataConnection(self.djhome)

        self.curTangoEditingIndexes = []
        self.curTangoEditing = 0  # a index telling wich is the current tango idited in properties window
        self.volumeSetToInitial = True

        self.infoMilongaSentence = ''

        # print(mime_types)

        self._isPlaying = False
        self._isPaused = False
        self._isMilongaPlaying = False
        self._startMilongaTimeStamp = 0
        self._curMilongaLine = 0
        self._isClicked = False  # to be sure to do nothing on changing state if it's clicked
        self._currentIndex = 0

        # Initialize some other variables.
        self._filePath = ''
        self._dialog = None

        # self.mediaObj = phonon.Phonon.MediaObject(self)
        self.player = QMediaPlayer()
        # self.mediaObj.setTickInterval(250)
        # self.audioSink = Phonon.AudioOutput(Phonon.MusicCategory, self)
        # self.audioSink.setVolume(1)
        # self.audioPath = Phonon.createPath(self.mediaObj, self.audioSink)
        self.firstTime = False

        # the circular progress bar

        pbPalette = QPalette()
        pbPalette.setColor(QPalette.Base, QtGui.QColor.fromRgb(42, 42, 42))
        pbPalette.setColor(QPalette.Highlight, QtGui.QColor.fromRgb(160, 52, 77))
        pbPalette.setColor(QPalette.Window, QtGui.QColor.fromRgb(160, 52, 77, 0))
        pbPalette.setColor(QPalette.AlternateBase, QtGui.QColor.fromRgb(160, 52, 77, 0))
        pbPalette.setColor(QPalette.Shadow, QtGui.QColor.fromRgb(160, 52, 77, 0))
        pbPalette.setColor(QPalette.Text, QtGui.QColor.fromRgb(255, 255, 255))

        self.bar = QRoundProgressBar()
        self.bar.setPalette(pbPalette)
        self.bar.setFixedSize(140, 140)
        self.bar.setDataPenWidth(10)
        self.bar.setOutlinePenWidth(3)
        self.bar.setDonutThicknessRatio(0.7)
        self.bar.setDecimals(1)
        self.bar.setFormat('%t')
        # self.bar.resetFormat()
        self.bar.setNullPosition(90)
        self.bar.setBarStyle(QRoundProgressBar.StyleDonut)
        # self.bar.setBarStyle(QRoundProgressBar.StyleLine)
        # self.bar.setDataColors([(0., QtGui.QColor.fromRgb(255,0,0)), (0.5, QtGui.QColor.fromRgb(255,255,0)), (1., QtGui.QColor.fromRgb(0,255,0))])
        self.bar.setDataColors([(1., QtGui.QColor.fromRgb(160, 52, 77)), ])
        # self.bar.setBackgroundColor(QtGui.QColor.fromRgb(160,52,77,0))

        self.bar.setRange(0, 100)
        self.bar.setValue(75)

        # end of progress barr

        if not os.path.exists(self.djData.path):
            print("it's the first time, will create the database")
            self.djData.createDatabase()
            self.firstTime = True
            # self._tangoList.fillListOfFile()

        # print (self._tangoList.tangos[1].type)
        self.TYPE = self.djData.getTangoTypeList()

        # Tt = TANGO = 1, VALS = 2, MILONGA = 3, CORTINA = 4, UNKNOWN=5
        # print (self.TYPE[1])
        prop = self.djData.getPreferences()

        self.audioPath = prop['path']
        self.durationFadOut = prop['fadoutTime'] * 1000  # in ms
        self.FadOutTime = prop['cortinaDuration'] * 1000  # in ms, to get form the database
        self.writeTag = prop['writeTag']
        self.normalize = prop['normalize']
        self.stepFadOut = self.durationFadOut / self.player.notifyInterval()
        self.duration = 0

        # print("AUDIO PATH IN INITIALIZING DATA : "+self.audioPath)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 52, 77, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        if self.firstTime:
            introDialog = QMessageBox()
            # introDialog.setPalette(palette)
            introDialog.setStyleSheet(
                "QDialog{\n""background-color: rgb(42,42,42); color:white\n""}QPushButton {\n""background-color: #2a2a2a;\n""color: white;\noutline: none\n""}QLabel {\n""background-color: #2a2a2a;\n""color: white;\n""}")
            introDialog.setWindowTitle("First time user ?")
            # introDialog = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel);
            introDialog.setText(
                "Hi, I'm DJ-Tango and it appear that is the first time you use me. \nPlease select the directory where all your Tango are stored.");
            introDialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel);
            # introDialog.setModal(True)
            introDialog.setDefaultButton(QMessageBox.Ok);
            # introDialog.button(QMessageBox.Cancel).setDefault(False)
            # for button in introDialog.StandardButtons():
            #    button.setFocusPolicy(setFocusPolicy(QtCore.Qt.NoFocus))
            # introDialog.
            # res = introDialog.exec()
            # print (res)
            if introDialog.exec() == QMessageBox.Ok:
                self.audioPath = QFileDialog.getExistingDirectory(self, "Open Tango directory", os.path.expanduser('~'),
                                                                  QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks);
                self.djData.updateSongPath(self.audioPath)
                time.sleep(0.3)
            else:
                sys.exit(0)
        progressBar = QProgressDialog("Scanning dir and analyzing the songs...", "Abort", 0, 100, self)
        progressBar.setWindowTitle("Inporting Tangos in the database and set tags")
        progressBar.setWindowModality(Qt.WindowModal);
        progressBar.setStyleSheet(
            "QDialog{\n""background-color: rgb(42,42,42); color:white\n""}"
            "QPushButton {\n""background-color: #2a2a2a;\n""color: white;\noutline: none\n""}"
            "QLabel {\n""background-color: #2a2a2a;\n""color: white;\n""}"
            "QProgressBar {\n""border: 2px solid grey; border-radius: 5px;  background-color: #2a2a2a; color: white; text-align: center""}"
            "QProgressBar::chunk {""background-color: #a0344d;" "width: 20px;""}")
        progressBar.reset()
        self._tangoList = dirSong(self.audioPath, self.firstTime, progressBar, self.djData)
        progressBar.reset()
        # self.firstTime = False
        if not self.firstTime:
            self._tangoList.loadTangos(self.djData.getAllTangos())

        self.curTango = None
        self.scanningDir = False
        # self.dirthread = MyTimer(20, self.scannDir, ["test"])

        self.scanner = dirScan(self._tangoList, self.djData)
        self.dirthread2 = QThread()
        self.scanner.moveToThread(self.dirthread2)

        # j'ai modifié
        # Create self._dialog instance and call
        # necessary methods to create a user interface
        self._createUI()

        # Connect slots with signals.
        self._connect()

        # Create the shortcuts
        self._createShorcuts()

        # launch the worer threads
        print("starting directory scanning")
        self.dirthread2.start()

        # Show the Audio player.
        self.show()

    def _createShorcuts(self):
        print("creating shortcuts")
        _translate = QtCore.QCoreApplication.translate

        playSourceOnEnter = QShortcut(self._dialog.milongaSource)
        playSourceOnEnter.setContext(Qt.WidgetShortcut)
        playSourceOnEnter.setKey(QtCore.Qt.Key_Return)
        playSourceOnEnter.activated.connect(self.playSelectedSource)
        # playSourceOnEnter = QShortcut(QKeySequence(QKeySequence.InsertParagraphSeparator), self._dialog.milongaSource);
        # playSourceOnEnter.setContext(Qt.WidgetShortcut)
        # playSourceOnEnter.activated.connect(self.playSelectedSource)

        # playSourceOnSpace = QShortcut(QKeySequence(QKeySequence.InsertParagraphSeparator), self._dialog.milongaSource);
        # playSourceOnSpace.setContext(Qt.WidgetShortcut)
        # playSourceOnSpace.activated.connect(self.playSelectedSource)

        displaySideWindowOnCrtlF11 = QShortcut(self)
        displaySideWindowOnCrtlF11.setContext(Qt.WidgetShortcut)
        displaySideWindowOnCrtlF11.setKey(QtCore.Qt.CTRL + QtCore.Qt.Key_F11)
        displaySideWindowOnCrtlF11.activated.connect(self._handelDisplaySideScreen)

        fullScreenOnF11 = QShortcut(self)
        fullScreenOnF11.setContext(Qt.WidgetShortcut)
        fullScreenOnF11.setKey(QtCore.Qt.Key_F11)
        fullScreenOnF11.activated.connect(self._handelFullScren)

        # fullScreenOnF11 = QShortcut(QKeySequence(Qt.Key_F11))
        # self.shortcut.activated.connect(self._handelFullScren)

    def scannDir(unstr, nimp):

        # print("Currently scanning ? "+str(unstr.scanningDir))

        if not unstr.scanningDir:
            unstr.scanningDir = True
            newfiles = unstr._tangoList.checkNewFiles()
            # print(newfiles)
            if newfiles:
                # lastindex = unstr.sourceModel.rowCount(QModelIndex())
                # print("last index: "+str(lastindex))
                for path in newfiles:
                    # insert automatiquement un nouveau fichier et met à jour la liste
                    unstr.djData.insertTango(TangoSong(path, 0, True))

                unstr._tangoList.loadTangos(unstr.djData.getAllTangos())

                data = []
                for key in unstr._tangoList.tangos.keys():
                    tango = unstr._tangoList.tangos[key]
                    data.append(tango.list())
                unstr.sourceModel.changeData(data)
                unstr._showInfo(str(len(newfiles)) + " song has been added")

            unstr.scanningDir = False
            # TODO UPDATE THE DATA MODEL
            # self.djData.setNewSongAvailable(True)

    def _createUI(self):
        """
        Create self._dialog using the class Ui_AudioPlayerDialog.
        Tweak some UI elements
        """
        self._dialog = Ui_AudioPlayerDialog()
        self._dialog.setupUi(self)
        self._dialog.retranslateUi(self)
        self.playIcon = QIcon("./djtango/img/play-button.png")
        self.pauseIcon = QIcon("./djtango/img/pause-button.png")

        # self._dialog.seekSlider.setMediaObject(self.mediaObj)
        # self._dialog.volumeSlider.setAudioOutput(self.audioSink)

        self.colorDialog = QColorDialog()
        self.colorDialog.setOption(QColorDialog.ShowAlphaChannel, True)
        self.colorDialog.setWindowModality(Qt.WindowModal)

        libraryHeader = ['#', ' ', 'Title', 'Artist', 'Album', 'Genre', 'Year', 'BPM', 'Time']
        liraryMilongaHeader = ['#', ' ', 'Title', 'Artist', 'Album', 'Genre']
        # MilongaDestHeader = ['#', Title]
        libraryData = []
        sourceData = []
        destData = []
        # print (self._tangoList.tangos[1554].duration)
        for key in self._tangoList.tangos.keys():
            tango = self._tangoList.tangos[key]
            libraryData.append(tango.list())
        # print (self._tangoList.tangos[1554].duration)

        # model for the milonga library
        self.sourceModel = tableModels.milongaSource(self, libraryData, libraryHeader, self.TYPE)
        self.sourceProxyModel = tableModels.sourceFilterProxyModel(self)
        self.sourceProxyModel.setSourceModel(self.sourceModel)
        self._dialog.milongaSource.setModel(self.sourceProxyModel)
        self._dialog.milongaSource.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.destModel = tableModels.milongaDest(self, [], libraryHeader, self.TYPE)
        self._dialog.milongaDest.setModel(self.destModel)
        self._dialog.milongaDest.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self._dialog.labelsongNB_source.setText(str(self.sourceProxyModel.rowCount(QModelIndex())) + " song(s)");

        # create windows for tap counting

        self.tapWindow = QWidget()
        self.tapContent = Ui_tapDialog()
        self.tapContent.setupUi(self.tapWindow)

        # create windows for properties edition
        self.propWindow = QWidget()
        self.detailsContent = Ui_details()
        self.detailsContent.setupUi(self.propWindow)
        self.propWindow.setWindowFlags(Qt.FramelessWindowHint)
        for i in range(1, len(self.TYPE) + 1):
            self.detailsContent.comboBoxTangoType.insertItem(i - 1, self.TYPE[i][1].title())

        self.sideWindow = QWidget()
        self.sideContent = Ui_sideDisplay()

        self.sideContent.setupUi(self.sideWindow)
        self.sideContent.PBLayout.addWidget(self.bar)
        # self.sideContent.lcdNumber.setVisible(True)
        # self.sideWindow.grabShortcut(QKeySequence(tr("Ctrl+F11")),  Qt.WidgetShortcut)

        # self.shortcut

        # create window for infos
        self.infoWindow = QWidget()
        self.infoContent = Ui_infos()
        self.infoContent.setupUi(self.infoWindow)
        self.infoWindow.setWindowFlags(Qt.FramelessWindowHint)

        # create window for infosMilonga
        self.infoMilongaWindow = QWidget()
        self.infoMilongaContent = Ui_infosMilonga()
        self.infoMilongaContent.setupUi(self.infoMilongaWindow)
        self.infoMilongaWindow.setWindowFlags(Qt.FramelessWindowHint)

        # create the Qdialog for milonga list
        self.selectMilongaListWindow = QDialog()
        self.selectMilongaListContent = Ui_selectmilonga()
        self.selectMilongaListContent.setupUi(self.selectMilongaListWindow)

        self.milongaNameWindow = QDialog()
        self.milongaNameContent = Ui_DialogMilongaName()
        self.milongaNameContent.setupUi(self.milongaNameWindow)

        self.milongaAskDelete = QDialog()
        self.milongaAskDeleteContent = Ui_DialogAskDelete()
        self.milongaAskDeleteContent.setupUi(self.milongaAskDelete)

        # create the preferences window
        self.prefWindow = QDialog()
        self.prefContent = Ui_preferences()
        self.prefContent.setupUi(self.prefWindow)
        self.prefContent.lineEditSongDir.setText(self.audioPath)
        self.prefContent.spinBoxFadeOut.setValue(self.durationFadOut / 1000)
        self.prefContent.spinBoxCortinaDuration.setValue(self.FadOutTime / 1000)
        self.prefContent.checkBoxWriteTags.setCheckState(self.writeTag)
        self.prefContent.checkBoxNormalize.setCheckState(self.normalize)
        for i in self.TYPE.keys():
            self.prefContent.listWidgetTangoType.insertItem(i - 1, self.TYPE[i][1])
            R = self.TYPE[i][2]
            G = self.TYPE[i][3]
            B = self.TYPE[i][4]
            T = self.TYPE[i][5]
            # print (T)
            self.colorDialog.setCustomColor(i, QColor(R, G, B, T))

        self.setListOfType()
        self.setListOfArtist()
        self.setListOfAlbum()

    def closeEvent(self, evt):
        """
        Overrides QMainWindow.closeEvent.
        """
        # if self.mediaObj:
        #    self.mediaObj.stop()
        self.player.stop()

        # self.mediaObj = None
        # self._clearEffectsObjects()
        self.infoWindow.close()
        self.prefWindow.close()
        self.sideWindow.close()
        # self.dirthread.stop()
        self.dirthread2.terminate()

        QMainWindow.closeEvent(self, evt)

    @pyqtSlot(list, list)
    def done(self, datas, tangos):

        # print ("IN DONE")
        # print (len(datas))
        self.workingOnNewfileStatus.emit(True)
        # datas = newfiles[0]
        # tangos = newfiles[1]
        for tango in tangos:
            self._tangoList.addTango(tango)  # add a Tango with only the path
        self.sourceModel.addNewData(datas)  # update the table
        self._showInfo(str(len(tangos)) + " song has been added")
        self.workingOnNewfileStatus.emit(False)

    def _connect(self):
        """
        Connect slots with signals.
        """
        # self.dirthread2.finished.connect(self.done)
        self.dirthread2.started.connect(self.scanner.workOut)
        self.scanner.scanned.connect(self.done)

        self._dialog.actionPreferences.triggered.connect(self._handelPrefClose)

        self._dialog.actionFullscreen.triggered.connect(self._handelFullScren)

        self._dialog.actionDisplay_side_screen.setChecked(False)
        self._dialog.actionDisplay_side_screen.triggered.connect(self._handelDisplaySideScreen)

        # self.connect(self._dialog.fileExitAction,
        #             SIGNAL("triggered()"),
        #             self.close)

        # self.connect(self._dialog.menuAudioEffects,
        #             SIGNAL("triggered(QAction*)"),
        #             self._changeAudioEffects)

        # self._dialog.milongaSource.horizontalHeader().sectionAutoResize.connect(self.sourceResize)
        # self._dialog.milongaSource.horizontalHeader().sectionResized.connect(self.sourceResized)
        self._dialog.milongaSource.resizeEvent = self.resizeHeaderSource

        self.destModel.dataChanged.connect(self.updateMilongaInfos)
        self.destModel.rowsRemoved.connect(self.updateMilongaInfos)

        self.tapContent.tapButton.pressed.connect(self._handelBpmTapping)
        self.tapContent.validate.clicked.connect(self._handelValidatebpm)
        self.tapContent.cancel.clicked.connect(self._handelCancelbpm)
        self.tapContent.next.clicked.connect(self._handelTapingNext)
        self.tapContent.previous.clicked.connect(self._handelTapingPrevious)

        self.prefContent.addTypeButton.clicked.connect(self._addTangoType)
        self.prefContent.removeTypeButton.clicked.connect(self._removeTangoType)
        self.prefContent.selectColorButton.clicked.connect(self.colorDialog.show)
        self.prefContent.listWidgetTangoType.currentRowChanged.connect(self._selectTangoChange)
        # self.prefContent.lineEditSongDir.clicked.connect(self.openFileDialog)
        # self.prefContent.lineEditSongDir.cursorPositionChanged.connect(self.openFileDialog)
        self.prefContent.pushButtonSelectPath.clicked.connect(self.open_file_dialog)
        # self.colorDialog

        self.colorDialog.accepted.connect(self._selectTangoColor)
        # self.connect(self.colorDialog, SIGNAL("accepted()"), self._selectTangoColor)

        # self.connect(self.prefContent.closeButtonPref, SIGNAL("clicked()"), self._handelPrefClose)

        self.info_thread.finished.connect(self.closeInfo)
        # self.infothread.terminated.connect(self.closeIngo)
        # self.connect(self.infothread, SIGNAL("finished()"), self.closeInfo)
        # self.connect(self.infothread, SIGNAL("terminated()"), self.closeInfo)

        self._dialog.playToolButton.clicked.connect(self._handelPlayPause)

        self._dialog.lineEditFilter.returnPressed.connect(self._handelFilterChange)
        self._dialog.pushButtonRandom.clicked.connect(self.sourceModel.randomize)

        self._dialog.milongaDest.pressed.connect(self.destModel.pressed)

        self.infoContent.pushButtonClose.clicked.connect(self.closeInfo)

        self.detailsContent.closeButton.clicked.connect(self._handlePropWindowClose)

        self.detailsContent.nextButton.clicked.connect(self._handlePropWindowNext)

        self.detailsContent.previousButton.clicked.connect(self._handlePropWindowPrevious)

        # self.mediaObj.tick.connect(self._handleTick)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.positionChanged.connect(self.position_changed)
        self.player.stateChanged.connect(self._handelStateChanged)

        self._dialog.songSlider.sliderMoved.connect(self.seek)
        # self._dialog.songSlider.actionTriggered.connect(self.sliderAction)

        self._dialog.songSlider.valueChanged.connect(self.sliderValueChanged)

        self._dialog.pushButtonHideSource.clicked.connect(self._handelHideSource)
        self._dialog.pushButtonHideDest.clicked.connect(self._handelHideDest)

        self._dialog.milongaSource.doubleClicked.connect(self._libraryClicked)
        self._dialog.milongaDest.doubleClicked.connect(self._destLibraryClicked)

        # self.mediaObj.stateChanged.connect(self._handleStateChanged)

        # the context menu for the library
        self._dialog.milongaSource.customContextMenuRequested.connect(self.popupLibrary)
        self._dialog.milongaDest.customContextMenuRequested.connect(self.popupMilonga)

        self._dialog.stopToolButton.clicked.connect(self._stopMedia)

        self._dialog.comboBoxArtist.currentIndexChanged.connect(self._handelFilterChange)
        self._dialog.comboBoxAlbum.currentIndexChanged.connect(self._handelFilterChange)
        self._dialog.comboBoxGenre.currentIndexChanged.connect(self._handelFilterChange)
        self._dialog.pushButtonClearFilter.clicked.connect(self._clearFilter)

        self._dialog.pushButtonSaveMilonga.clicked.connect(self._saveMilonga)
        self._dialog.pushButtonSaveMilongaAs.clicked.connect(self._saveMilongaAs)
        self._dialog.pushButtonDeleteMilonga.clicked.connect(self._deleteMilonga)
        self._dialog.pushButtonLoadMilonga.clicked.connect(self._loadMilonga)
        self._dialog.pushButtonMilongaClear.clicked.connect(self._clearMilonga)

        self._dialog.pushButtonInfoMilonga.clicked.connect(self._showInfoMilonga)

        self.infoMilongaContent.pushButtonClose.clicked.connect(self.closeInfoMilonga)

        self.selectMilongaListContent.listWidgetMilongas.doubleClicked.connect(self._doubleClickedMilongaSelect)

    def _handelStateChanged(self):

        # print("state: "+str(self.player.state()))
        if self.player.state() == QMediaPlayer.PlayingState:
            self._isClicked = False
        elif self.player.state() == QMediaPlayer.StoppedState:

            if not self._isClicked and self._isPlaying:
                # print("will play the next song")
                # self.clearPlayingCursor()

                if self._isMilongaPlaying:
                    if self._dialog.checkBoxLetCortinaUntilEnd.isChecked():
                        # remove the checked state
                        self._dialog.checkBoxLetCortinaUntilEnd.setCheckState(False)
                    self.play_next_milonga_song()
                else:
                    self.playNextLibrarySong()

    def durationChanged(self, duration):
        # print("dans durationChanged")
        self.bar.setRange(0, duration)
        duration /= 1000
        # print(str(duration*1000)+" "+str(self.curTango.duration))

        self.duration = duration

        self._dialog.songSlider.setMaximum(duration)
        if (not self.curTango.duration == duration * 1000) and (duration > 0):
            # print ("duration: "+str(self.curTango.duration)+" time in mediaObj: "+str(self.mediaObj.totalTime()))
            self.curTango.duration = duration * 1000

            if self._isMilongaPlaying:
                indexes = self._dialog.milongaDest.selectionModel().selectedRows()
                tangoID = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)
            else:
                indexes = self._dialog.milongaSource.selectionModel().selectedRows()
                tangoID = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)

                data = self._tangoList.tangos[tangoID].list()
                # data[8] = utils.msecToms(data[8])
                count = 0
                for cdata in data:
                    index = self.sourceProxyModel.index(indexes[0].row(), count)
                    self.sourceProxyModel.setData(index, cdata, Qt.EditRole)
                    count += 1

            self.djData.updateTango(self.curTango)

    def position_changed(self, progress):
        slider_progress = progress / 1000
        if not self._dialog.songSlider.isSliderDown():
            self._dialog.songSlider.setValue(slider_progress)
            self._dialog.timeLabel.setText(str(utils.msecToms(progress)) + " / " + str(utils.msecToms(self.duration)))

        if not self.curTango.type == 4 or not self.volumeSetToInitial or self._dialog.checkBoxLetCortinaUntilEnd.isChecked():
            self.player.setVolume(100)
            # print("case 1")
            self.volumeSetToInitial = True
            self.bar.setValue(self.duration * 1000 - progress * 1000)
            print(progress, self.curTango.tend)
            if progress >= self.curTango.tend:
                self.play_next_tango()
                print("It's time to stop / I should put a timer here to wait ")
        elif self.curTango.type == 4 and not self._dialog.checkBoxLetCortinaUntilEnd.isChecked():
            # print("case 2")
            self.bar.setRange(0, self.FadOutTime)  # set the maximum value of the circular progress bar
            self.bar.setValue(self.FadOutTime - progress)
            if (self.FadOutTime - self.durationFadOut) <= progress:
                if self.player.volume() > 1:
                    self.player.setVolume(self.player.volume() - 100 / self.stepFadOut)
                if self.player.volume() <= 1 and progress >= self.FadOutTime:
                    self.volumeSetToInitial = False
                    self.player.stop()
                    self.player.setVolume(100)
        # elif self._dialog.checkBoxLetCortinaUntilEnd.isChecked():
        # print("case 3")
        #  self.player.setVolume(100)

    def seek(self, seconds):
        self.player.setPosition(seconds * 1000)

    def sliderValueChanged(self, newpos):
        btns = QApplication.mouseButtons();
        localMousePos = self._dialog.songSlider.mapFromGlobal(QCursor.pos())

        clickOnSlider = btns == Qt.LeftButton and (
                localMousePos.x() >= 0 and localMousePos.y() >= 0 and localMousePos.x() < self._dialog.songSlider.size().width() and localMousePos.y() < self._dialog.songSlider.size().height())
        # print(clickOnSlider)
        if clickOnSlider:
            posRatio = localMousePos.x() / self._dialog.songSlider.size().width()
            slideRange = self._dialog.songSlider.maximum() - self._dialog.songSlider.minimum()
            sliderPosUnderMouse = self._dialog.songSlider.minimum() + slideRange * posRatio
            if not sliderPosUnderMouse == newpos:
                self._dialog.songSlider.setValue(sliderPosUnderMouse)
                self.seek(sliderPosUnderMouse)

    def resizeHeaderSource(self, event):
        sizeList = {}
        sizeList['#'] = 50
        sizeList['play'] = 35
        sizeList['genre'] = 120

        sizeList['year'] = 50
        sizeList['bpm'] = 50
        sizeList['duration'] = 50

        total = 0
        for key in sizeList.keys():
            total += sizeList[key]
        tableSize = self._dialog.milongaSource.width()
        # print ("total: "+str(total))
        # print("size of table: "+str(tableSize))
        size = (tableSize - total - 20) / 3  # size of the scroll

        self._dialog.milongaSource.horizontalHeader().resizeSection(0, sizeList['#'])
        self._dialog.milongaSource.horizontalHeader().resizeSection(1, sizeList['play'])

        self._dialog.milongaSource.horizontalHeader().resizeSection(2, size)
        self._dialog.milongaSource.horizontalHeader().resizeSection(3, size)
        self._dialog.milongaSource.horizontalHeader().resizeSection(4, size)

        self._dialog.milongaSource.horizontalHeader().resizeSection(5, sizeList['genre'])
        self._dialog.milongaSource.horizontalHeader().resizeSection(6, sizeList['year'])
        self._dialog.milongaSource.horizontalHeader().resizeSection(7, sizeList['bpm'])
        self._dialog.milongaSource.horizontalHeader().resizeSection(8, sizeList['duration'])

        # print("size of table: "+str(self._dialog.milongaSource.width()))

    ##########################################################################################
    #
    # Function to deal with the properties of Tangos,
    #
    ##########################################################################################
    def enableTableView(self):
        self._dialog.milongaSource.setSelectionMode(QAbstractItemView.ExtendedSelection)
        pass

    def disabledTableView(self):
        self._dialog.milongaSource.setSelectionMode(QAbstractItemView.NoSelection)
        pass

    def _handlePropWindowClose(self):
        # print ("about to close the window")
        self.updateTangoSong()
        self.TangoBeforeChange = self._tangoList.tangos[self.curTangoEditing]
        self.propWindow.close()
        self._dialog.milongaSource.setSortingEnabled(True)
        self.enableTableView()
        self.scanningDir = False
        self._dialog.labelsongNB_source.setText(str(self.sourceProxyModel.rowCount(QModelIndex())) + " song(s)");
        # self._dialog.milongaSource.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self._dialog.milongaSource.setEditTriggers(QAbstractItemView.AllEditTriggers)
        # self.setListOfArtist()
        # self.setListOfAlbum()

    def _handlePropWindowNext(self):
        self.enableTableView()
        self.updateTangoSong()
        self.TangoBeforeChange = self._tangoList.tangos[self.curTangoEditing]

        # print ("current row: "+str(self.curLibraryRow+1)+" total row: "+str(self.sourceProxyModel.rowCount(self)))
        if self.curLibraryRow + 1 < self.sourceProxyModel.rowCount(QModelIndex()):
            self.curLibraryRow += 1
            index = self.sourceProxyModel.index(self.curLibraryRow, 0)
            self.curTangoEditing = self.sourceProxyModel.data(index, Qt.DisplayRole)
            self._dialog.milongaSource.selectRow(self.curLibraryRow)
            self.updateTangoProp()
        self._dialog.labelsongNB_source.setText(str(self.sourceProxyModel.rowCount(QModelIndex())) + " song(s)");
        self.disabledTableView()
        self.scanningDir = True

    def _handlePropWindowPrevious(self):
        self.enableTableView()
        self.updateTangoSong()
        if self.curLibraryRow > 0:
            self.curLibraryRow -= 1
            self._dialog.milongaSource.selectRow(self.curLibraryRow)
            index = self.sourceProxyModel.index(self.curLibraryRow, 0)
            self.curTangoEditing = self.sourceProxyModel.data(index, Qt.DisplayRole)
            self.updateTangoProp()
        self.disabledTableView()
        self.scanningDir = True
        self._dialog.labelsongNB_source.setText(str(self.sourceProxyModel.rowCount(QModelIndex())) + " song(s)");

    def deleteTangos(self, removeFile=False):
        indexes = self._dialog.milongaSource.selectionModel().selectedRows()
        for index in indexes:
            # print(index.column())
            curTangoID = self.sourceProxyModel.data(index, Qt.DisplayRole)
            # print(str(curTangoID))
            # ask for confirmation (do it later)
            # delete entry in database
            self.djData.deleteTango(curTangoID)

            # detete the real file
            if os.path.isfile(self._tangoList.tangos[curTangoID].path) and removeFile:
                os.remove(self._tangoList.tangos[curTangoID].path)

            # delete tango in _tangoList.tangos
            if curTangoID in self._tangoList.tangos.keys():
                self._tangoList.removeTango(curTangoID)
                self.tangoListUpdated.emit(self._tangoList)
                # print ("tango removed from tangoList")

        # update the table model
        data = []
        for key in self._tangoList.tangos.keys():
            tango = self._tangoList.tangos[key]
            data.append(tango.list())
        self.sourceModel.changeData(data)
        self._dialog.labelsongNB_source.setText(str(self.sourceProxyModel.rowCount(QModelIndex())) + " song(s)");
        # self._dialog.labelsongNB_source.setText(self._dialog.milongaSource.sourceData.rowCount());
        # self.sourceModel.changeData(data)

    def handelOpenPropWidow(self):
        self.disabledTableView()
        self._dialog.milongaSource.setSortingEnabled(False)
        self.updateTangoProp()
        self.TangoBeforeChange = self._tangoList.tangos[self.curTangoEditing]
        self.propWindow.show()
        self.scanningDir = True

    def popupLibrary(self, pos):
        menu = QMenu()
        detailsAction = menu.addAction("Details")
        audacityAction = menu.addAction("Open with audacity")
        deleteAction = menu.addAction("Delete selected")
        deleteAction2 = menu.addAction("Remove selected (without deleting file")
        writeTagAction = menu.addAction("Write the tags")
        mp3infos = menu.addAction("Show mp3 infos")
        tapbpm = menu.addAction("Set the bpm by taping the tempo of the song")
        updateTangoDurations = menu.addAction("update the Tango duration")
        action = menu.exec_(self._dialog.milongaSource.viewport().mapToGlobal(pos))
        if action == detailsAction:
            self.handelOpenPropWidow()
        elif action == deleteAction:
            # print("I will delete selected tangos and remove the file")
            self.deleteTangos(True)
        elif action == deleteAction2:
            # print("I will delete selected tangos and keep the file")
            self.deleteTangos()

        elif action == audacityAction:
            indexes = self._dialog.milongaSource.selectionModel().selectedRows()
            self.curTangoEditing = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)
            os.system("audacity \"" + str(self._tangoList.tangos[self.curTangoEditing].path) + "\" &")
        elif action == writeTagAction:
            indexes = self._dialog.milongaSource.selectionModel().selectedRows()
            for index in indexes:
                # print(index.column())
                curTangoID = self.sourceProxyModel.data(index, Qt.DisplayRole)
                # print("tangoID: "+str(curTangoID))
                self._tangoList.tangos[curTangoID].writeTags(self.TYPE)
        elif action == mp3infos:
            indexes = self._dialog.milongaSource.selectionModel().selectedRows()
            self.curTangoEditing = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)
            os.system("mp3info2 \"" + str(self._tangoList.tangos[self.curTangoEditing].path) + "\" &")
        elif action == tapbpm:
            self._handelBpmTappingAction()
        elif action == updateTangoDurations:
            self.updateDuration()

    def _handelBpmTappingAction(self):
        indexes = self._dialog.milongaSource.selectionModel().selectedRows()
        self.curTangoEditing = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)
        self.curLibraryRow = indexes[0].row()
        self._isClicked = True
        self.curTango = self._tangoList.tangos[self.curTangoEditing]
        self._load_new_media()
        self._playMedia()
        self.tapTable = []
        self.tapContent.lcdNumber.display(0.0)
        self.bpm = 0
        self.initialiszeBmpInfo()
        self.tapWindow.show()

    # def playCurrentRow():

    def _handelBpmTapping(self):
        self.tapTable.append(time.time())
        # print(self.tapTable)

        self.delta = []
        self.bpmtrack = []
        if len(self.tapTable) > 1:
            for i in range(1, len(self.tapTable)):
                self.delta.append(self.tapTable[i] - self.tapTable[i - 1])
                self.bpmtrack.append(60 / (sum(self.delta) / len(self.delta)))
            mean = sum(self.delta) / len(self.delta)

            self.bpm = 60 / mean

            if len(self.bpmtrack) > 4:
                # print("sup to 4")
                temp = []
                for i in range(len(self.bpmtrack) - 1, len(self.bpmtrack) - 6, -1):
                    # print (self.delta[i])
                    temp.append(self.bpmtrack[i])
                # print("delta: "+str(max(temp)-min(temp)))
                if max(temp) - min(temp) < 0.3 and self.bmpState != 2:
                    self.tapContent.labelDone.setText("DONE")
                    self.tapContent.labelDone.setStyleSheet("color: rgba(70,169,73)")
                    self.bmpState = 2
                    # print("STOP")
                elif max(temp) - min(temp) < 0.8 and max(temp) - min(temp) > 0.5 and self.bmpState == 0:
                    self.tapContent.labelDone.setText("CONTINUE")
                    self.tapContent.labelDone.setStyleSheet("color: rgba(215,0,8)")
                    self.bmpState = 1
                elif max(temp) - min(temp) < 0.5 and self.bmpState != 2:
                    self.tapContent.labelDone.setText("ALMOST")
                    self.tapContent.labelDone.setStyleSheet("color: rgba(240,169,73)")

            self.curTango.bpmHuman = self.bpm

            self.tapContent.lcdNumber.display(self.bpm)

    def initialiszeBmpInfo(self):
        self.bmpState = 0
        self.tapContent.labelDone.setText("DONE")
        self.tapContent.labelDone.setStyleSheet("color: rgba(42,42,42)")
        # print(self.curTango.bpmHuman)
        # print(self.curTango.bpmFromFile)
        if self.curTango.bpmHuman == 0 and self.curTango.bpmFromFile == 0:
            self.tapContent.labelTypeBmp.setText("Not set")
            self.tapContent.labelTypeBmp.setStyleSheet("color: rgba(215,0,8)")
        elif self.curTango.bpmHuman == 0 and self.curTango.bpmFromFile > 0:
            self.tapContent.labelTypeBmp.setText("Set by computer")
            self.tapContent.labelTypeBmp.setStyleSheet("color: rgba(240,169,73)")
        else:
            self.tapContent.labelTypeBmp.setText("Set by human")
            self.tapContent.labelTypeBmp.setStyleSheet("color: rgba(70,169,73)")

    def _handelValidatebpm(self):

        self.updateTangoBPM()
        self.tapWindow.close()

    def _handelCancelbpm(self):
        self.tapWindow.close()

    def _handelTapingNext(self):
        # print("next")

        self.updateTangoBPM()
        self.tapTable = []
        self.delta = []
        self.tapContent.lcdNumber.display(0.0)
        self.bpm = 0
        if self.curLibraryRow + 1 < self.sourceProxyModel.rowCount(QModelIndex()):
            self.curLibraryRow += 1
            index = self.sourceProxyModel.index(self.curLibraryRow, 0)
            self.curTangoEditing = self.sourceProxyModel.data(index, Qt.DisplayRole)
            self._dialog.milongaSource.selectRow(self.curLibraryRow)
            self._isClicked = True
            self.curTango = self._tangoList.tangos[self.curTangoEditing]
            self._load_new_media()
            self._playMedia()
            self.initialiszeBmpInfo()

    def _handelTapingPrevious(self):
        # print("Previous")
        self.updateTangoBPM()
        self.tapTable = []
        self.delta = []
        self.tapContent.lcdNumber.display(0.0)
        self.bpm = 0
        if self.curLibraryRow - 1 >= 0:
            self.curLibraryRow -= 1
            index = self.sourceProxyModel.index(self.curLibraryRow, 0)
            self.curTangoEditing = self.sourceProxyModel.data(index, Qt.DisplayRole)
            self._dialog.milongaSource.selectRow(self.curLibraryRow)
            self._isClicked = True
            self.curTango = self._tangoList.tangos[self.curTangoEditing]
            self._load_new_media()
            self._playMedia()
            self.initialiszeBmpInfo()

    def updateTangoBPM(self):
        indexes = self._dialog.milongaSource.selectionModel().selectedRows()
        tangoID = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)
        # self._tangoList.tangos[tangoID].bpmHuman = self.bpm
        data = self._tangoList.tangos[tangoID].list()
        count = 0
        for cdata in data:
            index = self.sourceProxyModel.index(indexes[0].row(), count)
            # if count =
            self.sourceProxyModel.setData(index, cdata, Qt.EditRole)
            count += 1

        self.djData.updateBPM(self._tangoList.tangos[tangoID])

    def updateTangoProp(self):
        indexes = self._dialog.milongaSource.selectionModel().selectedRows()
        # ATTENTION, si l'utilisateur change l'index, (en cliquant sur un autre musique par exemple, on met tout en l'air)
        # solution : interdir le double click sur pour changer la chanson ou conserver la valeur et la position du tango en cours d'édition

        if len(indexes) > 1:
            self.detailsContent.nextButton.setVisible(False)
            self.detailsContent.previousButton.setVisible(False)
            self.detailsContent.textPath.setText('')
        else:
            self.detailsContent.nextButton.setVisible(True)
            self.detailsContent.previousButton.setVisible(True)

            self.curTangoEditing = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)

            self.curLibraryRow = indexes[0].row()
            self.detailsContent.textPath.setText(self._tangoList.tangos[self.curTangoEditing].path)
            if self.detailsContent.checkBoxPlayMusic.isChecked():
                self._isClicked = True
                self.curTango = self._tangoList.tangos[self.curTangoEditing]
                self._load_new_media()
                self._playMedia()

            # check for the common fields
        sameFieldValue = self.getSameFieldInfos(indexes)

        # self.detailsContent.lineEditTitle.setText('-')

        # print (sameFieldValue)
        if sameFieldValue['artist'] == False:
            self.detailsContent.lineEditArtist.setText('-')
        elif sameFieldValue['artist'] != "Unknown":
            self.detailsContent.lineEditArtist.setText(sameFieldValue['artist'])
        else:
            self.detailsContent.lineEditArtist.setText('')

        if sameFieldValue['title'] == False:
            self.detailsContent.lineEditTitle.setText('-')
        elif sameFieldValue['title'] != "Unknown":
            self.detailsContent.lineEditTitle.setText(sameFieldValue['title'])
        else:
            self.detailsContent.lineEditTitle.setText('')

        if sameFieldValue['album'] == False:
            self.detailsContent.lineEditAlbum.setText('-')
        elif sameFieldValue['album'] != "Unknown":
            self.detailsContent.lineEditAlbum.setText(sameFieldValue['album'])
        else:
            self.detailsContent.lineEditAlbum.setText('')

        if sameFieldValue['type'] == False:
            self.detailsContent.comboBoxTangoType.setCurrentIndex(-1)
        else:
            self.detailsContent.comboBoxTangoType.setCurrentIndex(sameFieldValue['type'] - 1)

        if sameFieldValue['year'] == False:
            self.detailsContent.spinBoxYear.setValue(-1)
        else:
            self.detailsContent.spinBoxYear.setValue(sameFieldValue['year'])

    def getSameFieldInfos(self, indexes):
        sameFieldValue = {}
        for i in range(0, len(indexes)):
            tangoID = self.sourceProxyModel.data(indexes[i], Qt.DisplayRole)
            # print ("tangoID: "+str(tangoID))
            if 'artist' not in sameFieldValue:
                sameFieldValue['artist'] = self._tangoList.tangos[tangoID].artist
            elif sameFieldValue['artist'] == self._tangoList.tangos[tangoID].artist:
                pass
            else:
                sameFieldValue['artist'] = False

            if 'album' not in sameFieldValue:
                sameFieldValue['album'] = self._tangoList.tangos[tangoID].album
            elif sameFieldValue['album'] == self._tangoList.tangos[tangoID].album:
                pass
            else:
                sameFieldValue['album'] = False

            if 'type' not in sameFieldValue:
                sameFieldValue['type'] = self._tangoList.tangos[tangoID].type
            elif sameFieldValue['type'] == self._tangoList.tangos[tangoID].type:
                pass
            else:
                sameFieldValue['type'] = False

            if 'year' not in sameFieldValue:
                sameFieldValue['year'] = self._tangoList.tangos[tangoID].year
            elif sameFieldValue['year'] == self._tangoList.tangos[tangoID].year:
                pass
            else:
                sameFieldValue['year'] = False

            if 'title' not in sameFieldValue:
                sameFieldValue['title'] = self._tangoList.tangos[tangoID].title
            elif sameFieldValue['title'] == self._tangoList.tangos[tangoID].title:
                pass
            else:
                sameFieldValue['title'] = False
        return sameFieldValue

    # check if the tango has change or not
    def isSomethingChanged(self):
        ret = True
        if (self.TangoBeforeChange.artist == self.detailsContent.lineEditArtist.text() and
                self.TangoBeforeChange.title == self.detailsContent.lineEditTitle.text() and
                self.TangoBeforeChange.year == self.detailsContent.spinBoxYear.value() and
                self.TangoBeforeChange.type == self.detailsContent.comboBoxTangoType.currentIndex() + 1 and
                self.TangoBeforeChange.album == self.detailsContent.lineEditAlbum.text()):
            # print("rien n'a changé")
            ret = False
        # else:
        #    print("quelque chose a changé")
        #    print (self.TangoBeforeChange.artist+" -> "+ self.detailsContent.lineEditArtist.text())
        #    print (self.TangoBeforeChange.title+" -> "+ self.detailsContent.lineEditTitle.text())
        #    print (self.TangoBeforeChange.year+" -> "+ self.detailsContent.spinBoxYear.value())
        #    print (self.TangoBeforeChange.type+" -> "+ self.detailsContent.lineEditArtist.text())
        #    print (self.TangoBeforeChange.album+" -> "+ self.detailsContent.lineEditArtist.text())

        return ret

    def updateTangoSong(self):
        if not self.isSomethingChanged():
            return
        self.scanningDir = True
        indexes = self._dialog.milongaSource.selectionModel().selectedRows()
        for i in range(0, len(indexes)):
            tangoID = self.sourceProxyModel.data(indexes[i], Qt.DisplayRole)
            if not self.detailsContent.lineEditArtist.text() == '-':
                if not self.detailsContent.lineEditArtist.text() == '':
                    self._tangoList.tangos[tangoID].artist = self.detailsContent.lineEditArtist.text()
                else:
                    self._tangoList.tangos[tangoID].artist = 'Unknown'

            if not self.detailsContent.lineEditTitle.text() == '-':
                if not self.detailsContent.lineEditTitle.text() == '':
                    self._tangoList.tangos[tangoID].title = self.detailsContent.lineEditTitle.text()
                else:
                    self._tangoList.tangos[tangoID].title = 'Unknown'

            if self.detailsContent.spinBoxYear.value() > 0:
                self._tangoList.tangos[tangoID].year = self.detailsContent.spinBoxYear.value()

            if not self.detailsContent.lineEditAlbum.text() == '-':
                if not self.detailsContent.lineEditAlbum.text() == '':
                    self._tangoList.tangos[tangoID].album = self.detailsContent.lineEditAlbum.text()
                else:
                    self._tangoList.tangos[tangoID].album = 'Unknown'

            if self.detailsContent.comboBoxTangoType.currentIndex() > -1:
                self._tangoList.tangos[tangoID].type = self.detailsContent.comboBoxTangoType.currentIndex() + 1

                #

            if self.normalize == 2:
                self._tangoList.normalizeTango(tangoID, self.TYPE)

            if self.writeTag == 2:
                self._tangoList.tangos[tangoID].writeTags(self.TYPE)

            data = self._tangoList.tangos[tangoID].list()
            # data[8] = utils.msecToms(data[8])
            count = 0
            for cdata in data:
                index = self.sourceProxyModel.index(indexes[i].row(), count)
                self.sourceProxyModel.setData(index, cdata, Qt.EditRole)
                count += 1
            # print("before to update tango")
            # print(self._tangoList.tangos[tangoID].duration)
            # dirsong.normalizeTango(self._tangoList.tangos[tangoID], self.audioPath)

            self.djData.updateTango(self._tangoList.tangos[tangoID])

            self.updateTangoInfos(self._tangoList.tangos[tangoID])

        self.scanningDir = False

    ### END ###########################

    ##########################################################################################
    #
    # Function to deal with context menu in milonga Dest
    #
    ##########################################################################################
    def popupMilonga(self, pos):
        menu = QMenu()
        deleteAction = menu.addAction("Delete")
        action = menu.exec_(self._dialog.milongaDest.viewport().mapToGlobal(pos))
        if action == deleteAction:
            self.deleteTangoInMilonga()

    def deleteTangoInMilonga(self):
        # print ("will delete song")
        indexes = self._dialog.milongaDest.selectionModel().selectedRows()

        # print ("number of rows: "+str(len(indexes)))
        for index in indexes:
            if index.isValid():
                # print (index.row())
                self.destModel.removeRows(index.row(), 1, QModelIndex())

    def _handelHideSource(self):
        # self._dialog.milongaLayout.setVisible(False)
        if self._dialog.milongaSource.isVisible():
            self._dialog.pushButtonHideDest.setVisible(False)
            self._dialog.pushButtonHideSource.setIcon(QIcon("./djtango/img/hide-right.png"))
            self._dialog.milongaSource.setVisible(False)
            self._dialog.pushButtonClearFilter.setVisible(False)
            self._dialog.comboBoxArtist.setVisible(False)
            self._dialog.comboBoxAlbum.setVisible(False)
            self._dialog.comboBoxGenre.setVisible(False)
            self._dialog.lineEditFilter.setVisible(False)
            self._dialog.pushButtonRandom.setVisible(False)
            self._dialog.labelsongNB_source.setVisible(False)

        else:
            self._dialog.pushButtonHideDest.setVisible(True)
            self._dialog.pushButtonHideSource.setIcon(QIcon("./djtango/img/hide-left.png"))
            self._dialog.milongaSource.setVisible(True)
            self._dialog.pushButtonClearFilter.setVisible(True)
            self._dialog.comboBoxArtist.setVisible(True)
            self._dialog.comboBoxAlbum.setVisible(True)
            self._dialog.comboBoxGenre.setVisible(True)
            self._dialog.lineEditFilter.setVisible(True)
            self._dialog.pushButtonRandom.setVisible(True)
            self._dialog.labelsongNB_source.setVisible(True)

    def _handelHideDest(self):

        if self._dialog.milongaDest.isVisible():
            self._dialog.pushButtonHideSource.setVisible(False)
            self._dialog.pushButtonHideDest.setIcon(QIcon("./djtango/img/hide-left.png"))

            self._dialog.milongaDest.setVisible(False)
            self._dialog.pushButtonMilongaClear.setVisible(False)
            self._dialog.labelMilongaName.setVisible(False)
            self._dialog.pushButtonLoadMilonga.setVisible(False)
            self._dialog.pushButtonDeleteMilonga.setVisible(False)
            self._dialog.pushButtonSaveMilonga.setVisible(False)
            self._dialog.labelSizeDuration.setVisible(False)
            self._dialog.pushButtonInfoMilonga.setVisible(False)
            self._dialog.pushButtonSaveMilongaAs.setVisible(False)



        else:
            self._dialog.pushButtonHideSource.setVisible(True)
            self._dialog.pushButtonHideDest.setIcon(QIcon("./djtango/img/hide-right.png"))

            self._dialog.milongaDest.setVisible(True)
            self._dialog.milongaDest.setVisible(True)
            self._dialog.pushButtonMilongaClear.setVisible(True)
            self._dialog.labelMilongaName.setVisible(True)
            self._dialog.pushButtonLoadMilonga.setVisible(True)
            self._dialog.pushButtonDeleteMilonga.setVisible(True)
            self._dialog.pushButtonSaveMilonga.setVisible(True)
            self._dialog.labelSizeDuration.setVisible(True)
            self._dialog.pushButtonInfoMilonga.setVisible(True)
            self._dialog.pushButtonSaveMilongaAs.setVisible(True)
            # self.resizeHeaderSource()
            # self._dialog.milongaSource.horizontalHeader() emit()

    ### END ###########################

    ##########################################################################################
    #
    # Function to deal with the preferencies of the application
    #
    ##########################################################################################

    def _handelPrefClose(self):
        # print ("will update preferences")
        self.prefWindow.exec_()
        if self.prefWindow.result() == 0:
            return

        sys.stdout.write(str(self.prefWindow.result()))
        self._tangoList.songpath = self.prefContent.lineEditSongDir.text()
        self.durationFadOut = self.prefContent.spinBoxFadeOut.value() * 1000
        self.FadOutTime = self.prefContent.spinBoxCortinaDuration.value() * 1000
        self.stepFadOut = self.durationFadOut / self.player.notifyInterval()
        self.writeTag = self.prefContent.checkBoxWriteTags.checkState()
        self.normalize = self.prefContent.checkBoxNormalize.checkState()

        self.djData.updateProperties(self.durationFadOut, self.FadOutTime, self.writeTag, self.normalize, self.TYPE)
        # if self.isMilongaPlaying:
        if self.destModel.rowCount(QModelIndex()) > 1:
            self.updateMilongaInfos();

    def open_file_dialog(self):

        dir_name = QFileDialog.getExistingDirectory(self, "Open Directory", os.path.expanduser('~'),
                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks);
        # print (dirName)
        self.prefContent.lineEditSongDir.setText(dir_name)
        self.scanningDir = True
        new_files = self._tangoList.checkNewFiles()
        if new_files:
            for path in new_files:
                # insert automatiquement un nouveau fichier et met à jour la liste
                self.djData.insertTango(TangoSong(path, 0, True))
                self._tangoList.loadTangos(unstr.djData.getAllTangos())

                data = []
                for key in self._tangoList.tangos.keys():
                    tango = self._tangoList.tangos[key]
                    data.append(tango.list())
                self.sourceModel.changeData(data)
                self._showInfo(str(len(new_files)) + " song has been added")

        self.scanningDir = False

    def _addTangoType(self):
        # print("adding "+self.prefContent.lineEditTangoType.text())
        text = self.prefContent.lineEditTangoType.text()
        # print(text)
        if text == '':
            self._showInfo("put some text in the field")
        else:
            self.prefContent.listWidgetTangoType.addItem(text)
            self.prefContent.lineEditTangoType.setText('')
            lastRow = self.prefContent.listWidgetTangoType.count() - 1
            # print('lastrow: '+str(lastRow))
            self.TYPE[lastRow + 1] = (lastRow + 1, text, 42, 42, 42, 255)
            # print (self.TYPE)
            self.prefContent.listWidgetTangoType.setCurrentRow(lastRow, QItemSelectionModel.ClearAndSelect)

            # print(self.prefContent.listWidgetTangoType.currentRow())
            # self._selectTangoChange()

            self.colorDialog.show()

            # self._selectTangoColor()
            # TODO : updating the self.TYPE and the database in the update button handling

    def _removeTangoType(self):
        row = self.prefContent.listWidgetTangoType.currentRow()
        if row > 4:
            self.prefContent.listWidgetTangoType.takeItem(row)
        else:
            self._showInfo("this item is not removable")

    def _selectTangoColor(self):
        color = self.colorDialog.currentColor()
        # print(color.red())
        self.prefContent.selectColorButton.setStyleSheet(
            "background-color: rgba(" + str(color.red()) + "," + str(color.green()) + "," + str(
                color.blue()) + "," + str(color.alpha()) + ")")
        item = self.prefContent.listWidgetTangoType.currentRow()
        # print ("item:"+str(item)+" color: "+str(color))
        self.TYPE[item + 1] = (
            self.TYPE[item + 1][0], self.TYPE[item + 1][1], color.red(), color.green(), color.blue(), color.alpha())

    def _selectTangoChange(self):
        item = self.prefContent.listWidgetTangoType.currentRow()
        # print("currentrow:"+str(item) )
        # self.prefContent.listWidgetTangoType.insertItem(i-1, self.TYPE[i][1])
        R = self.TYPE[item + 1][2]
        G = self.TYPE[item + 1][3]
        B = self.TYPE[item + 1][4]
        T = self.TYPE[item + 1][5]
        self.prefContent.selectColorButton.setStyleSheet(
            "background-color: rgba(" + str(R) + "," + str(G) + "," + str(B) + "," + str(T) + ")")

        # print("row changed")
        # pass

    ### END ###########################

    def _handelPlayPause(self):

        # print ("number of row in Milonga: "+str(self.destModel.rowCount(QModelIndex())))
        if self._isPlaying:
            self._pauseMedia()
            self._isPaused = True
        else:
            if self.destModel.rowCount(QModelIndex()) > 0 and not self._isPaused:
                # self._isMilongaPlaying = True
                self._handelMilongaLaunch()
            else:
                #    self._isMilongaPlaying = False
                if self._okToPlayPauseStop:
                    self._playMedia()
            # elif self._dialog.tabMilonga
            self._isPaused = False

    def _handelMilongaLaunch(self):

        self.curLibraryRow = 0

        index = self.destModel.index(self.curLibraryRow, 0)
        self._currentIndex = self.destModel.data(index, Qt.DisplayRole)
        # self.curLibraryRow = indexes[0].row()
        self.curTango = self._tangoList.tangos[self._currentIndex]
        self._isMilongaPlaying = True
        self._updateSideScreen()
        self._startMilongaTimeStamp = time.time()
        # print("new Start: "+str(self._startMilongaTimeStamp))
        self._isClicked = True
        self._dialog.milongaDest.selectRow(self.curLibraryRow)
        index = self.destModel.index(self.curLibraryRow, 1)
        # set the player icon to play
        self.destModel.setData(index, 1, Qt.EditRole)
        # print ("launching the Milonga")
        self.updateMilongaInfos();

        self._load_new_media()
        self._playMedia()

    def play_next_tango(self):
        if self._isMilongaPlaying:
            self.play_next_milonga_song()
        else:
            self.playNextLibrarySong()

    def play_next_milonga_song(self):

        print("I will play the next one")

        rowIndex = self.curLibraryRow + 1
        if rowIndex <= self.destModel.rowCount(
                QModelIndex()):  # we allow put the cursor after the en of the list, but will not play it
            self.curLibraryRow += 1
            rowIndex = self.curLibraryRow + 1
        index = self.destModel.index(self.curLibraryRow, 0)
        self._currentIndex = self.destModel.data(index, Qt.DisplayRole)
        self._dialog.milongaDest.selectRow(self.curLibraryRow)
        self.updatePlayingCursor()

        if rowIndex <= self.destModel.rowCount(QModelIndex()):
            self.curTango = self._tangoList.tangos[self._currentIndex]
            if self.curTango.type == 4:
                time.sleep(0.5)
            else:
                time.sleep(1.5)
            if self.sideWindow.isFullScreen() and rowIndex == self.destModel.rowCount(QModelIndex()):
                self._updateSideScreen(True)
            elif self.sideWindow.isFullScreen():
                self._updateSideScreen()
            if self._load_new_media():
                self._play_media()
            else:
                self.play_next_milonga_song()
        else:
            self._showInfo("The milonga is finished")

    def playNextLibrarySong(self):

        rowIndex = self.curLibraryRow + 1
        # print("avant: "+str(rowIndex)+" -> "+str(self.sourceProxyModel.rowCount(QModelIndex())))
        if rowIndex <= self.sourceProxyModel.rowCount(
                QModelIndex()):  # we allow put the cursor after the en of the list, but will not play it
            self.curLibraryRow += 1
            rowIndex = self.curLibraryRow + 1

        index = self.sourceProxyModel.index(self.curLibraryRow, 0)
        self._currentIndex = self.sourceProxyModel.data(index, Qt.DisplayRole)
        # print("curIndex: "+str(self._currentIndex))
        self._dialog.milongaSource.selectRow(self.curLibraryRow)
        # index = self.sourceProxyModel.index(self.curLibraryRow, 1)
        # self.sourceProxyModel.setData(index, 1, Qt.EditRole)
        self.updatePlayingCursor()

        # print("Apres: "+str(rowIndex)+" -> "+str(self.sourceProxyModel.rowCount(QModelIndex())))
        time.sleep(0.1)

        if rowIndex <= self.sourceProxyModel.rowCount(QModelIndex()):

            self.curTango = self._tangoList.tangos[self._currentIndex]

            self._load_new_media()
            self._playMedia()
            self._updateSideScreen()
            # print("je met à jour le side Screen")
            # pdb.set_trace()
        else:
            self._showInfo("We have reach the end of the list we stop here")

    def updatePlayingCursor(self):
        self.clearPlayingCursor()
        if self._isMilongaPlaying:
            index = self.destModel.index(self.curLibraryRow, 1)
            self.destModel.setData(index, 1, Qt.EditRole)
        else:
            index = self.sourceProxyModel.index(self.curLibraryRow, 1)
            self.sourceProxyModel.setData(index, 1, Qt.EditRole)

    def clearPlayingCursor(self):
        # print("clearing cursors")

        if not self._isMilongaPlaying:
            for row in range(0, self.sourceProxyModel.rowCount(QModelIndex())):
                # print(row)
                index = self.sourceProxyModel.index(row, 1)
                self.sourceProxyModel.setData(index, 0, Qt.EditRole)
        else:
            for row in range(0, self.destModel.rowCount(QModelIndex())):
                # print(row)
                index = self.destModel.index(row, 1)
                self.destModel.setData(index, 0, Qt.EditRole)

    def playSelectedSource(self):
        # print("will play on enter press?")
        self._libraryClicked()

    def _libraryClicked(self):
        if self._isMilongaPlaying:
            self._showInfo("You can't play a tango if a milonga is playing. Stop the Milonga first")
            return
        if self.propWindow.isVisible():
            return
        self._isClicked = True
        indexes = self._dialog.milongaSource.selectionModel().selectedRows()

        # self.clearPlayingCursor()

        if len(indexes) == 1:
            self._currentIndex = self.sourceProxyModel.data(indexes[0], Qt.DisplayRole)
            self.curLibraryRow = indexes[0].row()
            self.curTango = self._tangoList.tangos[self._currentIndex]

            # index = self.sourceProxyModel.index(indexes[0].row(), 1)
            # self.sourceProxyModel.setData(index, 1, Qt.EditRole)
            self.updatePlayingCursor()
            self._load_new_media()
            self._playMedia()
            self._updateSideScreen()

    def _destLibraryClicked(self):
        if self._isMilongaPlaying:
            self._showInfo("You can't play a tango if a milonga is playing. Stop the Milonga first")
            return
        if self.propWindow.isVisible():
            return
        # print ("will paly a song in dest")

        self._isClicked = True
        indexes = self._dialog.milongaDest.selectionModel().selectedRows()

        if len(indexes) == 1:
            self._currentIndex = self.destModel.data(indexes[0], Qt.DisplayRole)
            # print("the current Index is "+ str(self._currentIndex));
            self.curLibraryRow = indexes[0].row()
            self.curTango = self._tangoList.tangos[self._currentIndex]

            self._load_new_media()
            self._playMedia()

    def updateDuration(self):

        sysName = platform.system();
        print(sysName);
        if (sysName == 'Linux'):
            for key in self._tangoList.tangos:
                tmpTango = self._tangoList.tangos[key]
                audio = audioread.audio_open(tmpTango.path)
                print(str(audio.duration * 1000))
                tmpTango.duration = audio.duration * 1000
                self.djData.updateTango(tmpTango)
        elif (sysName == 'Windows'):
            self._showInfo('You can not run this command on Windows :-(')

    def _load_new_media(self):
        print(self.curTango.path)
        if not os.path.isfile(self.curTango.path):
            self._showInfo('This file is not existing on disk, remove it')
            return False
        else:
            self.mediaSource = QMediaContent(QUrl.fromLocalFile(QFileInfo(self.curTango.path).absoluteFilePath()))
            self.player.setMedia(self.mediaSource)
            return True

    def _playMedia(self):
        """
        Play the curent tango
        """

        if not self._okToPlayPauseStop():
            return

        # if self.mediaObj is None:

        #    self._showInfo ("Error playing Audio")
        #    return

        if self.curTango is None:
            self._showInfo("No tango selected")
            return

        # self.audioSink.setVolume(1.0)
        self._dialog.playToolButton.setIcon(self.pauseIcon)
        self.updateTangoInfos(self.curTango)
        self._isPlaying = True

        # self.mediaObj.play()
        # print("je vais jouer le tango")

        # print(self.mediaSource)
        # pdb.set_trace()
        if not self.curTango.tstart == 0:
            self.seek(self.curTango.tstart / 1000)

        if self._isMilongaPlaying:
            time.sleep(1.5)
        self.player.play()
        # print("c'est parti")

        # time.sleep(0.1)

    def updateTangoInfos(self, tango):

        if self.curTango is not None and self.curTango.ID == tango.ID:
            self.curTango = tango
            self._dialog.labelTypeSong.setText(self.TYPE[tango.type][1].upper())
            self._dialog.labelArtist.setText(tango.artist)
            self._dialog.labelAlbum.setText(tango.album)
            self._dialog.labelTitle.setText(tango.title)

    def _stopMedia(self):
        """
        Stop streaming the media
        """
        # print ("stoping")
        if not self._okToPlayPauseStop():
            return
        self.clearPlayingCursor()

        if self._isMilongaPlaying:
            self._isMilongaPlaying = False

        # self.mediaObj.stop()

        self._isPlaying = False
        self._dialog.playToolButton.setIcon(self.playIcon)
        self._dialog.timeLabel.setText("00:00 / 00:00")
        self.player.stop()

    def _pauseMedia(self):
        """
        Pause the media streaming
        """
        self._isPlaying = False
        if not self._okToPlayPauseStop():
            return
        # self.mediaObj.pause()
        self.player.pause()
        self._dialog.playToolButton.setIcon(self.playIcon)

    def _okToPlayPauseStop(self):
        """
        Determines if the medai source can be played paused or stopped.
        """
        okToProceed = True
        if self.mediaSource is None:
            err = "No tango selected, please select a tango first"
            self._dialog.playToolButton.setIcon(self.playIcon)
            # self._dialog.fileLineEdit.setText(err)
            # self._dialog.titleLineEdit.setText(err)
            # print (err)
            self._showInfo(err)

            okToProceed = False

        return okToProceed

    # def _handelFilter(self):
    #	print ("will filter")

    # ---------------------------------------------
    #
    # Deal with the filter infos
    #
    # ---------------------------------------------
    def getListOfArtist(self, album, genre):
        # print ("in get artists")
        artists = {}
        for key in self._tangoList.tangos.keys():
            if not album == '' and not self._tangoList.tangos[key].album.lower() == album.lower():
                pass
            elif (album == '') or (not album == '' and self._tangoList.tangos[key].album.lower() == album.lower()):
                if self._tangoList.tangos[key].artist not in artists:
                    artists[self._tangoList.tangos[key].artist] = 1
                else:
                    artists[self._tangoList.tangos[key].artist] += 1
        return artists

    def getListOfAlbum(self, artist, genre):
        albums = {}
        for key in self._tangoList.tangos.keys():
            if self._tangoList.tangos[key].album not in albums:
                albums[self._tangoList.tangos[key].album] = 1
            else:
                albums[self._tangoList.tangos[key].album] += 1
        return albums

    def setListOfType(self):
        for i in range(0, self._dialog.comboBoxGenre.count()):
            self._dialog.comboBoxGenre.removeItem(i)
        self._dialog.comboBoxGenre.insertItem(0, '-select type-')
        for i in range(1, len(self.TYPE) + 1):
            self._dialog.comboBoxGenre.insertItem(i, self.TYPE[i][1].title())

    def setListOfArtist(self, album='', genre=''):

        artists = self.getListOfArtist(album, genre)
        self._dialog.comboBoxArtist.clear()
        self._dialog.comboBoxArtist.insertItem(0, '-select Artist-')
        count = 1
        for key in sorted(artists.keys()):
            self._dialog.comboBoxArtist.insertItem(count, key + " (" + str(artists[key]) + ")")
            count += 1

    def setListOfAlbum(self, artist='', genre=''):
        album = self.getListOfAlbum(artist, genre)
        self._dialog.comboBoxAlbum.clear()
        self._dialog.comboBoxAlbum.insertItem(0, '-select Album-')
        count = 1
        for key in sorted(album.keys()):
            self._dialog.comboBoxAlbum.insertItem(count, key + " (" + str(album[key]) + ")")
            count += 1

    def _handelFilterChange(self):
        reg = re.compile('(.+)\s\(\d+\)')
        # print ("I will filter")
        artist = self._dialog.comboBoxArtist.currentText()
        album = self._dialog.comboBoxAlbum.currentText()
        genre = self._dialog.comboBoxGenre.currentText()
        linefilter = self._dialog.lineEditFilter.text()
        # print ("filter is : "+str(linefilter))

        res = reg.search(artist)
        if res:
            artist = res.group(1)
        elif self._dialog.comboBoxArtist.currentIndex() == 0:
            artist = '.*'
        res = reg.search(album)
        if res:
            album = res.group(1)
        elif self._dialog.comboBoxAlbum.currentIndex() == 0:
            album = '.*'

        if self._dialog.comboBoxGenre.currentIndex() == 0:
            genre = '.*'

        if linefilter == '':
            # print("filter is empty")
            linefilter = '.*'

        # TODO : quand selection d'un album, ne mettre que les auteurs et les genres
        # qui correspondent. Faire même chose pour artistes et genre
        self.sourceProxyModel.setlFilterValues(artist, album, genre, linefilter)
        self._dialog.labelsongNB_source.setText(str(self.sourceProxyModel.rowCount(QModelIndex())) + " song(s)");

    def _clearFilter(self):

        indexArtist = self._dialog.comboBoxArtist.currentIndex()
        indexAlbum = self._dialog.comboBoxAlbum.currentIndex()
        indexGenre = self._dialog.comboBoxGenre.currentIndex()
        filterVal = self._dialog.lineEditFilter.text()
        manualUpdate = False

        if indexAlbum == 0 and indexArtist == 0 and indexGenre == 0 and not filterVal == '':
            manualUpdate = True

        self._dialog.comboBoxArtist.setCurrentIndex(0)
        self._dialog.comboBoxAlbum.setCurrentIndex(0)
        self._dialog.comboBoxGenre.setCurrentIndex(0)
        self._dialog.lineEditFilter.clear()

        # print("shoul i update ? "+str(manualUpdate))
        if manualUpdate:
            self._handelFilterChange()

        self._dialog.labelsongNB_source.setText(str(self.sourceProxyModel.rowCount(QModelIndex())) + " song(s)");

    # ----------------------------------------------------
    #
    # Deal with save, load clean and delete the milongas
    #
    # ----------------------------------------------------

    def _saveMilonga(self):

        # if self._isMilongaPlaying:
        #    self._showInfo("You can not do this while a milonga is playing")
        #    return

        if self.destModel.rowCount(QModelIndex()) == 0:
            self._showInfo("The Milonga list is empty, can't save anything")
            return

        if self._dialog.labelMilongaName.text() == '- No Milonga -':
            self.milongaNameWindow.exec_()
            if self.milongaNameWindow.result() == 1:
                self.currentMilongaName = self.milongaNameContent.lineEditName.text()
                self._dialog.labelMilongaName.setText(self.currentMilongaName)
            else:
                return
            # print ("Have a name : "+self.currentMilongaName)

        self.djData.saveMilonga(self.currentMilongaName, self.getIDListFromMilonga())
        self._showInfo("The milonga \"" + str(self.currentMilongaName) + "\" has been saved")

    def _saveMilongaAs(self):

        if self.destModel.rowCount(QModelIndex()) == 0:
            self._showInfo("The Milonga list is empty, can't save anything")
            return

        # if self._dialog.labelMilongaName.text() == '- No Milonga -':
        self.milongaNameContent.lineEditName.setText(self.currentMilongaName)
        self.milongaNameWindow.exec_()
        if self.milongaNameWindow.result() == 1:
            self.currentMilongaName = self.milongaNameContent.lineEditName.text()
            self._dialog.labelMilongaName.setText(self.currentMilongaName)
        else:
            return
            # print ("Have a name : "+self.currentMilongaName)

        self.djData.saveMilonga(self.currentMilongaName, self.getIDListFromMilonga())
        self._showInfo("The milonga \"" + str(self.currentMilongaName) + "\" has been saved")

    def _deleteMilonga(self):
        if self._isMilongaPlaying:
            self._showInfo("You can not do this while a milonga is playing")
            return

        if self._dialog.labelMilongaName.text() == '- No Milonga -':
            # print ("will have to ask for a milonga name")
            return
        # self.currentMilongaName = 'TestMilongaName'

        self.milongaAskDelete.exec_()
        if self.milongaAskDelete.result() == 1:
            if self.djData.deleteMilonga(0, self.currentMilongaName):
                self.destModel.removeRows(0, self.destModel.rowCount(QModelIndex()), QModelIndex())
                self._dialog.labelMilongaName.setText('- No Milonga -')
                self._showInfo(self.currentMilongaName + " has been deleted")
            else:
                self._showInfo("something went wrong, " + self.currentMilongaName + " has not been deleted")
        else:
            self._showInfo("You abort the deletion")

    def _loadMilonga(self):

        if self._isMilongaPlaying:
            self._showInfo("You can not do this while a milonga is playing")
            return

        self.selectMilongaListContent.listWidgetMilongas.clear()
        self.selectMilongaListContent.listWidgetMilongas.addItems(self.djData.getListOfMilongas())
        self.selectMilongaListWindow.exec_()

        if self.selectMilongaListWindow.result() == 0:
            return
        self.currentMilongaName = self.selectMilongaListContent.listWidgetMilongas.currentItem().data(Qt.DisplayRole)
        tangoList = self.djData.getTangoFromMilonga(self.currentMilongaName)

        data = []
        for tango in tangoList:
            # tango.duration = utils.msecToms(tango.duration)
            data.append(tango.list())

        # print("column de la milonga : "+str(len(data[0])))
        self._dialog.labelMilongaName.setText(self.currentMilongaName)
        # self.updateMilongaInfos(tangoList)
        self.destModel.changeData(data)
        self.updateMilongaInfos(tangoList)

    def updateMilongaInfos(self, tangoList=None):
        # print("will udpte the milonga Infos");
        # print("updating milonga infos")
        tangoIdList = self.getIDListFromMilonga()
        # if tangoList is None and not self.currentMilongaName == '- No Milonga -':
        #    tangoList = self.djData.getTangoFromMilonga(self.currentMilongaName)
        tangoList = self.djData.getTangoFromListID(tangoIdList)
        songnum = 0
        classique = 0
        totalDuration = 0
        totalDurWithCort = 0
        ending = 0
        typeCount = {}
        # print(tangoList)
        for tango in tangoList:
            if tango.type in typeCount:
                typeCount[tango.type] += tango.duration
            else:
                typeCount[tango.type] = tango.duration

            if tango.type < 4:
                classique += tango.duration
            if not tango.type == 4:
                # print(tango.ID)
                # print(tango.duration)
                totalDuration += float(tango.duration)
                totalDurWithCort += float(tango.duration)
                songnum += 1
            else:
                totalDuration += self.FadOutTime
                # print("Add time of cortina: "+str(self.FadOutTime));

        # print("###############")

        if totalDurWithCort > 0:
            self.infoMilongaSentence = "Classique \t{0:.0f}% \nAlternatif \t{1:.0f}%".format(
                classique * 100 / totalDurWithCort,
                (1 - classique / totalDurWithCort) * 100) + "\n\n---------------------------------------\n\n"
            for key in typeCount.keys():
                if not key == 4:
                    # print ("{0:15}  {1:.0f}%".format(self.TYPE[key][1], typeCount[key]*100/totalDurWithCort))
                    self.infoMilongaSentence += "{0:15}  \t{1:.0f}%".format(self.TYPE[key][1].title(), typeCount[
                        key] * 100 / totalDurWithCort) + "\n"
        # print (self.infoMilongaSentence)
        # print("classique {0:.0f}% \nalternatif {1:.0f}%".format(classique*100/totalDurWithCort, (1-classique/totalDurWithCort)*100))

        now = time.time()
        # print(now)
        # print(time.strftime("%H:%M", time.localtime(now+totalDuration/1000)))
        end = time.strftime("%H:%M", time.localtime(self._startMilongaTimeStamp + totalDuration / 1000))
        # print ("end of Milonga: "+str(utils.msecToHouMin(now+totalDuration)))
        text = str(songnum) + " song(s)    |    duration : " + str(
            utils.msecToHouMin(totalDuration)) + "    |    Milonga will end at " + end
        self._dialog.labelSizeDuration.setText(text)

    # def getMilongaInfos(self):

    def getIDListFromMilonga(self):
        tangoIdList = []
        for i in range(0, self.destModel.rowCount(QModelIndex())):
            # print("hello "+str(i))
            index = self.destModel.index(i, 0)
            tangoID = self.destModel.data(index, Qt.DisplayRole)
            # print("tangoID: "+str(tangoID))
            tangoIdList.append(tangoID)
        return tangoIdList

    def _clearMilonga(self):
        if self._isMilongaPlaying:
            self._showInfo("You can not do this while a milonga is playing")
            return

        self._dialog.labelMilongaName.setText('- No Milonga -')
        self.destModel.removeRows(0, self.destModel.rowCount(QModelIndex()), QModelIndex())
        # self.destModel.reset()

    def _doubleClickedMilongaSelect(self):
        # print("will have to close the milonga dialog")
        self.selectMilongaListWindow.done(1)

    # ------------------------------------------------
    #
    # Deal with the info show and close infos methode
    #
    # ------------------------------------------------

    def _showInfo(self, info):
        self.infoContent.labelInfo.setText(info)
        width = self.infoContent.labelInfo.fontMetrics().boundingRect(self.infoContent.labelInfo.text()).width()
        self.infoWindow.resize(width + 60, 40)

        self.infoWindow.move(self.geometry().x() + (self.geometry().width() - self.infoWindow.geometry().width()) / 2,
                             self.geometry().y() + 5)
        # self.infoWindow.move(self.geometry().x()+self.geometry().width()-self.infoWindow.geometry().width() -5 ,
        #    self.geometry().y()+self.geometry().height()-self.infoWindow.geometry().height()-5)

        self.infoWindow.show()
        self.info_thread.render(5)

    def closeInfo(self):
        self.infoWindow.close()

    ### END ###

    # ------------------------------------------------
    #
    # Deal with the info show Milonga and close infos methode
    #
    # ------------------------------------------------

    def _showInfoMilonga(self):
        # print("in Show Info Milonga")
        # print (self.infoMilongaSentence)
        self.infoMilongaContent.labelInfo.setText(self.infoMilongaSentence)
        width = self.infoMilongaContent.labelInfo.fontMetrics().boundingRect(self.infoContent.labelInfo.text()).width()
        height = self.infoMilongaContent.labelInfo.fontMetrics().boundingRect(
            self.infoContent.labelInfo.text()).height()
        self.infoMilongaWindow.resize(width + 10, height + 10)

        self.infoMilongaWindow.move(
            self.geometry().x() + (self.geometry().width() - self.infoMilongaWindow.geometry().width()) / 2,
            self.geometry().y() + (self.geometry().height() - self.infoMilongaWindow.geometry().height()) / 2)
        # self.infoWindow.move(self.geometry().x()+self.geometry().width()-self.infoWindow.geometry().width() -5 ,
        #    self.geometry().y()+self.geometry().height()-self.infoWindow.geometry().height()-5)

        self.infoMilongaWindow.show()
        # self.infothread.render(5)

    def closeInfoMilonga(self):
        self.infoMilongaWindow.close()

    ### END ###

    # ------------------------------------------------
    #
    # Deal with displaying side screen
    #
    # ------------------------------------------------
    def _handelDisplaySideScreen(self):
        #        self.sideWindow.showFullScreen()
        # we assume that only 2 desk are available

        self._updateSideScreen()
        self.desk = QDesktopWidget()

        mainAppDeskID = self.desk.screenNumber(self)
        sideDispDeskID = 0
        # print("main app is on screen : "+str(mainAppDeskID))
        if self.desk.screenCount() > 1:
            if mainAppDeskID == 0:
                # print("will put the side on screnn 1")
                sideDispDeskID = 1
            else:
                sideDispDeskID = 0

        # print("is side checked ?"+str(self._dialog.actionDisplay_side_screen.isChecked()))
        # print("side screen will be on screen : "+str(sideDispDeskID))
        # if not self._dialog.actionDisplay_side_screen.isChecked():
        if not self.sideWindow.isVisible():

            # print ("will display side screen")

            geom = self.desk.availableGeometry(sideDispDeskID)
            # print (geom)
            self.sideWindow.move(geom.x(), geom.y())
            self.sideWindow.showFullScreen()
            self._dialog.actionDisplay_side_screen.setChecked(True)
            # self._dialog.milongaSource.activateWindow()
            # self.setFocus(True)
        else:
            # print("will hide side screen")
            # self.sideWindow.showNormal()
            self.sideWindow.hide()
            self._dialog.actionDisplay_side_screen.setChecked(False)

    def _handelFullScren(self):
        if not self.isFullScreen():
            self.showFullScreen()
        else:
            self.showNormal()

    def _updateSideScreen(self, lastsong=False):

        # update size depending on the lentgh of the text.
        #
        # print("in side sceen updating")

        if self.curTango is not None:
            nextTanda = self.getNextTanda();
            # print("type : "+str(self.curTango.type))
            self.sideContent.labelArtist.setText(self.curTango.artist)
            if self.curTango.type == 4:
                self.sideContent.labelType.setText(self.TYPE[self.curTango.type][1].upper())
            else:
                if not self._isMilongaPlaying:
                    self.sideContent.labelType.setText(self.TYPE[self.curTango.type][1].upper())
                else:
                    self.sideContent.labelType.setText(self.TYPE[self.curTango.type][1].upper() + " - " + str(
                        nextTanda['nbintanda'] - nextTanda['num'] + 1) + "/" + str(nextTanda['nbintanda']))

            if self.curTango.year == 0:
                self.sideContent.labelTitle.setText(self.curTango.title)
            else:
                self.sideContent.labelTitle.setText(self.curTango.title + " ( " + str(self.curTango.year) + " )")

            if not self._isMilongaPlaying:
                self.sideContent.labelNextTanda.setText("LIST PLAYING :-)")
            elif nextTanda['type'] == 'last':
                self.sideContent.labelNextTanda.setText("LAST TANDA :-(")
            else:
                # self.sideContent.labelNextTanda.setText("NEXT TANDA ( "+str(nextTanda['num'])+")""  |  "+str(nextTanda['type']))
                self.sideContent.labelNextTanda.setText("NEXT TANDA  |  " + str(nextTanda['type']))

            R = self.TYPE[self.curTango.type][2]
            G = self.TYPE[self.curTango.type][3]
            B = self.TYPE[self.curTango.type][4]
            T = self.TYPE[self.curTango.type][5]
            # self.prefContent.selectColorButton.setStyleSheet("background-color: rgba("+str(R)+","+str(G)+","+str(B)+","+str(T)+")")
            self.sideContent.frameType.setStyleSheet(_fromUtf8(
                "QFrame{\n  background-color: rgba(" + str(R) + "," + str(G) + "," + str(B) + "," + str(
                    T) + ");\n border: 0px;\n  margin-right: 0px;\n    margin-bottom: 0px;\n margin-left: 0px;\n spacing: 0px;\n padding: 0px;\n} \nQFrame::layout { margin: 0px }"))

            # self.sideContent.frameType.setStyleSheet(_fromUtf8("QFrame{\n  background-color: rgba("+str(R)+","+str(G)+","+str(B)+","+str(T)+");\n border: 0px;\n  margin-right: 0px;\n    margin-bottom: 0px;\n margin-left: 0px;\n spacing: 0px;\n padding: 0px;\n} \nQFrame::layout { margin: 0px }")
            self._updateLabelSize()

    def _updateLabelSize(self):
        size1 = 100
        size2 = 70
        nextTandaSize = 70
        recalculate = True
        coef = 0.9

        while recalculate:

            font1 = QFont("sans", size1)
            font2 = QFont("sans", size2)
            metrics = QFontMetrics(font2)

            if metrics.boundingRect(str(self.sideContent.labelTitle.text())).width() > self.sideWindow.width() * coef:
                recalculate = True
            else:
                recalculate = False

            if not recalculate:
                metrics = QFontMetrics(font1)

                if metrics.boundingRect(self.sideContent.labelArtist.text()).width() > self.sideWindow.width() * coef:
                    recalculate = True
                elif metrics.boundingRect(self.sideContent.labelType.text()).width() > self.sideWindow.width() * coef:
                    recalculate = True
                else:
                    recalculate = False

            if recalculate:
                size1 = size1 - 1
                size2 = round(size1 * 0.7)

        recalculate = True
        while recalculate:
            font1 = QFont("sans, bold", nextTandaSize)
            metrics = QFontMetrics(font1)
            if metrics.boundingRect(self.sideContent.labelNextTanda.text()).width() > self.sideWindow.width() * coef:
                recalculate = True
            else:
                recalculate = False

            nextTandaSize -= 1

        self.sideContent.labelArtist.setStyleSheet(_fromUtf8(
            "QLabel{\n margin-top: 30px;\n margin-left: 20px;\n margin-bottom: 25px;\n  font-weight: bold;\n color: white;\n font-size: " + str(
                size1) + "px;\n   font-family: \"sans\"\n}"))
        self.sideContent.labelType.setStyleSheet(_fromUtf8(
            "QLabel{\n  background-color: \"transparent\";\n font-weight: bold;\n    color: white;\n font-size: " + str(
                size1 - 3) + "px;\n margin-left: 20px;\n    font-family: \"sans\"\n}"))

        self.sideContent.labelTitle.setStyleSheet(_fromUtf8(
            "QLabel{\n  margin-left: 20px;\n    color: white;\n font-size: " + str(
                size2) + "px;\n  font-family: \"sans\"\n}"))
        self.sideContent.labelNextTanda.setStyleSheet(_fromUtf8(
            "QLabel{\n font-family: \"sans\";\n  font-weight: bold;\n color: white;\n font-size: " + str(
                nextTandaSize) + "px;\n}"))

    def getNbSongInCurTanda(self):

        count = self.curLibraryRow
        index = self.destModel.index(count, 5)
        # print ("startingrow: "+str(index.row()))

        num = 0

        currentType = self.destModel.data(index, Qt.DisplayRole)

        while currentType == self.destModel.data(index, Qt.DisplayRole) and count + 1 <= self.destModel.rowCount(
                QModelIndex()):
            # curi = self.destModel.index(count, 0)
            # print("type: "+currentType+" nb: "+str(num)+" row: "+str(index.row())+" ID: "+str(self.destModel.data(curi, Qt.DisplayRole)))

            num += 1
            count += 1
            index = self.destModel.index(count, 5)
        # print("num song before backward: "+str(num))

        count = self.curLibraryRow - 1
        index = self.destModel.index(count, 5)
        # currentType = self.destModel.data(index, Qt.DisplayRole)
        # print (index.row())
        while currentType == self.destModel.data(index, Qt.DisplayRole) and count + 1 < self.destModel.rowCount(
                QModelIndex()) and index.row() > -1:
            # curi = self.destModel.index(count, 0)
            # print("type: "+currentType+" nb: "+str(num)+" row: "+str(index.row())+" ID: "+str(self.destModel.data(curi, Qt.DisplayRole)))

            num += 1
            count -= 1
            index = self.destModel.index(count, 5)

        # print("nb song: "+str(num))
        return num

    def getNextTanda(self):
        ret = {}
        ret['nbintanda'] = self.getNbSongInCurTanda()
        count = self.curLibraryRow
        # print("count before while: "+str(count))
        numSong = 0
        index = self.destModel.index(count, 5)
        currentType = self.destModel.data(index, Qt.DisplayRole)
        while currentType == self.destModel.data(index, Qt.DisplayRole) and count + 1 <= self.destModel.rowCount(
                QModelIndex()):
            # print("count: "+str(count)+" size model: "+str(self.destModel.rowCount(QModelIndex())))
            numSong += 1
            count += 1
            # index = self.destModel.index(count, 0)
            # print("tangoID: "+str(self.destModel.data(index, Qt.DisplayRole)))
            index = self.destModel.index(count, 5)

        # print("count after while: "+str(count))
        # if count+1 >= self.destModel.rowCount(QModelIndex()):
        # print ("It's the LAST TANDA !")

        # print ("current Type = "+str(currentType))

        if numSong == 1:
            ret['num'] = 1
        else:
            ret['num'] = numSong
        if self.destModel.data(index, Qt.DisplayRole) == 'Cortina':
            index = self.destModel.index(count + 1, 5)
            ret['type'] = self.destModel.data(index, Qt.DisplayRole).upper()
        elif count + 1 >= self.destModel.rowCount(QModelIndex()):
            ret['type'] = 'last'
        else:
            ret['type'] = self.destModel.data(index, Qt.DisplayRole).upper()
        return ret


# ----------------------------------
# Run the Audio Player !
# ----------------------------------
app = QApplication(sys.argv)
musicPlayer = AudioPlayerDialog()
app.exec_()
