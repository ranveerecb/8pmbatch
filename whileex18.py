#check number is palindrome or not
num=temp=787
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
print(rev)
print(temp)
if rev==temp:
    print('Palindrome')
else:
    print('Not Palindrome')