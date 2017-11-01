#!/usr/bin/python3

import bs4
import urllib
import re
from bs4 import BeautifulSoup
from pprint import pprint
from data import DBtangoConnexion


def getSongsFromPage(page, url):
	soup = BeautifulSoup(page, "lxml")
	myul = soup.find("ul", {"class": "pagination"})
	print()
	print(url)
	pageNb = 0;
	songs =[];
	if myul != None:
		mylis = myul.findAll("li")
		if "ENREGISTREMENTS" in mylis[len(mylis)-2].a.next : 
			pageNb = 1
		else:
			#print (mylis[len(mylis)-2].a)
			pageNb = int(mylis[len(mylis)-2].a.next)

		print('pageNB: '+str(pageNb))
		curPage = 1
		while curPage <= pageNb:
			print("reading page " +str(curPage))
			mytrs = soup.findAll('tr', {"class": "small"})
			for tr in mytrs:
				song = []
				tds = tr.findAll("td")
				#print(str(tds[4].a.next)+' | '+str(tds[5].next))
				song = [tds[1].a.next,tds[2].a.next,tds[3].a.next,tds[4].a.next,tds[5].next+tds[5].span.next,tds[6].a.next]
				if isinstance(tds[4].a.next, bs4.element.Tag):
					song[3] =''
				if not isinstance(tds[7].a.next, bs4.element.Tag):
					song.append(tds[7].a.next)
				else:
 					song.append('?')
				
				for i, curVal in enumerate(song):
					if isinstance(curVal, bs4.element.Tag):
						song[i] = ''
				#print(song)

				songs.append(song)

			curPage+=1
			url = orchestra = re.sub(r'P=\d+','P='+str(curPage), url)
			print(url)
			fp = urllib.request.urlopen(url)
			soup = BeautifulSoup(fp.read(), "lxml")


	else:
		print("Pas d'enregistrement pour "+url)
	#exit(0);
	return songs;

def getListOfOrchestra(page):
	soup = BeautifulSoup(page, "lxml")
	mytds = soup.findAll("td", { "class" : "perso-graph-td perso-graph-tdcategorie text-right" })
	orchestraList = []
	for td in mytds:
		if td.a != None: 
			#print (td.a['href'])
			

			query = td.a['href'].split('?')[1]
			#query = td.a['href']
			params = urllib.parse.parse_qs(query)
			for i in params:
				#print (params[i][0])
				params[i] =params[i][0]
				params[i] = params[i].encode('Utf-8')
			params['P'] = '1'.encode('Utf-8')
			#print(urllib.parse.urlencode(params))
			fullUrl = "https://www.el-recodo.com/music?"+urllib.parse.urlencode(params)
			#ó %C3%B3
			#fullUrl.replace('%C3%B3','ó');
			fullUrl = str(fullUrl)
			#fullUrl = quote(fullUrl, safe="%/:=&?~#+!$,;'@()*[]")
			print (fullUrl)
			orchestraList.append(fullUrl)

	
	return orchestraList

#****************************************
#
# MAIN

rootPage = "https://www.el-recodo.com/music?page=O&tri=O&P=0&lang=fr#";

fp = urllib.request.urlopen(rootPage)
#<a href="music?O=Adolfo CARABELLI&amp;tri=&amp;P=0&amp;lang=fr">Adolfo CARABELLI <span class="label label-default">58</span></a>
dbData = DBtangoConnexion()
#dbData.createDatabase()
songs=[]
orchestraList = getListOfOrchestra(fp.read())
banned = ['http://www.el-recodo.com/#',
'http://www.el-recodo.com/music?page=O&tri=&P=1&lang=fr',
'http://www.el-recodo.com/music?page=O&tri=0&P=0&lang=fr',
'http://www.el-recodo.com/music?page=O&tri=O&P=0&lang=fr',
'http://www.el-recodo.com/music?page=O&tri=Q&P=0&lang=fr',
'http://www.el-recodo.com/music?id=&lang=fr']


for orchestra in orchestraList:

	
	
	#print(fp.read())
	#exit(0)
	#query = urllib.parse.quote(url)
	#query = urllib.parse.urlencode(url)

	#print(query)
	
	try:
		#params = { "SendXML": "<company><User><Username>username</Username><Password>passweord</Password></User><Content Type=sms>.." }
		#orchestra = orchestra % (urllib.parse.urlencode(params))
		fp = urllib.request.urlopen(orchestra)
	except IOError:
		print ("problem with the orchestra !!!!")
		fp = None
	if fp:
		for song in (getSongsFromPage(fp.read(), orchestra)):
			#songs.append(song)
			print (song)
			dbData.insertSong(song)
