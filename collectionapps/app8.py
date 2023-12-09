#Wrong way to create a empty set
#a={}
#print(type(a))   #<class 'dict'>
#Right way to create a empty set
a=set()
print(type(a))   #<class 'set'>
b={1}
print(type(b))   #<class 'set'>
c={1,200,5000,7,1,9,4,6,4,7,8,9}
print(c)