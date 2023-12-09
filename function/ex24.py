#Called function
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i           #f=1*1    #f=1*2   #f=2*3   #f=6*4   #f=24*5
    return f
#Calling Function
print(fact(5))