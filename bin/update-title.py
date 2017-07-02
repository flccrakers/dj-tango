#!/usr/bin/python3
# -*- coding:Utf-8 -*-

from djtango.data import djDataConnection
import string, os

djhome = os.path.join(os.path.expanduser("~"), ".djtango")

djData = djDataConnection(djhome)

Tangos = djData.getAllTangos()
#start = 3880
start = 3400

#print (Tangos)
for tango in Tangos:
	if tango.ID > start:
		tango.title = string.capwords(tango.title)
		tango.artist = string.capwords(tango.artist)

		#print (tango.title+" "+str(tango.ID)+" -> "+string.capwords(tango.title))
		print (tango.title)
		djData.updateTango(tango)
	
