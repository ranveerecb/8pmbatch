#print() function
#end & sep keyword as arguments
'''
print(1,end='$')
print(2,end='$')
print()
print(3,end='$')
print(1,2,3,4,5,6,sep=',')
print(1,2,3,4,sep='$',end='&')
print(4,5,6,sep='@')
'''
#Format Specifier => %d %f %s
age=20
height=6.3
name='ranveer'
print('My Name is:%s My age is:%d My Height is:%f'%(name,age,height))
#string format() function
print('My Name is:{} My Age is:{} My Height is:{}'.format(name,age,height))