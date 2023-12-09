a=[10,2,30]
b=[4,50,6]
#1.Insertion related=> append(ele)   insert(index,ele)   extends(list)
a.append(100)
a.append(200)
a.insert(2,300)
a.extend(b)
print(a)
#2.Removal related=> pop() & remove(ele)
a.pop()
a.pop()
a.remove(30)
print(a) 
#Utility related
listA=[10,6,7,10,9,10,15]
print(listA.count(10))
listA.sort()
print(listA)
listA.reverse()
print(listA)
print(listA.index(9))
listB=listA.copy()
print(listB)