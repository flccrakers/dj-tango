# -*- coding: utf-8 -*-

import sqlite3, os

from djtango import utils
from djtango.tangosong import TangoSong

class djDataConnection:
	def __init__(self, home):
		print(home)
		if not os.path.isdir(home):
			os.makedirs(home)
		
		self.path = os.path.join(home, 'djtango.db')
		self.pathTangoDatabase = os.path.join(home,'el-recodo.db')
		self.typeList = {}
	def getDataFromSql(self, sqlfile):
		ret = ""
		with open(sqlfile) as file:
			for line in file:
				ret+=line

		return ret
	def createDatabase(self):
		open(self.path, 'w').close()
		open(self.pathTangoDatabase, 'w').close
		
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()
		
		#create the table
		script = self.getDataFromSql('databaseCreation.sql')
		print (script)
		cursor.executescript(script)
		
		#fill the default table
		script = self.getDataFromSql('databaseFill.sql')
		print (script)
		cursor.executescript(script)

		
		
		
		conn.commit()
		conn.close()
		
	def existTangoInTangoDatabase(self, tango):
		conn = sqlite3.connect(self.pathTangoDatabase)
		cursor = conn.cursor()
		sql = "SELECT * FROM tangos WHERE norm_artist = ? and norm_title = ?"
		#print("SELECT * FROM tangos WHERE norm_artist = \""+utils.remove_accents(tango.artist).lower()+"\" AND norm_title = \""+utils.remove_accents(tango.title).lower()+"\"")

		cursor.execute(sql, (utils.remove_accents(tango.artist).lower(), utils.remove_accents(tango.title).lower()))
		rows = cursor.fetchall()
		
		conn.commit()
		conn.close()

		return rows

	def updateTitleArtistInTangoDatabase(self, ID, artist, title):
		conn = sqlite3.connect(self.pathTangoDatabase)
		cursor = conn.cursor()
		
		sql = """
		UPDATE tangos 
		SET norm_artist = ?, norm_title = ?
		WHERE ID = ? """
		#print (sql)
		cursor.execute(sql, (artist, title, ID))

		conn.commit()
		conn.close()


	def getAllTangInTangoDatabase(self):
		conn = sqlite3.connect(self.pathTangoDatabase)
		cursor = conn.cursor()

		sql = "SELECT ID, artist, title FROM tangos"
		cursor.execute(sql)
		rows = cursor.fetchall()


		conn.commit()
		conn.close()

		return rows


	def updatePath(self, ID, newpath):
		print(str(ID)+" "+newpath)
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()
		
		sql = """
		UPDATE tangos
		SET tangopath = ?
		WHERE ID = ? """
		#print (sql)
		cursor.execute(sql, (newpath, ID))
		#cursor.execute(sql, (ID,))

		conn.commit()
		conn.close()		

	def existTango(self, tango):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		sql = "SELECT * FROM tangos WHERE tangopath = ?"
		#print (sql)
		#print (tango.path)

		cursor.execute(sql, (tango.path,))
		rows = cursor.fetchall()

		conn.commit()
		conn.close()		

		if len(rows) > 0:
			return True
		else:
			return False

	def insertTango(self, tango):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		#don't insert a tango who already exist
		if self.existTango(tango):
			return

		if not self.typeList:
			sql = "SELECT * FROM tangoType"
			cursor.execute(sql)
			rows = cursor.fetchall()
			for row in rows:
				self.typeList[row[1]] = row[0]

		if str(tango.type).lower() in self.typeList:
			tango.type = self.typeList[str(tango.type).lower()]
		else:
			tango.type = self.typeList['unknown']
		sql = "INSERT INTO tangos (tangopath, title, artist, album, genre, year) VALUES(?,?,?,?,?,?)"
		cursor.execute(sql, tango.listDB())
		#print ("inserting "+str(tango.path))

		conn.commit()
		conn.close()

	#def insertManyTango(self, tangoList):
	#	conn = sqlite3.connect(self.path)
	#	cursor = conn.cursor()	
	#	sql = "INSERT INTO tangos (path, title, artist, album, genre, year) VALUES(?,?,?,?,?,?)"
	
	def getAllTangos(self):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		#sql = "SELECT tangos.ID, tangos.path, tangos.title, tangos.artist, tangos.album, tangoType.type, tangos.year \
		#FROM tangos, tangoType\

		#WHERE tangos.genre = tangoType.ID"
		sql = "SELECT * from tangos";
		cursor.execute(sql)
		rows = cursor.fetchall()
		conn.close()

		tangoList = []
		for row in rows:
			ctango = TangoSong(row[1], row[0])
			ctango.title = row[2]
			ctango.artist = row[3]
			ctango.album = row[4]
			ctango.type = row[5]
			if ctango.type == 0:
				ctango.type = 5
			ctango.year = row[6]
			ctango.bpmHuman = row[7]
			ctango.bpmFromFile = row[8]
			ctango.duration = row[9]

			tangoList.append(ctango)
			#print (ctango.type)
		return tangoList


	def getTangoFromMilonga(self, name):
		#print("in data geting milonga")
		ID = self.getMilongaID(name)
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		sql = "SELECT * FROM tangos, Milonga_Tango WHERE tangos.ID = Milonga_Tango.idTango AND Milonga_Tango.IdMilonga = "+str(ID)
		cursor.execute(sql)
		rows = cursor.fetchall()
		conn.close()

		tangoList = []
		for row in rows:
			#print(row)
			ctango = TangoSong(row[1], row[0])
			ctango.title = row[2]
			ctango.artist = row[3]
			ctango.album = row[4]
			ctango.type = row[5]
			if ctango.type == 0:
				ctango.type = 5
			ctango.year = row[6]
			ctango.bpmHuman = row[7]
			ctango.bpmFromFile = row[8]
			#print("duration in database: "+str(row[9]))
			ctango.duration = row[9]
			tangoList.append(ctango)
			#print (ctango.type)
		return tangoList

	def getTangoFromListID(self, listID):
		s = ','
		listIDstring = s.join(["'"+str(ID)+"'" for ID in listID])
		sql = "SELECT * FROM tangos WHERE ID IN ("+listIDstring+")"
		#print (sql)

		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		cursor.execute(sql)
		rows = cursor.fetchall()
		conn.close()

		tangoList = []
		for row in rows:
			#print(row)
			ctango = TangoSong(row[1], row[0])
			ctango.title = row[2]
			ctango.artist = row[3]
			ctango.album = row[4]
			ctango.type = row[5]
			if ctango.type == 0:
				ctango.type = 5
			ctango.year = row[6]
			ctango.bpmHuman = row[7]
			ctango.bpmFromFile = row[8]
			#print("duration in database: "+str(row[9]))
			ctango.duration = row[9]
			tangoList.append(ctango)
			#print (ctango.type)
		return tangoList



	def getTangoTypeList(self):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		typeList={}
		sql = "SELECT * FROM tangoType"
		cursor.execute(sql)
		rows = cursor.fetchall()
		conn.close()
		for row in rows:
			typeList[row[0]] = row
			#rint (row)
		return typeList

	def updateTango(self, tango):
		#print("will update tango")
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		
		sql = """
		UPDATE tangos 
		SET title = ?,
		artist = ?,
		album = ?,
		genre = ?,
		year = ?,
		bpmHuman = ?,
		bpmFromFile = ?,
		duration = ?,
		tangopath = ?
		WHERE ID = ? """
		#print (tango.listUpdateDB())
		cursor.execute(sql, tango.listUpdateDB())

		conn.commit()
		conn.close()

	def deleteTango(self, ID):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		
		print("deleting tango ID "+str(ID))
		sql = """
		DELETE FROM tangos
		WHERE ID = ? """
		#print (tango.listUpdateDB())
		cursor.execute(sql, [ID,])

		conn.commit()
		conn.close()

	def updateBPM(self, tango):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		
		sql = """
		UPDATE tangos 
		SET bpmHuman = ?
		WHERE ID = ? """
		#print (sql)
		cursor.execute(sql, (tango.bpmHuman, tango.ID))

		conn.commit()
		conn.close()


	def updateProperties(self, durationFadOut, fadoutTime, writeTagBox, normalize, TYPE):
		print("I will update the database for preferences")
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		sql = """UPDATE preferences 
		SET timeCortina = ?,
		timeFadOut = ?,
		writeID3tag = ?,
		normalize = ? """
		
		cursor.execute(sql, (fadoutTime/1000, durationFadOut/1000, writeTagBox, normalize))
		
		conn.commit()
		conn.close()
		#print (TYPE)

		#TODO : add a finction that update the type
		self.updateType(TYPE)

	def updateType(self, TYPE):

		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()
		print (TYPE)
		#print(TYPE.length)


		sql = """DELETE FROM tangoType"""
		cursor.execute(sql)

		#"INSERT INTO tangos (path, title, artist, album, genre, year) VALUES(?,?,?,?,?,?)"
		sql = "INSERT INTO tangoType (ID, type, R, G, B, T) VALUES(?,?,?,?,?,?)"
		for nb in TYPE:
			print (TYPE[nb][0])
			cursor.execute(sql, TYPE[nb])
			conn.commit()
	
		conn.close()

	def setNewSongAvailable(self, value):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()
		val = 0
		if value:
			val = 1

		sql = "UPDATE preferences SET newSongAvailable= "+val
		cursor.execute(sql)

		conn.commit()
		conn.colse()
		

	def getPreferences(self):
		ret={}
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		
		sql = "SELECT * FROM preferences"
		cursor.execute(sql)
		rows = cursor.fetchall()
		conn.close()
		print(rows)
		for row in rows:
			ret['path'] = row[0]
			ret['cortinaDuration'] = row[1]
			ret['fadoutTime'] = row[2]
			ret['writeTag'] = row[3]
			ret['normalize'] = row[4]
			
		return ret

	def getMilongaID(self, name):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		sql = "SELECT * FROM Milonga WHERE Name = ?"
		cursor.execute(sql, (name,))
		rows = cursor.fetchall()

		conn.commit()
		conn.close()		

		if len(rows) > 0:
			return rows[0][0]
		else:
			return 0

	def getListOfMilongas(self):
		ret = []
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		sql = "SELECT * FROM Milonga"
		cursor.execute(sql)
		rows = cursor.fetchall()

		conn.commit()
		conn.close()
		
		for row in rows:
			ret.append(row[1])
		return ret

	def deleteMilonga (self, milongaID=0, name=''):

		if milongaID == 0 and name == '':
			return False

		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		if milongaID == 0 and not name == '':
			milongaID = self.getMilongaID(name)
		#if milongaID > 0:

		sql="DELETE FROM Milonga WHERE ID = ?"
		cursor.execute(sql, (milongaID,))

		sql = "DELETE FROM Milonga_TANGO WHERE IdMilonga = ?"
		cursor.execute(sql, (milongaID,))

		conn.commit()
		conn.close()	
		return True

	def saveMilonga(self, name, tangoList):	
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()
		milongaID = self.getMilongaID(name)
		if milongaID >0:
			self.deleteMilonga(milongaID)
		
		sql = "INSERT INTO Milonga (Name) VALUES(?)"
		cursor.execute(sql, (name,))

		ID = cursor.lastrowid
		#print(ID)

		count = 1
		for tangoId in tangoList:
			sql = "INSERT INTO Milonga_Tango (IdMilonga, IdTango, Ord) VALUES(?,?,?)"
			cursor.execute(sql, (ID, tangoId, count))
			count+=1

		conn.commit()
		conn.close()	

	
