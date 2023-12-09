listA=[1,2,3]
setA={1,2,3}
dictA={1:'Apple',2:'Banana',3:'Orange'}
#Normal for loop
for i in range(len(listA)):
    print(listA[i])
#for each loop
for ele in listA:
    print(ele)
for ele in setA:
    print(ele)
for k,v in dictA.items():
    print(k,v)