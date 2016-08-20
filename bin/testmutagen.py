#!/usr/bin/python3
# -*- coding:Utf-8 -*-

from djtango.tangosong import TangoSong
from djtango.dirsong import dirSong
from djtango.data import djDataConnection
from djtango import utils

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

import os, sys, time, threading, operator, re, 
import gi

songpath = "/home/hoonakker/media/tango-propres"
#acceptedFileExt={'.mp3', '.flac', '.wav', '.aiff', '.ogg'}
count = 0
ret = {}

def extractTags(self, audio):
		self.duration = audio.info.length
		title = 'rien'
		album = 'rien'
		bpmFromFile = 0

		try:
			title = audio["title"][0]
			#artist = audio["artist"][0]
			#album = audio["album"][0]
			ctype = audio["genre"][0] #TODO: essayer de mapper le genre avec le TYPE défini dans la base. Metter à Unknow sinon
			year = audio["date"][0]
			author = audio["author"][0]
			bpmFromFile = audio["bpm"][0].replace(',','.')
			#print ("bpmFromFile: "+str(self.bpm))
		except Exception as err:
			print("Can't get the tag: "+str(err))
			if err == 'TBPM':
				bpmFromFile = 0

		print ("title: "+title)
		print ("album: "+album)
		print ("bpmFromFile: "+str(bpmFromFile))


def extractID3Tag(path):
		audio = None
		audio = MP3(path, ID3=EasyID3)
		duration = audio.info.length

		title = 'rien'
		album = 'rien'
		bpmFromFile = 0


		try: 
			
			title = audio["title"][0]
			artist = audio["artist"][0]
			album = audio["album"][0]
			ctype = audio["genre"][0]
			year = audio["date"][0]
			author = audio["author"][0]
			bpmFromFile= audio['bpm'][0].replace(',','.')
			#self.bpmFromFile = audio["bpm"][0] 
		
		except Exception as err:
			print("Can't get the tag: "+str(err))
			#if err == 'TBPM':
			#	bpmFromFile = 0

		print ("title: "+title)
		print ("album: "+album)
		print ("bpmFromFile: "+str(bpmFromFile))
			
		



def extractAnyTag(path):
		#acceptedFileExt={'.mp3', '.flac', '.wav', '.aiff', '.ogg'}
		name, ext = os.path.splitext(path)
		if ext.lower() in utils.acceptedFileExt and os.path.isfile(path):
			if ext.lower() == '.mp3':
				extractID3Tag(path)
			elif ext.lower() == '.flac':
				try:
					audio = FLAC(path)
					extractTags(audio)
				except:
					pass

			else:
				print("the file is a: "+ext)
				pass
		elif not os.path.isfile(self.path):
			print("unexisting file: "+str(self.path))
		else:
			print ("not an accepted file extention: "+ext)




for root, dirs, files in os.walk(songpath):
	for file in files:
		#print (os.path.join(root, file))
		#print (mime.guess_type(os.path.join(root, file)))
		count+=1 #set the ID
		name, ext = os.path.splitext(file)
		#if ext in mimetypes.types_map.keys():
		#print(mimetypes.types_map[ext.lower()])
		if ext.lower() in utils.acceptedFileExt:
			ret[os.path.join(root, file)] = count
			print (os.path.join(root, file))
			extractAnyTag(os.path.join(root, file))
			
