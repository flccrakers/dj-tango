#!/usr/bin/python
# -*- coding:Utf-8 -*-

import urllib
from bs4 import BeautifulSoup
from pprint import pprint
from data import DBtangoConnexion



#page : template de la page

def getSongsFromPage(page, url):
	soup = BeautifulSoup(page, "lxml")


	uls = soup.find_all('ul')
	maxNB = 1
	for i,ul in enumerate(uls):
		#print(ul['class'])
		if  'pagination' in ul['class']:
			#print("in pagination")
			first = True
			for li in ul.select('li'):
				#print (li.select('a').text)
				if first:
					first = False
				else:
					for a in li.select('a'):
						if not a.text == '':
							if int(a.text) > int(maxNB):
								maxNB = int(a.text)
							#print (a.text)

	print ("NB de page: "+str(maxNB))
	
	currentPage = 1
	songs = []
	while int(currentPage) <= int(maxNB):
		#print (str(currentPage)+" sur "+str(maxNB))
		if currentPage>1:
			
			url = url+"&P="+str(currentPage)
			#print ("traitement page suivante\n"+url)
			fp = urllib.urlopen(url.encode('ascii','ignore'))
			soup = BeautifulSoup(fp.read(),"lxml") 
		
		tables = soup.select("table") #get all tables

		
		for i,table in enumerate(tables):
			for tr in table.select("tr"):
				song = ("hello",)
				first = True
				second = True
				for td in tr.select("td"):
					if first:
						#song = (td.text,)
						first = False
					elif second :
						song = (td.text,)
						second = False
					else: 
						song = song + (td.text,)
				if len(song) >1:
					#print (song)
					#exit(0)
					songs.append(song)
		currentPage+=1



	print("nb de chansons: "+str(len(songs)))
	return (songs)

def getListOfOrchestra(page):
	soup = BeautifulSoup(page, "lxml")

	#print (soup.find_all('a'))

	tables = soup.select("table") #get all tables
	orchestraList = []
	for i,table in enumerate(tables):
		for tr in table.select("tr"):
			for td in tr.select("td"):
				for a in td.select("a"):
					#print("http://www.el-recodo.com/"+a.get('href')+'&p=1')
					orchestraList.append("http://www.el-recodo.com/"+a.get('href'))

	return orchestraList

#****************************************
#
# MAIN

rootPage = "https://www.el-recodo.com/music?page=O&tri=&P=0&lang=fr#";

fp = urllib.urlopen(rootPage)
dbData = DBtangoConnexion()
dbData.createDatabase()
songs=[]


orchestraList = getListOfOrchestra(fp.read())
banned = ['http://www.el-recodo.com/#',
'http://www.el-recodo.com/music?page=O&tri=&P=1&lang=fr',
'http://www.el-recodo.com/music?page=O&tri=0&P=0&lang=fr',
'http://www.el-recodo.com/music?page=O&tri=O&P=0&lang=fr',
'http://www.el-recodo.com/music?page=O&tri=Q&P=0&lang=fr',
'http://www.el-recodo.com/music?id=&lang=fr']
#exit(0)
for orchestra in orchestraList:
	
	if (orchestra not in banned):
		#print ('will not test this one')
	
	#else:
		print (orchestra)
		#print ('will test')
		try:
			fp = urllib.urlopen(orchestra.encode('ascii','ignore'))
		
		except IOError:
			print ("problem with the orchestra !!!!")
			fp = None
		if fp:
			for song in (getSongsFromPage(fp.read(), orchestra)):
				#songs.append(song)
				#print (song)
				dbData.insertSong(song)
	


'''
#orchestra = "http://www.el-recodo.com/music?O=Francisco CANARO&lang=fr"
orchestra = "http://www.el-recodo.com/music?O=Jorge CASAL"
fp = urllib.urlopen(orchestra.encode('ascii','ignore'))
if fp:
	for song in (getSongsFromPage(fp.read(), orchestra)):
		songs.append(song)
		dbData.instertSong(song)

'''



print("taille: "+str(len(songs)))

#pprint(songs)












