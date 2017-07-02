# -*- coding: utf-8 -*-
# TODO ajouter les liseur et ecrivain de tag pour tous les type de fichiers traités.
# TODO - ajouter compositeur (et pas seulement auteur)
# TODO - ajouter l'extraction du bpm pour chaque chanson (l'affichier éventuellement)

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
import os
import string
from djtango import utils



class TangoSong:
	def __init__(self, path, ID=0, extractTag = False):
		self.ID = ID
		self.path=path
		self.type=5
		self.artist='Unknown'
		self.title='Unknown'
		self.album='Unknown'
		self.year=0
		self.author = 'Unknown'
		self.duration = 0
		self.bpmHuman = 0
		self.bpmFromFile = 0
		#print (EasyID3.valid_keys.keys())
		#self.list = []
		
		#TODO, replace this by a function that extract tag according to the file type (mp3, flac, aiff, wave  etc)
		if extractTag:
			self.extractAnyTag()
		#if extractTag:
			#self.extractID3Tag()

	def titleFields(self):
		self.artist = self.artist.title()
		self.title = self.title.title()
		self.album = self.album.title()
		self.author = self.author.title()

	def extractAnyTag(self):
		
		name, ext = os.path.splitext(self.path)
		if ext.lower() in utils.acceptedFileExt and os.path.isfile(self.path):
			if ext.lower() == '.mp3':
				self.extractID3Tag()
			elif ext.lower() == '.flac':
				try:
					audio = FLAC(self.path)
					self.extractTags(audio)
				except:
					pass
			else:
				print("the file is a: "+ext)
				pass
		elif not os.path.isfile(self.path):
			print("unexisting file: "+str(self.path))
		else:
			print ("not an accepted file extention: "+ext)

	def extractTags(self, audio):
		
		try:
			self.duration = audio.info.length
			self.title = string.capwords(audio["title"][0])
			self.artist = audio["artist"][0]
			self.album = audio["album"][0]
			self.type = audio["genre"][0] #TODO: essayer de mapper le genre avec le TYPE défini dans la base. Mettre à Unknow sinon
			self.year = int(audio["date"][0])
			self.author = audio["author"][0]
			self.bpmFromFile = audio["bpm"][0].replace(',','.')
			#print ("bpmFromFile: "+str(self.bpm))
		except Exception as err:
			print("In path: "+self.path+"\nCan't get the tag: "+str(err)+"\n it will be set to the default value")


	def extractID3Tag(self):
		audio = None
		

		try: 
			audio = MP3(self.path, ID3=EasyID3)
			self.duration = audio.info.length
			self.title = string.capwords(audio["title"][0])
			self.artist = audio["artist"][0]
			self.album = audio["album"][0]
			self.type = audio["genre"][0]
			self.year = int(audio["date"][0])
			self.author = audio["author"][0]
			self.bpmFromFile = audio['bpm'][0].replace(',','.')
			
		except Exception as err:
			print("In path: "+self.path+"\nCan't get the tag: "+str(err)+"\n it will be set to the default value")

	def listDB(self):
		#print (self.type)
		return [self.path, self.title, self.artist, self.album, self.type, int(self.year) ]

	def list(self):
		bpm = 0
		if self.bpmHuman > 0:
			bpm = self.bpmHuman
		else:
			bpm = self.bpmFromFile
		return [self.ID, 0, self.title, self.artist, self.album, self.type, self.year, bpm, self.duration ]

	def sourceList(self):
		return [self.ID, self.title, self.artist, self.album, self.type]

	def listUpdateDB(self):
		return [self.title, self.artist, self.album, self.type, int(self.year), self.bpmHuman, self.bpmFromFile, self.duration, self.path, self.ID]


	def writeTags(self, TYPE):
		
		name, ext = os.path.splitext(self.path)
		if ext.lower() in utils.acceptedFileExt:
			if ext.lower() == '.mp3':
				try:
					audio = MP3(self.path, ID3=EasyID3)
					self.writeAnyTags(audio, TYPE)
				except:
					pass
			elif ext.lower() == '.flac':
				try:
					audio = FLAC(self.path)
					self.writeAnyTags(audio, TYPE)
				except:
					pass

			else:
				print("the file is a: "+ext)
				pass
		else:
			print ("not an accepted file extention: "+ext+" in "+self.path)

	def writeAnyTags(self, audio, TYPE):
		#print("will write the tags")
		#print(self.toString())
		#print(TYPE)
		#print (self.type)
		#genre = TYPE[self.type][1].title()
		#print ("GENRE !!!! :"+str(genre))
		try:
			audio['title'] = u""+self.title
			audio['artist'] = u""+self.artist
			audio['album'] = self.album
			audio['genre'] = u""+str(TYPE[self.type][1].title())
			audio['date'] = u""+str(self.year)
			audio['author'] = u""+self.author
			if self.bpmHuman > 0:
				audio['bpm'] = str(self.bpmHuman)
			else:
				audio['bpm'] = str(self.bpmFromFile)
			audio.save()
		except Exception as err:
			print (err)
			print ("can't write the tags for "+self.path)

	def writeID3Tag(self, TYPE):
		#print ("I'm writing the tags")
		try:
			
			audio['title'] = self.title
			audio['artist'] = self.artist
			audio['album'] = self.album
			audio['genre'] = str(TYPE[self.type][1].title())
			audio['date'] = str(self.year)
			audio['author'] = self.author
			if self.bpmHuman > 0:
				audio['bpm'] = self.bpmHuman
			else:
				audio['bpm'] = self.bpmFromFile

			audio.save()
		except Exception as err:
			print (err)
			print ("can't write the ID3 tags for "+self.path)
			#e = sys.exc_info()[0]
			#print (e)

	def toString(self):
		return " Path: "+str(self.path)+"\n Title: "+str(self.title)+"\n Album: "+str(self.album)+"\n Artist: "+str(self.artist)+"\n Author: "+str(self.author)+"\n Type: "+str(self.type)+"\n Année: "+str(self.year)+"\n bpmHuman: "+str(self.bpmHuman)+"\n bpmFromFile: "+str(self.bpmFromFile)+"\n Duration: "+str(self.duration)
