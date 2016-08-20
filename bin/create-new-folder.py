#!/usr/bin/python3
# -*- coding:Utf-8 -*

import os
import time

from djtango.data import djDataConnection
from djtango.tangosong import TangoSong
from djtango.shutil import copyfile
import unicodedata, re

p = re.compile('(\/|\:|\.)')
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
def removeOddCaracters(input_str):
	output = input_str.replace('/', '')
	output = output.replace(':', '')
	output = output.replace('.', '')
	return output

root = "/home/hoonakker/media/tango-propres-HQ"
djData = djDataConnection()

tangoList = djData.getAllTangos()
TYPE=djData.getTangoTypeList()

for tango in tangoList:
	#print(tango.path)
	filename, file_extension = os.path.splitext(tango.path)
	name = str(tango.year)+"-"+removeOddCaracters(tango.title)+"-"+remove_accents(tango.artist).upper()+"-"+remove_accents(tango.album).upper()+"-"+TYPE[tango.type][1].upper()+file_extension
	if tango.type == 4:
		rep = os.path.join(root, "CORTINA")
	elif tango.type < 4:
		rep = os.path.join(root, "TANGO", remove_accents(tango.artist).upper())

	elif tango.type >5 :
		rep = os.path.join(root, "ALTERNATIF", remove_accents(tango.artist).upper())
	#print (rep)
	
	if not os.path.isdir(rep):
		os.makedirs(rep)


	count = 1
	while os.path.isfile(os.path.join(rep, name)):
		count+=1
		name = str(tango.year)+"-"+removeOddCaracters(tango.title)+"_"+str(count)+"-"+remove_accents(tango.artist).upper()+"-"+remove_accents(tango.album).upper()+"-"+TYPE[tango.type][1].upper()+file_extension
	if count > 1:
		#print(str(tango.ID)+" "+name)
		print (str(tango.ID)+" "+name+ " already exist, we have to change the name")
	#if not os.path.isfile(os.path.join(rep, name)):


	try:
		djData.updatePath(tango.ID, os.path.join(rep, name))
		copyfile(tango.path, os.path.join(rep, name))
	except:
		print("Something bad happen with "+tango.path)
	
	
	#else:
	
