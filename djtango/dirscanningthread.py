# -*- coding: utf-8 -*-

import time
from random import randint
from djtango import utils
from djtango.tangosong import TangoSong
from djtango.dirsong import dirSong
from djtango.data import djDataConnection
from PyQt5.Qt import QMutex, pyqtSignal, QObject, pyqtSlot
#from PyQt5.QtCore import pyqtSignal


class dirScan(QObject):
	scanned = pyqtSignal(list,list)
	def __init__(self, tangoList, djData, parent = None):
		super(dirScan, self).__init__(parent)
		print("initialize dirScan for Thread")
		self.tangoList = tangoList
		self.emitted = False
		self.djData = djData

	def workOut(self):
		#print("running DirScanningThread")
		while True:
			#print("SCANNING !!!!")
			if not self.emitted:
				newfiles = self.tangoList.checkNewFiles()
			
				if newfiles:
					#print("Nb of new tango: "+str(len(newfiles)))
					datas = []
					#firstID = 0
					tangos = []
					for path in newfiles:
						print("\n\nWORKING AND NON BLOQUING\n\n")
						#insert automatiquement un nouveau fichier et met à jour la liste
						insertedtango = TangoSong(path, 0, True)
						insertedID = self.djData.insertTango(insertedtango)
						#if firstID == 0:
						#	firstID = insertedID
						insertedtango.ID = insertedID
						#print("ID: "+str(insertedID)+" id in tango: "+str(insertedtango.ID))
						tangos.append(insertedtango)
						data = insertedtango.list()
						datas.append(data)
					print("nb: "+str(len(datas))+" "+str(len(tangos)))
					self.scanned.emit(datas, tangos)
			else:
				print("############################################\n#################################################\nI know that you are working on file, so I do nothing")

			time.sleep(10)

	@pyqtSlot(bool)
	def setUpdatingStatus(self, status ):
		self.emitted = status

	@pyqtSlot(dirSong)
	def updateTangoList(self, tangoList):
		self.tangoList = tangoList

    


