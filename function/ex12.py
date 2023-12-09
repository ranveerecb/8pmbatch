a=100
def onefunction(b):
    c=10
    global a
    a=a+c
    print(a,b,c)

def twofunction(d):
    e=5
    global a
    a=a+e
    print(a,d,e)

onefunction(7)  #110,7,10
twofunction(8)  #115,8,5