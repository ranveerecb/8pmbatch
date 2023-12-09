#Aim: Keyword  as argument=Assigning values to arguments directly
def showemployeeinfo(id,name,salary):
    print('Employee ID=' ,id)
    print('Employee Name=' ,name)
    print('Employee Salary=' ,salary)

#Approach1
#showemployeeinfo(1,'ranveer',15000)
#Approach2
#a,b,c=1,'ranveer',15000
#showemployeeinfo(a,b,c)
#Approach3: Keyword as argument
showemployeeinfo(id=1,name='ranveer',salary=15000)

print('Hello' , 'Ranveer' , 'How are you' ,sep=',')