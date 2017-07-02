#!/usr/bin/python3
# -*- coding:Utf-8 -*-

from djtango.data import djDataConnection
from djtango.dirsong import dirSong
import string, os

djhome = os.path.join(os.path.expanduser("~"), ".djtango")
djData = djDataConnection(djhome)

tangoList = dirSong('/home/hoonakker/media/tango-propres-HQ', False)
tangoList.loadTangos(djData.getAllTangos())
fileOnHD = tangoList.getListFromDir()
tangos ={}
for ID in tangoList.tangos:
	#print (tangoList.tangos[ID].path)
	tangos[tangoList.tangos[ID].path] = ID

tmp = {}
for file in fileOnHD:
	if file in tangos and file in tmp:
		tmp[file]+=1
		print (tmp[file])
	else:
		tmp[file] = 1
		#print (tmp[file])

isredundancy  = False
for file in tmp:
	if tmp[file]>1:
		isredundancy = True
	#else:
	#	print(file+" "+str(tmp[file]))
		

if isredundancy:
	print("this file appear twice: "+file)
else:
	print ("No redundancy")


