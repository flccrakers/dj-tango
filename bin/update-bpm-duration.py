# -*- coding:Utf-8 -*-

from djtango.tangosong import TangoSong
from djtango.dirsong import dirSong
from djtango.data import djDataConnection

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

import os, sys, time, threading, operator, re
import gi

djData = djDataConnection()
tangoList = djData.getAllTangos()

TYPE=djData.getTangoTypeList()
count = 0
countNU = 0
tagedFileNB =0
lenght = len(tangoList)
for tango in tangoList:
	count+=1
	

	if not os.path.isfile(tango.path):
		djData.deleteTango(tango.ID)
	elif float(tango.bpmFromFile) <1:
		before = tango.bpmFromFile
		
		
		
	#else:
		#print("")
		#print(tango.bpmFromFile)
		countNU+=1
		name, ext = os.path.splitext(tango.path)

		try:
			audio = MP3(tango.path, ID3=EasyID3)
			tango.duration = audio.info.length*1000 #convert into milliseconds
			tango.bpmFromFile = float(audio['bpm'][0].replace(',','.'))

			#if tango.ID == 218:
			#	print("IN !!!!!!!!!!!!!!")
			#	print("bpm: "+str(tango.bpmFromFile))


			after = tango.bpmFromFile
			if tango.bpmFromFile >1:
				sys.stdout.write(" updating ID ("+str(tango.ID)+") "+str(count)+" on "+str(lenght)+" - "+str(tango.title)+" - "+str(tango.album)+"                     "+chr(13))
				tango.writeTags(TYPE)
				djData.updateTango(tango)
				tagedFileNB+=1
		except Exception as err:
			pass
	else:
		sys.stdout.write(" pass ID "+str(tango.ID)+"                                            "+chr(13))		

	#if count>200: sys.exit(0)
print("number of remaning file not tagged: "+str(countNU-tagedFileNB))



