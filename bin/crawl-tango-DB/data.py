# -*- coding: utf-8 -*-

import sqlite3
#from tangosong import TangoSong

class DBtangoConnexion:
	def __init__(self):
		self.path = 'tangodatabase.db'
		self.typeList = {}

	def createDatabase(self):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()
		# create a table
		cursor.execute("""CREATE TABLE tangos
			(ID INTEGER PRIMARY KEY ASC, title text, artist text, album text, 
			genre text, year integer, singer text, composer text, author text) 
			""")
		conn.commit()
		conn.close()




	def insertSong(self, song):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()
		song = list(song)
		song[0] = song[0].split('-')[0]
		
		if self.existTango(song):
			return

		sql = "INSERT INTO tangos (year,artist, title,singer, genre, composer, author) VALUES(?,?,?,?,?,?,?)"
		cursor.execute(sql, song)

		
		conn.commit()
		conn.close()		

	def existTango(self, tango):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		sql = "SELECT * FROM tangos WHERE year =? and artist =? and title =? and singer =? and genre =? and composer =? and author =?"
		#print (sql)
		#print (tango.path)

		cursor.execute(sql, tango)
		rows = cursor.fetchall()

		conn.commit()
		conn.close()		

		if len(rows) > 0:
			return True
		else:
			return False

#OLD funciton, DON NOT USE (TO BE REMOVED IN PRODUCTION)

	

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
		sql = "INSERT INTO tangos (path, title, artist, album, genre, year) VALUES(?,?,?,?,?,?)"
		cursor.execute(sql, tango.listDB())
		print ("inserting "+str(tango.path))

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
		duration = ?
		WHERE ID = ? """
		#print (tango.listUpdateDB())
		cursor.execute(sql, tango.listUpdateDB())

		conn.commit()
		conn.close()

	def deleteTango(self, ID):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()	
		
		print("deleting tange ID "+str(ID))
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


	def updateProperties(self, durationFadOut, fadoutTime, writeTagBox, TYPE):
		print("I will update the database for preferences")
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		sql = """UPDATE preferences 
		SET timeCortina = ?,
		timeFadOut = ?,
		writeID3tag = ? """
		
		cursor.execute(sql, (fadoutTime/1000, durationFadOut/1000, writeTagBox))
		
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
		for row in rows:
			ret['path'] = row[0]
			ret['cortinaDuration'] = row[1]
			ret['fadoutTime'] = row[2]
			ret['writeTag'] = row[3]
			
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

	
