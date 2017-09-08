#!/usr/bin/python3
# -*- coding:Utf-8 -*-


from djtango.data import djDataConnection
from pydub import AudioSegment

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

import os, sys, time, threading, operator, re
#import gi

djhome = os.path.join(os.path.expanduser("~"), ".djtango")
djData = djDataConnection(djhome)
tangoList = djData.getAllTangos()

TYPE=djData.getTangoTypeList()
count = 0
countNU = 0
tagedFileNB =0
lenght = len(tangoList)
for tango in tangoList:
	count+=1
	print(str(tango.ID)+" - "+tango.path)
	
	if not os.path.isfile(tango.path):
		djData.deleteTango(tango.ID)
	else :
	
		countNU+=1
		ext = os.path.splitext(tango.path)[1][1:]

		try:
			song = AudioSegment.from_file(tango.path, ext.lower())

			tango.duration=len(song)
			#print(tango.duration)
			djData.updateTango(tango)
		except Exception as err:
			print(err)
			pass

	#if count>200: sys.exit(0)
print("number of remaning file not tagged: "+str(countNU-tagedFileNB))



