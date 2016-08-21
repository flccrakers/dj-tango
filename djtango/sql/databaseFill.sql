BEGIN TRANSACTION;
INSERT INTO `tangoType` (ID,type,R,G,B,T) VALUES (1,'tango',0,160,176,80),
 (2,'vals',204,51,63,80),
 (3,'milonga',237,201,81,80),
 (4,'cortina',106,74,60,80),
 (5,'unknown',42,42,42,80);

INSERT INTO `preferences` (baseDir,timeCortina,timeFadOut,writeID3Tag,normalize,newSongAvailable) VALUES ('none',46,6,2,2,0);
COMMIT;
