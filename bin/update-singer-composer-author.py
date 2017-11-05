#!/usr/bin/python3
# -*- coding:Utf-8 -*-

# If we detect that singer, author or composer are null, we put Unknown
#
from djtango.data import djDataConnection
import string, os


djhome = os.path.join(os.path.expanduser("~"), ".djtango")

djData = djDataConnection(djhome)

Tangos = djData.getAllTangos()
#start = 3880
start = 0

#print (Tangos)
for tango in Tangos:
	if tango.ID > start:
		if not tango.singer:
			tango.singer = 'Unknown'
		if not tango.author:
			tango.author = 'Unknown'
		if not tango.composer:
			tango.composer = 'Unknown'
		


		#print (tango.title+" "+str(tango.ID)+" -> "+string.capwords(tango.title))
		print (tango.listUpdateDB())
		djData.updateTango(tango)
	
