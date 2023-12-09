tuple1=(1,2,3,4,5,6)
#tuple1[0]=100
'TypeError: tuple object does not support item assignment'
#del tuple[2]
'TypeError: tuple object does not support item deletion'
print(tuple1.index(3))
print(tuple1.count(6))