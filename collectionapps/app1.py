a=[10,10,10,10,2,30,4,15]
b=list()
b=b+[1,2.2,'Apple',True,3+4j]
print(type(a),type(b))
a[0]=1000
del a[6]
print(a)
print(b)
print(b[0])
print(b[-1])