'''
8.Utility function
  index()
  rindex()
  count()
  split()
  replace()
  join()
  format()
'''
s1='india'
print(s1.index('d'))
print(s1.index('i'))
print(s1.rindex('i'))
print(s1.count('i'))
print(','.join(s1))
print('@'.join(s1))

age=21
height=6.2
name= 'Ajay'
msg='Person details are: Height={1} Name={0} Age={2}'.format(height,name, age)
print(msg)

str1='Python is simple'
str2='Python$is$simple$to$learn'
print(str1.split(' '))
print(str2.split('$'))

print(str1.replace('Python','Java'))
print(str1)