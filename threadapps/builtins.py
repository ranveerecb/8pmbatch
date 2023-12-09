from threading import Thread
from time import sleep
class Job1(Thread):
    def task1(self):
        for i in range(1,6):
            print(self.getName(),' :task1() prints i=' ,i)
            sleep(1)
    def run(self) -> None:
        self.task1()
class Job2(Thread):
    def task2(self):
        for i in range(6,11):
            print(self.getName(),' :task2() prints i=' ,i)
            sleep(1)
    def run(self) -> None:
        self.task2()
ob1=Job1()
ob1.setName('ram')
ob1.start()
ob1.join()
ob2=Job2()
ob2.setName('ajay')
ob2.start()
ob2.join()
