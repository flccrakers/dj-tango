# -*- coding:Utf-8 -*-

from djtango.data import djDataConnection
import string

djData = djDataConnection()

Tangos = djData.getAllTangos()
#start = 3880
start = 1000

#print (Tangos)
for tango in Tangos:
	if tango.ID > start:
		tango.title = string.capwords(tango.title)
		#print (tango.title+" "+str(tango.ID)+" -> "+string.capwords(tango.title))
		print (tango.title)
		djData.updateTango(tango)
	
