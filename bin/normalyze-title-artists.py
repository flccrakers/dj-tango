#!/usr/bin/python3
# -*- coding:Utf-8 -*


from djtango.data import djDataConnection
import unicodedata, re
p = re.compile('(\s\(2\)| \(3\)| \(4\)| \(5\))')

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def normalize(tango):
	tango = list(tango)
	tango[1] = remove_accents(tango[1]).lower()
	tango[2] = remove_accents(tango[2]).lower()

	tango[1] = p.sub('', tango[1]) 
	tango[2] = p.sub('', tango[2]) 
	
	#djData.updateTitleArtistInTangoDatabase(tango[0], tango[1], tango[2])

	print (str(tango[0]) +" "+tango[1]+" "+tango[2])
	return(tango)


data = djDataConnection()
tangos = data.getAllTangInTangoDatabase()

for tango in tangos:
	tango = normalize(tango)
	data.updateTitleArtistInTangoDatabase(tango[0], tango[1], tango[2])