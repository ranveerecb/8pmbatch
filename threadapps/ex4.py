from threading import Thread, Lock
from time import sleep
class BookMyShow:
    totaltickets=10
    def getTickets(self,name,reqtkt):
        print(BookMyShow.totaltickets,' tickets are available for ',name)
        if reqtkt>BookMyShow.totaltickets:
            print('SOLD OUT')
        else:
            for i in range(1,reqtkt+1):
                sleep(.5)
                print(i,' ticket is issued to ',name)
                BookMyShow.totaltickets=BookMyShow.totaltickets-1

bms=BookMyShow()
lock=Lock()
class Thread1(Thread):
    def run(self) -> None:
        lock.acquire()
        bms.getTickets('ram',8)
        lock.release()
class Thread2(Thread):
    def run(self) -> None:
        lock.acquire()
        bms.getTickets('shyam',8)
        lock.release()
ob1=Thread1()
ob2=Thread2()
ob1.start()
ob2.start()
