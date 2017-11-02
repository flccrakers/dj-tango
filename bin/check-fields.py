#!/usr/bin/python3
# -*- coding:Utf-8 -*

from djtango.data import djDataConnection
from djtango.tangosong import TangoSong
import os

#listOfTango = []
djhome = os.path.join(os.path.expanduser("~"), ".djtango")
djData = djDataConnection(djhome)
TYPE = djData.getTangoTypeList()

def getTypeFromName(name):
	ret = 5
	for i in range (1, len(TYPE)):
		#print(name+" is equal to "+TYPE[i][1].upper())
		if TYPE[i][1].upper() == name:
			ret = i
	return ret


#tangoInDB = djData.getAllTangInTangoDatabase()

listOfTango = djData.getAllTangos()
noMatching = 0
matched = 0
noMatched = []


for tango in listOfTango:
	#print (tango.list())
	rows = djData.existTangoInTangoDatabase(tango)
	#print(rows)
	if len(rows) == 0:
		#print("no matching with: "+str(tango.list()))
		noMatching+=1
		noMatched.append(tango)
	elif len(rows) == 1:
		matched+=1
		#print(rows[0])
		#djdata.updateTitleArtistInTangoDatabase(rows[0][0], rows[0][2], rows[0][1])
		if tango.year < 10 or tango.year>1990:
			print ("will update date")
			tango.year = rows[0][5]
			djData.updateTango(tango)
		if tango.type == 5:
			tango.type = getTypeFromName(rows[0][4])
			print(rows[0][4]+" -> "+str(getTypeFromName(rows[0][4])))

			djData.updateTango(tango)


	else:
		print (tango.title+" | "+tango.artist)
		#print(rows)
		for row in rows:
			print (row)
		print ("multiple choice, we will to have to treat this correctly");
		matched+=1
		for row in rows:
			print("\t - "+str(row[5]))

count = 0
fichier = open("./tobecorrected.csv", "w")
for tango in noMatched:
	tList = tango.list()
	#if tList[5] <4 and not (tList[3].lower() == 'miguel calo'):
	
	if tList[5] <4 :
		count+=1
		#print ('{0:10}  {1:30}  {2:30}  {3:2}'.format(str(tList[0]), tList[2].lower(), tList[3].lower(), tList[5]))
		fichier.write("%s;%s;%s\n" % (str(tList[0]),tList[2].lower(),tList[3].lower()))
	
fichier.close()

print ("\n"+str(noMatching)+ "("+str(count)+") noMaching and "+str(matched)+" matched on "+str(noMatching+matched))

