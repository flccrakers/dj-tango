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
outF.write('title, artist, album, type, year, bpmHuman, bpmFromFile, duration, path, tstart, tend,author, singer, composer,treated, ID'+"\n")
for tango in tangos:
	if os.path.isfile(tango.path):
		size = os.path.getsize(tango.path)
	else:
		size = 0
	print(tango.listUpdateDBTxt());
	tango = tango.listUpdateDBTxt()
	for i in range(len(tango)):
		if tango[i] == None:
			tango[i] = 'Unknown'
	tango[3] = TYPE[int(tango[3])][1]
	s = ','
	outF.write(s.join(tango)+"\n")




