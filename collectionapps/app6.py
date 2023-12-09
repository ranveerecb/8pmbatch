#Single List
person=[1,'Ajay',6.1]
#Nested List
persons=[
    [1,'Ajay',6.1],
    [2,'Ram',6.2],
    [3,'Venu',6.3]
]
#Accessing Single list elements using for loop
for i in range(len(person)):
    print(person[i])
#Accessing Multi list elements using for loop
for r in range(len(person)):                #r=2
    for c in range(len(persons[r])):        #c=0,1,2
        print(persons[r][c],end=' ')
    print()