# -*- coding: utf-8 -*-

import os, mimetypes, re
from djtango import utils
from djtango.tangosong import TangoSong
from shutil import move

#from PyQt4.phonon import Phonon
#import glob 

class dirSong:
	def __init__(self, cpath = '', fill=False, progressBar = None):
		self.songpath = cpath
		self.listFiles ={}
		self.tangos ={}
		self.progress = progressBar
#		self.acceptedMime = self.getAcceptedMime()
		#self.acceptedFileExt={'.mp3', '.flac', '.wav', '.aiff', '.ogg'}
		if fill:
			self.fillListOfFile()

#	def getAcceptedMime(self):
#		ret = {}
#		mime_types = Phonon.BackendCapabilities.availableMimeTypes()
#		for songtype in mime_types:
#			res = re.search("audio/(.+)", songtype) 
#			if res is not None :
#				#print(songtype)
#				ret[songtype] =1
#		return ret


	def fillListOfFile(self):
		count = 0
		for root, dirs, files in os.walk(self.songpath):
			for i in files:
				name, ext = os.path.splitext(i)
				if ext.lower() in utils.acceptedFileExt:
					count+=1
		total = count
		count = 0
		self.progress.setMaximum(total)
		#self.progress.setWindowModality(Qt.WindowModal);
		for root, dirs, files in os.walk(self.songpath):
			for i in files:
				name, ext = os.path.splitext(i)
				if ext.lower() in utils.acceptedFileExt:
					count+=1
					self.progress.setValue(count)
					self.listFiles[os.path.join(root, i)] = count
					self.tangos[count] = TangoSong(os.path.join(root, i), count, True)
	
	def getListFromDir(self):
		#print ("in getListFromDir : "+self.songpath)
		count = 0
		ret = {}
		mime = mimetypes.MimeTypes()
		for root, dirs, files in os.walk(self.songpath):
			for file in files:
				#print (os.path.join(root, file))
				#print (mime.guess_type(os.path.join(root, file)))
				count+=1
				name, ext = os.path.splitext(file)
				#if ext in mimetypes.types_map.keys():
					#print(mimetypes.types_map[ext.lower()])
				if ext.lower() in utils.acceptedFileExt:
					ret[os.path.join(root, file)] = count
		return ret

	def loadTangos(self, tangos):
		
		for t in tangos:
			self.tangos[t.ID] = t
			self.listFiles[t.path] = t.ID

	def checkNewFiles(self):
		ret = []
		#print ("size of curFileList : "+str(len(self.tangos)))
		newfiles = self.getListFromDir()
		#print ("size of newFileList : "+str(len(newfiles)))
		if not len(self.tangos) == len(newfiles):
			for key in newfiles.keys():
				if not key in self.listFiles:
					#print ("file to add : "+key)
					ret.append(key)
		return ret

	def getMissedFiles(self, realfiles = False):
		ret=[]
		if realfiles:
			files = self.getListFromDir()
			#print ("files: "+str(len(files)))
			for file in files:
				isin = True
				try:
					c = self.listFiles[file]
					#print (file)
				except:
					isin = False
			if not isin:
				ret.append[file]
			
		else:
			for i in self.tangos:
				tango = self.tangos[i]
				if not os.path.isfile(tango.path):
					ret.append(tango.path)
					print (str(i))
				

		
		return ret

# this function will take a tango and verify if the naming correspond to the norm and if the folders are corrects.
# if not, it will noralazi it
# root is the root folder where tango are stored
	def normalizeTango(self, Tid, TYPE):
		#print("try to normalise")
		tango = self.tangos[Tid]
		filename, file_extension = os.path.splitext(tango.path)
		#root = self.songpath
		name = str(tango.year)+"-"+utils.removeOddCaracters(tango.title)+"-"+utils.remove_accents(tango.artist).upper()+"-"+utils.remove_accents(tango.album).upper()+"-"+TYPE[tango.type][1].upper()+file_extension

		if tango.type == 4:
			rep = os.path.join(self.songpath, "CORTINA")
		elif tango.type < 4:
			rep = os.path.join(self.songpath, "TANGO", utils.remove_accents(tango.artist).upper())
		elif tango.type >5 :
			rep = os.path.join(self.songpath, "ALTERNATIF", utils.remove_accents(tango.artist).upper())
		else:
			rep = os.path.join(self.songpath, "UNKNOWN")

		if not os.path.isdir(rep):
			os.makedirs(rep)

		if not os.path.isfile(os.path.join(rep, name)):
			#print("here I should create a new file")
			del(self.listFiles[tango.path])
			move(tango.path, os.path.join(rep, name))
		#else:
			#pass
			#print ("it seems that the new file created already exist, I will do nothing")
		self.tangos[Tid].path = os.path.join(rep, name)
		self.listFiles[tango.path] = tango.ID
		self.checkEmptyDir()

	#will remove the empty dir
	def checkEmptyDir(self):
		for root, dirs, files in os.walk(self.songpath):
			#print (root)
			#print(dirs)
			try:
				os.rmdir(root)
			except OSError:
				pass
		#print (files)
			#for directory in dirs:
				#os.rmdir()
				#print(directory)






