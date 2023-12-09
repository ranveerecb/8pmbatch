#Called function
def fact(num):
    if num==1:
        return 1
    else:
        return fact(num-1)*num     #Calling Function itself=>Recursion
#Calling Function
print(fact(5))