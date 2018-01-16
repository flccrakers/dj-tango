#!/usr/bin/python3
# -*- coding:Utf-8 -*

import os

from djtango.data import djDataConnection
from djtango.tangosong import TangoSong
djhome = os.path.join(os.path.expanduser("~"), ".djtango")


data = djDataConnection(djhome)
tangos = data.getAllTangos()
TYPE = data.getTangoTypeList()
#print(TYPE)
outF = open('tango-database.csv', "w")
outF.write('title, artist, album, type, year, bpmHuman, bpmFromFile, duration, path, tstart, tend,author, singer, composer, ID'+"\n")
for tango in tangos:
	if os.path.isfile(tango.path):
		size = os.path.getsize(tango.path)
	else:
		size = 0
	tango = tango.listUpdateDBTxt()
	tango[3] = TYPE[int(tango[3])][1];
	#print (tango[8].replace('/home/hoonakker/media/tango-propres-HQ/', ''))
	#tango[8] = tango[8].replace('/home/hoonakker/media/tango-propres-HQ/', '')
	tango.append(str(size))
	print(str(size))
	s = ','
	outF.write(s.join(tango)+"\n")
	#print(tango.listUpdateDB())




