class SimpleCalculator:
    def __init__(self,p1,p2):
        print('------INIT------')
        self.n1=p1
        self.n2=p2
    def __str__(self):
        print('------STR------')
        return str(self.n1)+','+str(self.n2)
    def __del__(self):
        print('------DEL------')
        del self.n1,self.n2
    def add(self):
        res=self.n1+self.n2
        print('Sum is:',res)
    def sub(self):
        res=self.n1-self.n2
        print('Sub is:',res)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#Object1 preparation
object1=SimpleCalculator(100,30)
print(object1)
object1.add()
object1.sub()
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#Object2 preparation
object2=SimpleCalculator(450,36)
print(object2)
object2.add()
object2.sub()
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
