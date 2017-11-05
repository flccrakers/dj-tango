#!/usr/bin/python3
# -*- coding:Utf-8 -*


# use pydub to detect the silences at the begining and the end of a song
# and save the real begining and end of each song in the database

from djtango.data import djDataConnection
from pydub import AudioSegment
from pydub import silence
import pydub

import unicodedata, re, os, sys
#p = re.compile('(\s\(2\)| \(3\)| \(4\)| \(5\))')
def backspace(n):
    # print((b'\x08').decode(), end='')     # use \x08 char to go back
    #clear()

    toPrint = ''
    for i in range(0,n):
    	toPrint+=' '
    print(toPrint, end='\r') 

def clear():

    os.system( 'clear' )
    print()


djhome = os.path.join(os.path.expanduser("~"), ".djtango")

data = djDataConnection(djhome)
tangos = data.getAllTangos()
sizeBackSpace = 1000;

startworkat = 4814
tangoCount = 0
cont = 1
size = 3
#count = 0
for tango in tangos:
	tangoCount+=1
	#count+=1
	#sys.stdout.flush()

	#printing infos
	backspace(sizeBackSpace)
	percent = tangoCount*100/len(tangos)
	start = '   ['+"%.0f" % percent+'% '
	for i in range(0,cont):
		start+='.'
	for i in range(0,size-cont):
		start+=' '
	start+='] - '
	cont+=1
	if cont >size: cont = 1;
	toPrint = start+str(tango.ID) + " - "+tango.path 
	print(toPrint, end='\r', flush=True) 
	sizeBackSpace = len (toPrint)


	file_extension = os.path.splitext(tango.path)[1][1:]
	if tango.ID >= startworkat:
		try:
			song = AudioSegment.from_file(tango.path, file_extension.lower())
			silences = silence.detect_silence_start_end(song, 500, -56)
			if (len(silences) > 1):
				starttime = silences[0][1]
				stoptime = silences[len(silences)-1][0]
				tango.tstart = starttime
				tango.tend = stoptime
			elif len(silences) == 1:
				if (silences[0][0] == 0):
					tango.tstart = silences[0][1]
					tango.tend = len(song)
				elif silences[0][0] > len(song)*3/4:
					tango.tstart = 0
					tango.tend = silences[0][0]
			elif len(silences) == 0:
				tango.tstart = 0
				tango.tend = len(song)
			else:
				tango.tstart = 0
				tango.tend = 0
		
			tango.duration = len(song)

			data.updateTango(tango)
		except FileNotFoundError:
			print (start+"We can not find the file of "+str(tango.ID));
			backspace(sizeBackSpace)
			print(toPrint)
		except KeyboardInterrupt:
			backspace(sizeBackSpace)
			print(toPrint)
			print(start+"KeyboardInterrupt")
			exit(0)
		except pydub.exceptions.CouldntDecodeError as e:
			clear()
			backspace(sizeBackSpace)
			print(toPrint)
			print(start+"Can't Decode "+str(tango.ID)+" "+tango.path)
			
			pass
