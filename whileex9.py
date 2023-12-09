#Count of digit in a number
num=6548
sum=0
count=0
while num>0:
    r=num%10
    sum+=r
    count+=r
    num=num//10
print(sum)
print(count)

