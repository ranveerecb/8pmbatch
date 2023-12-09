#print reverse of a number
num=7824
rev=0
while num>0:             #T                T            T                T         F
    r=num%10             #r=4              2            8                 7
    rev=rev*10+r         #rev=4            rev=42       rev=428          rev=4287
    num=num//10          #782               78           7                0
print(rev)
