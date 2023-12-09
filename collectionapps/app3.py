'''
Enter your family size:4
Enter 4 member ages:    21
                        23
                        45
                        50
Your family ages are: 21,23,45,50
'''
size=int(input('Enter your family size:'))
print('Enter',size,'member age:')
ages=list()
for i in range(size):
    ele=int(input())
    ages.append(ele)
print('Your family ages are:',ages)
