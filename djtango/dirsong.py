# -*- coding: utf-8 -*-

import os, mimetypes, re
from djtango import utils
from djtango.tangosong import TangoSong
from shutil import move

#from PyQt4.phonon import Phonon
#import glob 

class dirSong:
	def __init__(self, cpath = '', fill=False, progressBar = None, djData = None):
		self.songpath = cpath
		self.listFiles ={}
		self.tangos ={}
		self.progress = progressBar
		self.djData = djData
		if fill:
			self.fillListOfFile()
		

	#def getTangos(self):
	#	return self.tangos

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
		self.progress.setMinimum(0)
		self.progress.forceShow()
		abort = False;
		#self.progress.setWindowModality(Qt.WindowModal);
		for root, dirs, files in os.walk(self.songpath):
			for i in files:
				name, ext = os.path.splitext(i)
				if ext.lower() in utils.acceptedFileExt:
					count+=1
					self.progress.setValue(count)
					self.listFiles[os.path.join(root, i)] = count
					tmpTango = TangoSong(os.path.join(root, i), count, True)
					head, tail = os.path.split(tmpTango.path)
					self.progress.setLabelText("Importing Tangos, please be patient...\n"+str(count)+"/"+str(total)+"\n"+tail)#+str(count)+" / "+str(len(files)+"\n"+tail)
					self.tangos[count] = tmpTango
					self.djData.insertTango(tmpTango)
					if self.progress.wasCanceled():
						abort = True
						break;
				if abort:
					break;
			if abort:
				break;
		if abort:
			print("I have to delete the database and the file")
	
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
				else:
					print("this file hasn't the right extension: "+os.path.join(root, file))
		return ret

	def loadTangos(self, tangos):
		#check if the tango is not arleady existing and do someting with it
		#countExistingPath = {}
		for t in tangos:
			self.tangos[t.ID] = t
			if t.path in self.listFiles:
				print("hu ho, this path appear more than once: "+t.path+" Please check your file on remove it eventually")
			self.listFiles[t.path] = t.ID

	def addTango(self, t):
		#check if the tango is not arleady existing and do someting with it
		self.tangos[t.ID] = t
		self.listFiles[t.path] = t.ID
		#print ("adding a Tango")

	def removeTango(self, ID):
		t = self.tangos[ID]
		del self.tangos[ID]
		del self.listFiles[t.path]
		#print("removing")

	def checkNewFiles(self):
		ret = []
		print ("# of tangos in the database :\t"+str(len(self.tangos)))
		print("# of tangos in the table: \t"+str(len(self.listFiles)))
		newfiles = self.getListFromDir()
		print ("# of tangos on the Hard Drive :\t"+str(len(newfiles)))
		if not len(self.tangos) == len(newfiles):
			#print("les deux ne sont pas de la même taille")
			for key in newfiles.keys():
				if not key in self.listFiles:
					print ("file to add : "+key)
					ret.append(key)
		return ret

	def getMissedFiles(self, realfiles = False):
		ret=[]
		if realfiles:
			files = self.getListFromDir()
			print ("files on hard drive: "+str(len(files)))
			for file in files:
				if file in self.listFiles:
					pass
				else:
					ret.append(file)
		else:
			print ("files in database: "+str(len(self.tangos)))
			for i in self.tangos:
				tango = self.tangos[i]
				if not os.path.isfile(tango.path):
					ret.append(tango.path)
					print (str(i))
				

		
		return ret

# this function will take a tango and verify if the naming correspond to the norm and if the folders are corrects.
# if not, it will normalize it
# root is the root folder where tango are stored
	def normalizeTango(self, Tid, TYPE):
		#print("try to normalise")
		tango = self.tangos[Tid]
		filename, file_extension = os.path.splitext(tango.path)
		#root = self.songpath
		name = str(tango.year)+"-"+utils.removeOddCaracters(tango.title)+"-"+utils.remove_accents(tango.artist).upper()+"-"+utils.remove_accents(tango.album).upper()+"-"+TYPE[tango.type][1].upper()+file_extension

		name = utils.remvoveSlash(name) #be sure that no more slash are in the filename

		if tango.type == 4:
			rep = os.path.join(self.songpath, "CORTINA")
		elif tango.type < 4:
			rep = os.path.join(self.songpath, "TANGO", utils.remove_accents(tango.artist).upper())
		elif tango.type >5 :
			rep = os.path.join(self.songpath, "ALTERNATIF", utils.remove_accents(tango.artist).upper())
		else:
			rep = os.path.join(self.songpath, "UNKNOWN")

		#print("REP IS : "+rep)

		if not os.path.isdir(rep):
			os.makedirs(rep)

		if tango.title == "Unknown" and tango.artist == "Unknown":
			print ("It's unknown, I will not do anything")
		else:
			count = 2 
			while os.path.isfile(os.path.join(rep, name)):
				name = str(tango.year)+"-"+utils.removeOddCaracters(tango.title)+"_"+str(count)+"-"+utils.remove_accents(tango.artist).upper()+"-"+utils.remove_accents(tango.album).upper()+"-"+TYPE[tango.type][1].upper()+file_extension
				name = utils.remvoveSlash(name) #be sure that no more slash are in the filename
				count+=1;
			#print("here I should create a new file")
			if tango.path in self.listFiles: 
				del(self.listFiles[tango.path])
			else: 
				print("Warning: path did not exist in listFiles, I will not update it. Path: "+tango.path)
			
			print("Coying this file in the new directory")
			move(tango.path, os.path.join(rep, name))
		

			self.tangos[Tid].path = os.path.join(rep, name)
			self.tangos[Tid].titleFields()
			self.listFiles[tango.path] = tango.ID
			self.checkEmptyDir()


	#will remove the empty dir
	def checkEmptyDir(self):
		#TODO: check for files wich are not music and remove them
		for root, dirs, files in os.walk(self.songpath):
			#print (root)
			#print(dirs)
			for file in files:
				filename, file_extension = os.path.splitext(file)
				if file_extension.lower() not in utils.acceptedFileExt:
					#print("I should remvoe this file, but I'm still in testing mod so I'm waiting for my developper to add the proper function: "+os.path.join(root, file)) 
					os.remove(os.path.join(root, file))
				#else:
				#	print(os.path.join(root, file))
			try:
				os.rmdir(root)
			except OSError:
				pass
		#print (files)
			#for directory in dirs:
				#os.rmdir()
				#print(directory)






