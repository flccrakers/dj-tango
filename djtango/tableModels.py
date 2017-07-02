# -*- coding:Utf-8 -*-

from PyQt5.Qt import QAbstractTableModel
from PyQt5.Qt import QSortFilterProxyModel
from PyQt5.QtCore import Qt
#from PyQt4.QtCore import QString
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QDataStream, QIODevice, QVariant
import operator, re
from PyQt5.QtCore import QRegExp
from djtango import utils
import decimal, random

#from PyQt4.QtGui import *

class library(QAbstractTableModel):
    def __init__(self, parent, mylist, header, TYPE, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
        self.TYPE = TYPE
        
    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role=Qt.DisplayRole):
    	if not index.isValid():
    		return None
    	elif role==Qt.BackgroundRole:
            R = self.TYPE[self.mylist[index.row()][5]][2]
            G = self.TYPE[self.mylist[index.row()][5]][3]
            B = self.TYPE[self.mylist[index.row()][5]][4]
            T = self.TYPE[self.mylist[index.row()][5]][5]
            return(QColor(R,G,B,T))
    	elif role != Qt.DisplayRole:
    		return None
    	
    	if index.column() == 4:
            return self.TYPE[self.mylist[index.row()][5]][1].title()
    	else:
    		return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
    	#print (self.header[col])
    	if orientation == Qt.Horizontal and role == Qt.DisplayRole:
    		return self.header[col]
    	if role==Qt.BackgroundRole:
    		return QColor(0,160,176,100)
    	return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.layoutAboutToBeChanged.emit()
        #self.emit(SIGNAL("layoutAboutToBeChanged()"))
        print (Qt.InitialSortOrderRole)
        print (order)
        self.mylist = sorted(self.mylist, key=operator.itemgetter(col))
        #self.
        if order == Qt.AscendingOrder:
        	self.mylist.reverse()
        #self.emit(SIGNAL("layoutChanged()"))
        self.layoutChanged.emit()
        
    #renew all the data of the table model
    #this can be very time consuming
    def changeData(self, datain):

        #self.emit(SIGNAL("LayoutAboutToBeChanged()"))
        self.layoutAboutToBeChanged.emit()
        self.mylist = datain

        #self.emit(SIGNAL("LayoutChanged()"))
        self.layoutChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        #self.emit(SIGNAL("DataChanged(QModelIndex,QModelIndex)"), self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))

    


    def setData(self, index, value, role):
    	#print ("I will try to change the data")
        if index.isValid() and role == Qt.EditRole:
            self.mylist[index.row()][index.column()] = value
            self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
            #self.emit(SIGNAL("DataChanged(QModelIndex,QModelIndex)"), index, index)
            return True
        return False
		#def setData()   


#=======================================================================
#
#
#
#========================================================================

class milongaSource(QAbstractTableModel):
    def __init__(self, parent, mylist, header, TYPE, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
        self.TYPE = TYPE
        
        
    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        if(len(self.mylist)>0):
            return len(self.mylist[0])
        else:
            return 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        elif role==Qt.BackgroundRole:
            #print("Background")
            #print(self.TYPE)
            #print(self.mylist[index.row()][5])
            if self.mylist[index.row()][5] in self.TYPE:
                R = self.TYPE[self.mylist[index.row()][5]][2]
                G = self.TYPE[self.mylist[index.row()][5]][3]
                B = self.TYPE[self.mylist[index.row()][5]][4]
                T = self.TYPE[self.mylist[index.row()][5]][5]
                return(QColor(R,G,B,T))
            else:
                return None
        elif role != Qt.DisplayRole:
            return None
        
        if index.column() == 5:#genre column
            #print("genre")
            #print (self.TYPE)
            #print (self.mylist[index.row()][5])
            if self.mylist[index.row()][5] in self.TYPE:
                return self.TYPE[self.mylist[index.row()][5]][1].title()
            else:
                return "Unknown"
        elif index.column() == 1:
            if self.mylist[index.row()][index.column()] == 0:
                return ''
            else:
                return '>>>'
        elif index.column() == 8:#time column
            return utils.msecToms(self.mylist[index.row()][index.column()])
        #elif index.column() == 6:
        #    return int(self.mylist[index.row()][index.column()])
        elif index.column() == 7: #bpm column
            return ('%.2f' % float(self.mylist[index.row()][index.column()]))
        else:
            return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        #print (self.header[col])
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        if role==Qt.BackgroundRole:
            return QColor(0,160,176,100)
        return None

    def sort(self, col, order):
        #print ("sorting")
        """sort table by given column number col"""
        self.layoutAboutToBeChanged.emit()
        #self.emit(SIGNAL("layoutAboutToBeChanged()"))
        #print (Qt.InitialSortOrderRole)
        #print(Qt.AscendingOrder)
        #print (col)
        self.mylist = sorted(self.mylist, key=operator.itemgetter(col))
        #self.
        if order == Qt.AscendingOrder:
            self.mylist.reverse()
        self.layoutChanged.emit()
        #pass
    def randomize(self):

        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        random.shuffle(self.mylist)
        self.emit(SIGNAL("layoutChanged()"))

    def changeData(self, datain):
        print ("I'm changing the data")

        self.layoutAboutToBeChanged.emit()
        print("after layoutAboutToBeChanged emited");
        self.mylist = datain
        self.layoutChanged.emit()
        print("after layoutChanged emited");
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        print("after dataChanged emited");

    #will add some data at the end of the table, updating the model at this point
    def addNewData(self, datas):

        self.layoutAboutToBeChanged.emit()
        for data in datas:
            self.mylist.append(data)
        self.layoutChanged.emit()
        self.dataChanged.emit(self.createIndex(self.rowCount(0)-len(datas), self.columnCount(0)-len(datas)), self.createIndex(self.rowCount(0), self.columnCount(0)))
        #print("will add new data at the end of the table")
        #index = self.createIndex(self.rowCount(0),0)
        #for row in newdatas:
        #    print(row)
        
    def setData(self, index, value, role):
        #print ("I will try to change the data with value: "+str(value))

        if index.isValid() and role == Qt.EditRole:
            #if index.column() == 8: #if it's the time
            #    value = utils.msecToms(value)
            #if index.column() == 7: #if it's the bpm column
            #    value = round(value,2)
            self.mylist[index.row()][index.column()] = value
            #self.emit(SIGNAL("DataChanged(QModelIndex,QModelIndex)"), index, index)
            self.dataChanged.emit(index, index)
            return True
        return False
        #def setData()
    def flags(self, index):
        #return Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsDropEnabled 
        return Qt.ItemIsDragEnabled | Qt.ItemIsEnabled | Qt.ItemIsSelectable

   

    #def 

#=======================================================================
#
#
#
#========================================================================

class milongaDest(QAbstractTableModel):
    def __init__(self, parent, mylist, header, TYPE, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
        self.TYPE = TYPE
        self.invertTYPE = self.invert(TYPE)
        self.startingRow=0
        
    def invert(self, TYPE):
        ret={}
        for key in TYPE.keys():
            #print(TYPE[key])
            ret[TYPE[key][1].title()] = TYPE[key]
        return ret
    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        elif role==Qt.BackgroundRole:
            R = self.TYPE[self.mylist[index.row()][5]][2]
            G = self.TYPE[self.mylist[index.row()][5]][3]
            B = self.TYPE[self.mylist[index.row()][5]][4]
            T = self.TYPE[self.mylist[index.row()][5]][5]
            return(QColor(R,G,B,T))
        elif role != Qt.DisplayRole:
            return None
        
        if index.column() == 5:
            return self.TYPE[self.mylist[index.row()][5]][1].title()
        elif index.column() == 1:
            if self.mylist[index.row()][index.column()] == 0:
                return ''
            else:
                return '>>>'
        elif index.column() == 8:#time column
            #print ("time: "+str())
            #print(self.mylist[index.row()][5])
            if (self.mylist[index.row()][5] == 4):
                return "-"
            else:
                return utils.msecToms(self.mylist[index.row()][index.column()])
        elif index.column() == 7: #bpm column
            #print("bpm:"+str(self.mylist[index.row()][index.column()])+"|")
            return ('%.2f' % float(self.mylist[index.row()][index.column()]))
        else:
            #print(self.mylist[index.row()][index.column()])
            return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        #print (self.header[col])
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        if role==Qt.BackgroundRole:
            return QColor(0,160,176,100)
        return None

    #def sort(self, col, order):
    #    """sort table by given column number col"""
    #    self.emit(SIGNAL("layoutAboutToBeChanged()"))
    #    print (Qt.InitialSortOrderRole)
    #    print (order)
    #    self.mylist = sorted(self.mylist, key=operator.itemgetter(col))
    #    #self.
    #    if order == Qt.AscendingOrder:
    #        self.mylist.reverse()
    #    self.emit(SIGNAL("layoutChanged()"))
    #    #pass
    def changeData(self, datain):
        self.layoutAboutToBeChanged.emit()
        self.mylist = datain
        
        self.layoutChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))

    def setData(self, index, value, role):
        #print("row: "+str(index.row())+" column: "+str(index.column()))
        #print("longeur de mylist: "+str(len(self.mylist[index.row()])))
        if index.isValid() and role == Qt.EditRole:
            self.mylist[index.row()][index.column()] = value
            #self.emit(SIGNAL("DataChanged(QModelIndex,QModelIndex)"), index, index)
            self.dataChanged.emit(index, index)
            #print (self.mylist)
            return True
        return False
    #def updatePlaying(self, row, column):
    #    self.mylist[row][col] = value
    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsDropEnabled 
        #return Qt.ItemIsDropEnabled | Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled

    def dropMimeData(self, data, action, row, column, parent):
        #print("action: "+str(action))

        self.layoutAboutToBeChanged.emit()
        if action == Qt.IgnoreAction:
            print ("ignoring")
            return True

        if not data.hasFormat("application/x-qabstractitemmodeldatalist"):
            print ("False Format")
            return False


        beginRow = -1

        if not row == -1:
            beginRow = row;
        elif parent.isValid():
            beginRow = parent.row()
        else:
            beginRow = self.rowCount(self)


        encodedData = data.data("application/x-qabstractitemmodeldatalist")
        data_items = self.decode_data(encodedData)

        #print ("number of line = " + str(int(len(data_items)/self.columnCount(parent))))
        lineNB = int(len(data_items)/self.columnCount(parent))



        if action == Qt.MoveAction:
            self.moveRow(self.startingRow,beginRow, parent)
        else:
            #print("ça viens de la source")
            #print("size: "+str(self.rowCount(self)))
            #print ("beginRow: "+str(beginRow))
            #if not beginRow+1 == self.rowCount(self):
            beginRow +=1
            if beginRow <= self.rowCount(self): curRow = 0
            else: curRow = -1

            for i in range(0, lineNB):
                self.insertRow(beginRow+i, parent)

            col = 0
            rowItem={}

            for data in data_items:
                if data['row'] not in rowItem.keys():
                    rowItem[data['row']] = data['row']


            #print("curRow: "+str(curRow))
            for key in sorted(rowItem.keys()):
                rowItem[key] = curRow
                curRow+=1
                print ("key: "+str(key)+" item: "+str(rowItem[key]))


            for data in data_items:
                #if data[0] == '':
                #    print (data[0])

                if data['column'] == 5 and data[0] in self.invertTYPE.keys():
                    data[0] = self.invertTYPE[data[0]][0]
                if data['column'] == 1:
                    data[0] = 0

                #print("want to add column: "+str(data['column']))
                #print("total column allowed: "+str(self.columnCount(parent)))
                idx = self.index(beginRow+rowItem[data['row']], data['column'], parent);
                #print("row to instert: "+str(idx.row()))
                self.setData(idx, data[0], Qt.EditRole);
                
                col+=1
    
            #self.reset()
            self.layoutChanged.emit()
            self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        return True

    def supportedDropActions(self):
        return Qt.MoveAction | Qt.CopyAction

    def pressed(self, index):
        #print ("mousse pressed")
        #print (index.row())
        self.startingRow = index.row()

    def moveRow(self, start, end, parent):
        tmp = self.mylist[start]
        #print (self.rowCount(parent))
        if end == self.rowCount(parent):
            self.insertRow(end,parent)
            self.mylist[end] = tmp[:]    
        else:
            self.insertRow(end+1,parent)
            self.mylist[end+1] = tmp[:]    
        
        if start>end:
            self.removeRows(start+1,1,parent)
        else:
            self.removeRows(start,1,parent)

        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))

    def insertRow(self, row, parent):

        before = self.mylist[:row]
        after = self.mylist[row:]
        line =[0]*len(self.header)
        if len(self.mylist) == 0 or len(after) == 0 :
            self.mylist.append(line)
        else:
            self.mylist = before[:]
            self.mylist.append(line)
            self.mylist.extend(after)
        return True

    def removeRows(self, row, count, parent):
        
        self.beginRemoveRows(parent, row, count);
        print ("will remove row "+str(row))

        before = self.mylist[:row]
        after = self.mylist[row+count:]
        #print (before)
        #print (after)
        #print ("before : "+str(len(before)))
        #print ("after : "+str(len(after)))
        
        if len(before) == 0:
            self.mylist = after[:]
        elif len(after) == 0:
            self.mylist = before[:]
        else: 
            self.mylist = before[:]
            self.mylist.extend(after)

        #print (self.mylist)
        #
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        #self.endRemoveRows()
        return True
    

    def decode_data(self, encodedData):
        data = []
        item = {}
        ds = QDataStream(encodedData, QIODevice.ReadOnly)
        while not ds.atEnd():
        
            row = ds.readInt32()
            column = ds.readInt32()
            map_items = ds.readInt32()
            item = {}
            for i in range(map_items):
                key = ds.readInt32()
                item[Qt.ItemDataRole(key)] = ds.readQVariant()
                item['row'] = row
                item['column'] = column
            data.append(item)
        return data



class sourceFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent):
        QSortFilterProxyModel.__init__(self, parent)
        self.artistRegExp = re.compile('.*', re.IGNORECASE)
        self.albumRegExp = re.compile('.*', re.IGNORECASE)
        self.genreRegExp = re.compile('.*', re.IGNORECASE)
        self.allRegExp = re.compile('.*', re.IGNORECASE)
        self.linefilter = '.*'

        #print (self.artistRegExp)

    def filterAcceptsRow(self, sourceRow, parent):
        ret = True
        indexArtist = self.sourceModel().index(sourceRow, 3, parent)
        indexAlbum = self.sourceModel().index(sourceRow, 4, parent)
        indexGenre = self.sourceModel().index(sourceRow, 5, parent)

        resArtist = self.artistRegExp.match(self.sourceModel().data(indexArtist))
        resAlbum = self.albumRegExp.match(self.sourceModel().data(indexAlbum))
        resGenre = self.genreRegExp.match(self.sourceModel().data(indexGenre))

        if self.linefilter == '.*':
            retAllfilter = 'YES'
        else:
            retAllfilter = None

            for i in range(0,7):
                index = self.sourceModel().index(sourceRow, i, parent)
                retLineFilter = self.allRegExp.match(str(self.sourceModel().data(index)))
                if retLineFilter is not None:
                    retAllfilter = 'YES'
        




        if resArtist is None or resAlbum is None or resGenre is None or retAllfilter is None:
            ret = False

        return ret
        
    def setlFilterValues(self, artistExp, albumExp, genreExp, linefilter):
        self.artistRegExp = re.compile('.*'+artistExp+'.*', re.IGNORECASE)
        self.albumRegExp = re.compile('.*'+albumExp+'.*', re.IGNORECASE)
        self.genreRegExp = re.compile('.*'+genreExp+'.*', re.IGNORECASE)
        self.allRegExp = re.compile('.*'+linefilter+'.*', re.IGNORECASE)
        self.linefilter = linefilter

        #print ("filter is : "+str(linefilter))

        self.setFilterKeyColumn(0)  

        #print(self.artistRegExp)
        #self.setFilterRegExp()
    def sort(self, col, order):
        self.sourceModel().sort(col, order)
        #print ("sorting")
        """sort table by given column number col"""
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        print (Qt.InitialSortOrderRole)
        print(Qt.AscendingOrder)
        print (order)
        
        self.mylist = sorted(self.mylist, key=operator.itemgetter(col))
        #self.
        if not order == Qt.AscendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))
        #pass
        """
        