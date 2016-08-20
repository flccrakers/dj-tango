#!/usr/bin/python3
# -*- coding:Utf-8 -*-

from djtango.data import djDataConnection
from djtango.dirsong import dirSong
import string

djData = djDataConnection()

tangoList = dirSong('/home/hoonakker/media/tango-propres-HQ', False)
tangoList.loadTangos(djData.getAllTangos())
missed = tangoList.getMissedFiles()
missedFiles = tangoList.getMissedFiles(True)

for miss in missed:
	print (miss)
for file in missedFiles:
	print("FILE NOT IN DB: "+file)

if len(missed) == 0 and len(missedFiles) == 0:
	print("No missing file")
else:
	print("nb of file in the database without a real file: "+str(len(missed)))
	print("nb of file wich are not in the database: "+str(len(missedFiles)))
