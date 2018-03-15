#!/usr/bin/python

import os

class CreateCTLFile():
        def __init__(self,fileName,delimeter):
                self.fileName=fileName
                self.delimeter=delimeter
                self.tableName=self.fileName.strip().split(".")[0]
                self.createTableStaement="CREATE TABLE TMP_" + self.tableName + " ( "
                self.ctlStatement="load data \nappend \ninto table " + self.tableName + " \nfields terminated by " + "\",\" \nTRAILING NULLCOLS("
                self.__createCTLStatement()

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
                self.__createCtlAndCreateFile()

        def __createCtlAndCreateFile(self):
                fp = open(self.tableName+".ctl",'w')
                fp.write(self.ctlStatement)
                fp.close()

                fp = open(self.tableName+"_create.sql",'w')
                fp.write(self.createTableStaement)
                fp.close()

                command1="sed -i '1d' " + self.fileName +  "_FINAL"
                command2="cp " + self.fileName +  " " + self.fileName + "_FINAL"

                os.system(command1)
				os.system(command2)
                

