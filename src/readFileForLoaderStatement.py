#!/usr/bin/python

from createAndCtlStatementForLoader import *

if __name__ == '__main__':
        with open("file","r") as fp:
                fileLists=fp.readlines()

        for items in fileLists:
                fileName=items.strip().split("|")[0]
                delimeter=items.strip().split("|")[1]
                createCTLFile = CreateCTLFile(fileName,delimeter)
