#Avg of digit in a number
num=9876654
sum=0
count=0
while num>0:
    r=num%10
    sum+=r
    count+=1
    num=num//10

print(sum/count)