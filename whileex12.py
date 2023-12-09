#count odd digits in a number
num=235976845795
while num>0:
    r=num%10
    if r%2==1:
        print(r)
    num=num//10

