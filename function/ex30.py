#Call by Value & Call by Reference
def one(a,b):
    print('-------INSIDE ONE FUNCTION-------')
    a=a+1000
    b[0]=400
    b[1]=500
    b[2]=b[2]+594
    print(id(a),' address value is:',a)
    print(id(b), 'address value is:', b)
x=100
y=[4,5,6]
print('-------BEFORE CALLING ONE FUNCTION-------')
print(id(x),' address value is: ',x)
print(id(y),' address value is: ',y)
one(x,y)  # x is a call by value and y is call by reference
print('-------AFTER CALLING ONE FUNCTION-------')
print(id(x),' address value is: ',x)
print(id(y),' address value is: ',y)
print(y)