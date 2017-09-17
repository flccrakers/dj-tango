#!/usr/bin/python3
# -*- coding:Utf-8 -*


# use pydub to detect the silences at the begining and the end of a song
# and save the real beginin and end of each song.

from djtango.data import djDataConnection
from pydub import AudioSegment
from pydub import silence

import unicodedata, re, os
#p = re.compile('(\s\(2\)| \(3\)| \(4\)| \(5\))')
djhome = os.path.join(os.path.expanduser("~"), ".djtango")

data = djDataConnection(djhome)
tangos = data.getAllTangos()

startworkat = 5513
#count = 0
for tango in tangos:
	#count+=1
	print(str(tango.ID) +" - "+tango.path)
	file_extension = os.path.splitext(tango.path)[1][1:]
	#print (file_extension)
	#acceptedext = []

	if tango.ID >= startworkat:
		#song = AudioSegment.from_mp3(tango.path)
		song = AudioSegment.from_file(tango.path, file_extension.lower())
		#print (len(song))
		silences = silence.detect_silence_start_end(song, 500, -56)
		print ("#of silences: "+str(len(silences)))
		if (len(silences) > 1):
			starttime = silences[0][1]
			stoptime = silences[len(silences)-1][0]
			print (str(starttime)+" "+str(stoptime))
			tango.tstart = starttime
			tango.tend = stoptime
		elif len(silences) == 1:
			print(silences)
			if (silences[0][0] == 0):
				tango.tstart = silences[0][1]
				tango.tend = len(song)
			elif silences[0][0] > len(song)*3/4:
				tango.tstart = 0
				tango.tend = silences[0][0]
		elif len(silences) == 0:
			print ("start to end")
			tango.tstart = 0
			tango.tend = len(song)
		else:
			print("something not clear, put to 0")
			tango.tstart = 0
			tango.tend = 0
		
		print (str(tango.tstart)+" "+str(tango.tend))
		tango.duration = len(song)

		#exit(0)
		data.updateTango(tango)

	#data.updateTitleArtistInTangoDatabase(tango[0], tango[1], tango[2])