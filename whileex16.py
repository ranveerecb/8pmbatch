#print large digit in a number
num=7824
smallDigit=9
while num>0:
    r=num%10
    if r<smallDigit:
        smallDigit=r
    num=num//10

print(smallDigit)
