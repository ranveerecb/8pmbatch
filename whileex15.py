#print large digit in a number
num=7824
largeDigit=0
while num>0:             #T                T            T                T         F
    r=num%10             #r=4              2            8                 7
    if r>largeDigit:     #4>0              2>4          8>4               7>8
        largeDigit=r     #largedigit=4     NC           largedigit=8      NC
    num=num//10          #782               78           7                0

print(largeDigit)
