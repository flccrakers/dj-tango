#!/usr/bin/python3
# -*- coding:Utf-8 -*

from djtango.data import djDataConnection
from djtango.tangosong import TangoSong
import os, time, sys

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

def getProgress(progress, size, total):
	factor = progress/total
	endRange = round(size*factor)
	#print (factor)
	start = '   ['
	for i in range(0,endRange):
		start+='#'
	for i in range(0,size-endRange):
		start+='_'
	start+=']'
	
	print(start, end='\r', flush=True)
	if factor == 1: print()


def getStatistics(tangos):
	print('counting ...');
	noMatching = 0
	matched = 0
	multiChoice = 0
	count = 0
	cnt = 0
	size = 25
	total = len(tangos)
	for tango in tangos:
		cnt+=1;
		getProgress(cnt, size, total)
		
		rows = djData.existTangoInTangoDatabase(tango)#if exist in el-recodo database
		if len(rows) == 0: #If we can't find this tango in el-recodo database
			noMatching+=1
		elif len(rows) == 1:
			noMatching+=1
		elif tango.year < 10 or tango.year>1990:
			multiChoice+=1

	for tango in noMatched:
		tList = tango.list()
	#if tList[5] <4 and not (tList[3].lower() == 'miguel calo'):
	
		if tList[5] <4 :
			count+=1
#tangoInDB = djData.getAllTangInTangoDatabase()
	print('counting DONE')
	return [noMatching, matched, multiChoice, count]

def printResum(values):
	(noMatching, matched, multiChoice, count) = values
	print("\n-------------------------------")


	altCor = noMatching-count
	total = altCor+count+matched+multiChoice

	altCor = getFormatedNb(altCor)
	total = getFormatedNb(total)
	multiChoice = getFormatedNb(multiChoice)

	print("# alt. cort.:\t"+altCor)
	print("# noMatch:\t"+str(count))
	print("# matched:\t"+str(matched))
	print("# MultiChoice:\t"+multiChoice)
	print('----------------------------------')
	print("TOTAL: \t\t"+total)




#**********************************************
# MAIN
#**********************************************

#print(sys.argv)
ARGV = sys.argv
#print(ARGV)
if ARGV[1] == 'true':
	shouldAskCorrection = True
else:
	shouldAskCorrection = False

#print (shouldAskCorrection)
listOfTango = djData.getAllTangos()
noMatching = 0
matched = 0
multiChoice = 0
noMatched = []
stats = [0,0,0,0,0]
if shouldAskCorrection:
	stats = getStatistics(listOfTango)
treatedMultiChoice = 0
#printResum()
print('Starting analyzing')
cnt = 0
size = 25
for tango in listOfTango:
	#print (tango.list())
	cnt+=1;
	getProgress(cnt, size, len(listOfTango))
	
	#if cnt > 4: cnt = 0
	

	rows = djData.existTangoInTangoDatabase(tango)#if exist in el-recodo database
	#print(rows)
	if len(rows) == 0: #If we can't find this tango in el-recodo database
		noMatching+=1
		noMatched.append(tango)
	elif len(rows) == 1: #if only one tango is corresponding to el-recodo database (better case)
		matched+=1
		row = list(rows[0])
		if tango.year < 10 or tango.year>1990:
			for i in range (0, len(row)):
				if(row[i] == '?' or row[i] == '' or row[i] == ' '):
					row[i] = 'Unnkown'
			tango.year = row[7]
			tango.singer = row[10]
			tango.composer = row[11]
			tango.author = row[12]
			#djData.updateTango(tango)
		if tango.type == 5:
			tango.type = getTypeFromName(row[6])

		djData.updateTango(tango)


	elif tango.year < 10 or tango.year>1990: #if we have more than one tango
		if shouldAskCorrection:
			print("\n"+'treated: '+str(treatedMultiChoice)+' , remaining: '+str(stats[2]-treatedMultiChoice))
			count = 0
			print (str(count)+' - NONE ! TAKE ME TO THE NEXT')
			for row in rows:
				count+=1
				print (str(count)+' - '+str(row))
			print (str(22)+' - Change some fields')
			#print ("multiple choice, we will to have to treat this correctly");
		
			cmdvlc = 'vlc -q "'+tango.path+'" &'
			cmdFirefox = ('firefox "https://www.el-recodo.com/music?T='+row[2]+'&G=&O='+row[4]+'&C=&Dmin=&Dmax=&Cr=&Ar=&L=&lang=fr" &')
			os.system('killall vlc')

			#print (cmdFirefox)
			os.system('wmctrl -a firefox')
			time.sleep(0.5)
			os.system(cmdFirefox)
			time.sleep(0.5)
			os.system('xdotool key Ctrl+Tab')
			time.sleep(0.5)
			os.system('xdotool key Ctrl+w')
			os.system(cmdvlc)
			time.sleep(5)
			#print (val)
			print()
			while True:
				try:
					val = int(input("Which one correspond ?: "))       
				except ValueError:
					print("Not an integer!")
					continue
				else:
					break 

			if val >0 and val != 22:
				row = list(rows[val-1])
				print(row)
				#exit(0)
				for i in range (0, len(row)):
					if(row[i] == '?' or row[i] == '' or row[i] == ' '):
						#print(row[i])
						row[i] = 'Unnkown'
					tango.year = row[7]
					tango.singer = row[10]
					tango.composer = row[11]
					tango.author = row[12]
				if tango.type == 5:
					tango.type = getTypeFromName(row[6])
				djData.updateTango(tango)
			elif val == 22:
				print('will change some fields')
				acceptedFields = ['author','singer','artist','album','title','year']
				for key in vars(tango):
					if key in acceptedFields:
						#print (key+ ' ['+str(getattr(tango, key))+']: ')
						value = input(key+ ' ['+str(getattr(tango, key))+']: ')
						if value != '':
							print (value)
							setattr(tango, key, value)
						#	tango.artist = value
				print(tango.listUpdateDB())
				djData.updateTango(tango)
			else:
				tango.year = 11 # in this case, we will not ask for this tango, until the value is <10 again
				djData.updateTango(tango)

			#print('wmctrl -a firefox; xdotool key Ctrl+w;')
			#os.system('wmctrl -a firefox')
			#time.sleep(0.5)
			#os.system('xdotool key Ctrl+w')
			

			treatedMultiChoice+=1

		if shouldAskCorrection:
			os.system( 'clear' )
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
		row  = tango.listUpdateDB()
		print(tango.listUpdateDB())
		cmdFirefox = ('firefox "https://www.el-recodo.com/music?T='+row[0]+'&G=&O='+row[1]+'&C=&Dmin=&Dmax=&Cr=&Ar=&L=&lang=fr" &')
		print (cmdFirefox)
		#print ('{0:10}  {1:30}  {2:30}  {3:2}'.format(str(tList[0]), tList[2].lower(), tList[3].lower(), tList[5]))
		fichier.write("%s;%s;%s\n" % (str(tList[0]),tList[2].lower(),tList[3].lower()))
	
fichier.close()


printResum([noMatching, matched, multiChoice, count])

#print ("\n"+str(noMatching-count)+" alternatif or cortina "+ str(count)+" noMaching and "+str(matched)+" matched on "+str(noMatching+matched))

