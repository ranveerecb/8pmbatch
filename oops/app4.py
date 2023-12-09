#Class Preparation
class SimpleCalculator:
    #Static Method1
    @staticmethod
    def add(n1,n2):
        res=n1+n2
        print('Sum is:',res)
    #Static Method2
    @staticmethod
    def sub(n1,n2):
        res=n1-n2
        print('Sub is:',res)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
SimpleCalculator.add(10,20)
SimpleCalculator.sub(45,30)