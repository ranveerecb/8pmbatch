def addition(n1,n2):
    return n1+n2
def cube(num):
    return num**3
def power(a,b):
    return a**b
def average(n1,n2,n3):
    return (n1+n2+n3)/3
def biggest(a,b):
    if a>b:
        return a
    else:
        return b
#1. Can we prepare a function with out def keywords ?
#2. Can we prepare a function with out name ?
#3. What is ananymous function ?
#4. What is use of lambda keywords ?
t1=lambda a,b:a+b
t2=lambda a:a**3
t3=lambda a,b:a**b
t4=lambda a,b,c:(a+b+c)/3
print(t1(1,2))
print(t2(5))
print(t3(10,2))
print(t4(4,5,9))