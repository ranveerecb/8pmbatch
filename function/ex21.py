def say_hi():
    return 'Hi Students'

def say_bye():
        return 'Bye Students'

def addition(x,a,b,c,d,y):
        result=a+b+c+d
        print(x())
        print('Sum is:',result)
        print(y())

n1,n2,n3,n4=10,20,30,40
addition(say_hi,n1,n2,n3,n4,say_bye)