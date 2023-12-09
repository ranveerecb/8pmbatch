class SimpleCalculator:
    def __int__(self,p1,p2):
        self.n1=p1
        self.n2=p2
    #Instance Method1
    def add(self):
        res=self.n1+self.n2
        print('Sum is:',res)
    #Instance Method2
    def sub(self):
        res=self.n1-self.n2
        print('Sub is:',res)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#Object1 Preparation
object1=SimpleCalculator(100,30)
object1.add()
object1.sub()