#!/usr/bin/python3
# -*- coding:Utf-8 -*

import os
import time

from djtango.data import djDataConnection
from djtango.tangosong import TangoSong
from djtango.shutil import copyfile
import unicodedata, re


djData = djDataConnection()

tangoList = djData.getAllTangos()

for tango in tangoList:
	if tango.artist == "TANGO":
		#print (tango.title + " "+ tango.artist)	
		res = tango.title.split('-')
		if len(res) >1:
			#print (res[0].strip()+" - "+res[1].strip())
			tango.title = res[0].strip()
			tango.artist = res[1].strip()
			print (tango.title+" | "+tango.artist)
			djData.updateTango(tango)
			#print(res)
