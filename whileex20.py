#odd digit count
num=8417
oddcount=0
while num>0:
    r=num%10
    if r%2==1:
        oddcount+=1
        print(r)
    num==num//10

if oddcount==0:
    print('No Odd Digit Found')