BEGIN TRANSACTION;
CREATE TABLE "tangos" (
	`ID`	INTEGER,
	`tangopath`	text,
	`title`	text,
	`artist`	text,
	`album`	text,
	`genre`	integer,
	`year`	integer DEFAULT 0,
	`bpmHuman`	REAL DEFAULT 0,
	`bpmFromFile`	REAL DEFAULT 0,
	`duration`	INTEGER DEFAULT 0,
	`singer`	INTEGER,
	`composer`	INTEGER,
	`author`	INTEGER,
	PRIMARY KEY(ID)
);
CREATE TABLE tangoType
			(ID INTEGER PRIMARY KEY ASC, type text, R integer, G integer, B integer, 
			T integer);
CREATE TABLE "preferences" (
	`baseDir`	text DEFAULT 'none',
	`timeCortina`	integer DEFAULT 46,
	`timeFadOut`	integer DEFAULT 6,
	`writeID3Tag`	integer DEFAULT 0,
	`normalize`	INTEGER DEFAULT 0,
	`newSongAvailable`	INTEGER DEFAULT 0
);
CREATE TABLE `people` (
	`ID`	INTEGER,
	`firstname`	TEXT,
	`lastname`	TEXT,
	`normfirstname`	TEXT,
	`normlastname`	TEXT,
	`birthdate`	INTEGER DEFAULT 0,
	`birthplace`	TEXT,
	PRIMARY KEY(ID)
);
CREATE TABLE Milonga_Tango (IdMilonga INTEGER, IdTango INTERGER, Ord Integer);
CREATE TABLE 'Milonga' (ID INTEGER PRIMARY KEY ASC, Name text);
COMMIT;
