#!/usr/bin/python

import os

class CreateCTLFile():
	def __init__(self,fileName, threadName, delimeter):
		self.fileName=fileName
		self.delimeter=delimeter
		self.tableName=self.fileName.strip().split(".")[0]
	    extension = self.fileName.strip().split(".")[1]
       self.ctlFileName = self.tableName + "_" + threadName + ".ctl"
	    self.createFileName = self.tableName + "_" + threadName + "_create.sql"
	    self.finalFileName = self.tableName + "_" + threadName + "." + extension
		self.createTableStaement="CREATE TABLE TMP_" + self.tableName + " ( "
		self.ctlStatement="load data \nappend \ninto table " + self.tableName + " \nfields terminated by " + "\",\" \nTRAILING NULLCOLS(" 
		self.__createCTLStatement()
		self.__createCtlAndCreateFile()

	def __createCTLStatement(self):
		with open(self.fileName) as fp:
			header = fp.readline().strip().split(self.delimeter)

		for columns in header:
			self.createTableStaement += "\n"
			self.ctlStatement += "\n"
			self.createTableStaement += columns + " VARCHAR(50)"
			self.ctlStatement += columns + " VARCHAR(50)"
			if header[-1] == columns:
				break
			self.createTableStaement += ","
			self.ctlStatement += ","
		self.createTableStaement += ");"
		self.ctlStatement += ");"

	def __createCtlAndCreateFile(self):
		fp = open(self.ctlFileName, 'w')
		fp.write(self.ctlStatement)
		fp.close()

		fp = open(self.createFileName, 'w')
		fp.write(self.createTableStaement)
		fp.close()
		
		command = "tail -n +2 " + self.fileName + " > " + self.finalFileName 
		os.system(command)

