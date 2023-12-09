from time import sleep
class Job1:
    def task1(self):
        for i in range(1,6):
            print('Job1:task1() prints i=',i)
            sleep(1)
class Job2:
    def task2(self):
        for i in range(6,11):
            print('Job2:task2() print i=',i)
            sleep(1)
ob1=Job1()
ob1.task1()
ob2=Job2()
ob2.task2()