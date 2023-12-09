from threading import Thread

class ClassOne(Thread):
    def run(self) -> None:
        if self.isDaemon():
            print(self.getName(),' is Daemon thread')
        else:
            print(self.getName(),' is User Thread')

t1=ClassOne()
t2=ClassOne()
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()