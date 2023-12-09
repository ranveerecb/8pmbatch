#Class Preparation
class SimpleCalculator:
    def __init__(self,p1,p2):
        self.n1=p1
        self.n2=p2
    def add(self):
        res=self.n1+self.n2
        print('Sum is:',res)
    def sub(self):
        res=self.n1-self.n2
        print('Sub is:',res)
#object preparation
object1=SimpleCalculator(50,30)
object1.add() 
object1.sub()