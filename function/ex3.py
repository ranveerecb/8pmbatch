#reverse,of a number
num=523
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)