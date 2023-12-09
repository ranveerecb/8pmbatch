#count even digits in a number
num=235976845795
sum=0
count=0
evencount=0
while num>0:
    r=num%10
    sum+=r
    count+=1
    if r%2==0:
        evencount+=1
print(sum)
print(count)
print(evencount)

