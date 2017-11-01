#!/usr/bin/python
# -*- coding:Utf-8 -*-
# Premier essai de script Python
# petit programme simple affichant une suite de Fibonacci, c.à.d. une suite
# de nombres dont chaque terme est égal à la somme des deux précédents.
import time
from datetime import date
import os
import zipfile 
import glob

today = date.today()

print today

filedate = "NameOfFile-"+str(today)
print filedate
rep = os.listdir(".")
print rep

os.mkdir(filedate) #create the directory to stor the file 


##########################################
#                                        #
# Fonction pour ziper un fichier ZIP     #
#                                        #
# filezip : le fichier d'archive à créer #
# pathzip : le repertoire à zipe         #
#                                        #
##########################################
def zipdirectory(filezip, pathzip): 
    lenpathparent = len(pathzip)+1   ## utile si on veut stocker les chemins relatifs 
    def _zipdirectory(zfile, path): 
        for i in glob.glob(path+'\\*'): 
            if os.path.isdir(i): _zipdirectory(zfile, i ) 
            else: 
                print i 
                zfile.write(i, i[lenpathparent:]) ## zfile.write(i) pour stocker les chemins complets 
    zfile = zipfile.ZipFile(filezip,'w',compression=zipfile.ZIP_DEFLATED) 
    _zipdirectory(zfile, pathzip) 
    zfile.close()
## END zipdirectory 


##########################################
#                                        #
# Fonction pour ziper un fichier ZIP     #
#                                        #
# filezip : le fichier d'archive à créer #
# pathzip : le repertoire à zipe         #
#                                        #
##########################################
def dezip(filezip, pathdst = ''): 
    if pathdst == '': pathdst = os.getcwd()  ## on dezippe dans le repertoire locale 
    zfile = zipfile.ZipFile(filezip, 'r') 
    for i in zfile.namelist():  ## On parcourt l'ensemble des fichiers de l'archive 
        print i 
        if os.path.isdir(i):   ## S'il s'agit d'un repertoire, on se contente de creer le dossier 
            try: os.makedirs(pathdst + os.sep + i) 
            except: pass 
        else: 
            try: os.makedirs(pathdst + os.sep + os.path.dirname(i)) 
            except: pass 
            data = zfile.read(i)                   ## lecture du fichier compresse 
            fp = open(pathdst + os.sep + i, "wb")  ## creation en local du nouveau fichier 
            fp.write(data)                         ## ajout des donnees du fichier compresse dans le fichier local 
            fp.close() 
## END dezp