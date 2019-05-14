import threading
import time

class testThread(threading.Thread):

    def __init__(self, threadID, countdown):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.counter = countdown

    def run(self):
        print("Starting Thread " + str(self.threadID))
        self.print_time(self.threadID, self.counter)
        print("Exiting Thread " + str(self.threadID))

    def print_time(self, tid, delay):
        for i in range(5):
            time.sleep(delay)
            print("%s: %s" % ("Thread " + str(tid), time.ctime(time.time())))

thread1 = testThread(1, 1)
thread2 = testThread(2, 2)
thread3 = testThread(3, 3)
thread4 = testThread(4, 4)

thread1.start()
thread2.start()
thread3.start()
thread4.start()