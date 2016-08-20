#!/usr/bin/python3
# -*- coding:Utf-8 -*

import os
import time

from djtango.data import djDataConnection
from djtango.tangosong import TangoSong

inputFile = './tango-a-corriger.csv'

def loadcsv(file):
	ret=[]
	inF = open(file, "r") #opens file with name of "test.txt"
	for line in inF :
		res = line.strip().split(";")
		ret.append(res)
		#print(res)

	return ret
def printRest(tangoList):
	left = 0
	
	for index in range(1, len(tangoList)):
		table = tangoList[index]
		if table[3] == "":
			left+=1

	print(str(left)+" to inspect, "+str(len(tangoList)-left)+" checked, on a total of "+str(len(tangoList)))

def saveAndExit(file):
	outF = open(file, "w")
	s = ';'
	for i in range (0,len(tangoList)):
		outF.write(s.join(tangoList[i])+"\n")
		#outF.
	exit(0)

tangoList = loadcsv(inputFile)
printRest(tangoList)
#first = True
i = 1
curIndex = []
for index in range(1, len(tangoList)):
	table = tangoList[index]
	if table[3] == "":
		print(table)
		curIndex.append(index)
		command = "firefox \"http://www.el-recodo.com/music?T="+table[1].replace(" ", '+')+"&lang=fr\" &"
		#print (command)
		os.system(command)
		time.sleep(0.25)
		i+=1
		#else:
			#print("déjà corrigé "+str(i))

	if i>5:
		mdpe = input("une fois corrigé, appuyez sur entrer pour quitter et sauvegarder taper exit : ")
		print("mdpe is :" +mdpe)
			
			
		count = 0
		for x in curIndex:
				
			if mdpe == 'exit':
				saveAndExit(inputFile)
			elif mdpe[count] == 'c':
				print (tangoList[x])
				tangoList[x][3] = 'corrigé'
				print (tangoList[x])
			elif mdpe[count] == 'n':
				print (tangoList[x])
				tangoList[x][3] = "N’existe pas chez El Recodo" 
				print (tangoList[x])

			print("\n###########\n")		
			count+=1
		curIndex = []
		i = 1
			

