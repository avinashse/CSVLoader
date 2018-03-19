import threading
from Queue import *
from createAndCtlStatementForLoader import *
import time

fileQueue = Queue()
sleepTime = 1/1000000000
isComplete = True

class ReaderThread(threading.Thread):
    def __init__(self, threadId, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.threadId = threadId

    def run(self):
        time.sleep(sleepTime)
        while not fileQueue.empty():
            fileParam = fileQueue.get()
            fileName = fileParam.strip().split("|")[0]
            delimeter = fileParam.strip().split("|")[1]
            CreateCTLFile(fileName, self.threadName, delimeter)

