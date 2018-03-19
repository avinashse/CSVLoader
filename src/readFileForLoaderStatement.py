#!/usr/bin/python

from QueueReaderThread import *

THREAD_COUNT = 5

if __name__ == '__main__':
        with open("file", "r") as fp:
                fileLists = fp.readlines()

        THREAD_COUNT = len(fileLists) if len(fileLists) < THREAD_COUNT else THREAD_COUNT

        for threadId in range(THREAD_COUNT):
                ReaderThread(threadId, "Thread_" + str(threadId)).start()

        for files in fileLists:
                fileQueue.put(files)
