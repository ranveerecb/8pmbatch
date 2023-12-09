#check number is armstrong or not
num=temp=153
arm=0
while num>0:
    r=num%10
    arm=arm+r**3
    num=num//10

if arm==temp:
    print('Armstrong')
else:
    print('Not Armstrong')