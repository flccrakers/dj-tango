#!/usr/bin/python3
# -*- coding:Utf-8 -*

from djtango.data import djDataConnection
from djtango.tangosong import TangoSong
import os

#listOfTango = []
djhome = os.path.join(os.path.expanduser("~"), ".djtango")
djData = djDataConnection(djhome)
TYPE = djData.getTangoTypeList()


def getFormatedNb(nb):
	if (nb<1000):
		nb = ' '+str(nb)
	elif (nb<100):
		nb = '  '+str(nb)
	elif (nb<10):
		nb = '   '+str(nb)
	else:
		nb = str(nb)

	return nb

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
multiChoice = 0
noMatched = []


for tango in listOfTango:
	#print (tango.list())
	rows = djData.existTangoInTangoDatabase(tango)#if exist in el-recodo database
	#print(rows)
	if len(rows) == 0: #If we can't find this tango in el-recodo database
		#print(tango.listUpdateDB())
		noMatching+=1
		noMatched.append(tango)
	elif len(rows) == 1: #if only one tango is corresponding to el-recodo database (better case)
		matched+=1
		row = list(rows[0])
		#print(row)
		if tango.year < 10 or tango.year>1990:
		#if tango.year >=0:
			for i in range (0, len(row)):
			#print(row[i])
				if(row[i] == '?' or row[i] == '' or row[i] == ' '):
					row[i] = 'Unnkown'
			
			#print(tango.listUpdateDB())
			#print ("will update date, composer, singer")
			#print("row: ")
			#print(rows[0])
			tango.year = row[7]
			tango.singer = row[10]
			tango.composer = row[11]
			tango.author = row[12]
			#print ("tango modifié : "+str(tango.listUpdateDB()))
			#print()
			djData.updateTango(tango)
		if tango.type == 5:
			tango.type = getTypeFromName(row[6])
			#print(row[6]+" -> "+str(getTypeFromName(row[6])))

			djData.updateTango(tango)


	else: #if we have more than one tango
		#print (tango.title+" | "+tango.artist)
		#print(rows)
		#for row in rows:
		#	print (row)
		#print ("multiple choice, we will to have to treat this correctly");
		multiChoice+=1

		#for row in rows:
		#	print("\t - "+str(row[7]))

count = 0
fichier = open("./tobecorrected.csv", "w")
for tango in noMatched:
	tList = tango.list()
	#if tList[5] <4 and not (tList[3].lower() == 'miguel calo'):
	
	if tList[5] <4 :
		count+=1
		print(tango.listUpdateDB())
		#print ('{0:10}  {1:30}  {2:30}  {3:2}'.format(str(tList[0]), tList[2].lower(), tList[3].lower(), tList[5]))
		fichier.write("%s;%s;%s\n" % (str(tList[0]),tList[2].lower(),tList[3].lower()))
	
fichier.close()

print("\n-------------------------------")


altCor = noMatching-count
total = altCor+count+matched+multiChoice

altCor = getFormatedNb(altCor)
total = getFormatedNb(total)
multiChoice = getFormatedNb(multiChoice)

print("#alt. cort.:\t"+altCor)
print("#noMatch:\t"+str(count))
print("#Corrected:\t"+str(matched))
print("#MultiChoice:\t"+multiChoice)
print('----------------------------------')
print("TOTAL: \t\t"+total)

#print ("\n"+str(noMatching-count)+" alternatif or cortina "+ str(count)+" noMaching and "+str(matched)+" matched on "+str(noMatching+matched))

