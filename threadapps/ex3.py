from threading import Thread
from time import sleep
class Job1(Thread):
    def task1(self):
        for i in range(1,6):
            print('Job1:task1() print i=' ,i)
            sleep(1)
    def run(self) -> None:
        self.task1()
class Job2(Thread):
    def task2(self):
        for i in range(6,11):
            print('Job2:task2() print i=' ,i)
            sleep(1)
    def run(self) -> None:
        self.task2()
ob1=Job1()
ob1.start()
ob2=Job2()
ob2.start()