#Aliasing the function
def addition(n1,n2):
    print(n1+n2)

addition(10,20)
print(addition)#Printimg function name = It returns address of addition function
sum=addition
sum(100,200)
print(sum)    #Printimg function name = It returns address of addition function
addition(100,200)