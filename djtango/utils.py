# -*- coding:Utf-8 -*-
import unicodedata
acceptedFileExt={'.mp3', '.flac', '.wav', '.aiff', '.ogg'}


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
def removeOddCaracters(input_str):
	output = input_str.replace('/', '')
	output = output.replace(':', '')
	output = output.replace('.', '')
	return output
def msecToms(msec):
	#print ("msec: "+str(msec))
	#print(type(msec))
	if type(msec) is not float and type(msec) is not int:
		#msec = 0
		return msec #we asume that the value is already a string set to the right value
	m,s=(0,0)
	if msec >= 0:
		sec = msec / 1000
		q,s=divmod(sec,60)
		h,m=divmod(q,60)
	return "%.2d:%.2d" %(m,s)

def msecTohms(msec):
	if type(msec) is not float and type(msec) is not int:
		msec = 0
	h,m,s=(0,0,0)
	if msec >= 0:
		sec = msec / 1000
		q,s=divmod(sec,60)
		h,m=divmod(q,60)
	return "%.2d:%.2d:%.2d" %(h,m,s)

def msecToHouMin(msec):
	if type(msec) is not float and type(msec) is not int:
		msec = 0
	h,m=(0,0)
	if msec >= 0:
		sec = msec / 1000
		q,s=divmod(sec,60)
		h,m=divmod(q,60)
	return "%.1d h %.2d min" %(h,m)


