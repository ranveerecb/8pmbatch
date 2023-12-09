class A:
    def sum(self,n1,n2):
        print('A:sum=',(n1+n2))

class B(A):
    def sub(self,n1,n2):
        print('A:sub=',(n1-n2))

class C(B):
    def mul(self,n1,n2):
        print('C:mul=' , (n1*n2))

class D:
    def div(self, n1, n2 ):
        print('D:div=' ,(n1 / n2))

class E(D):
    def mod(self, n1, n2):
        print('E:mod=', (n1%n2))

class F(D):
    def power(self,n1,n2):
        print('F:power=',(n1 ** n2))

class C1:
    def wishhi(self):
        print(' Hi Ranveer')

class C2:
    def wishbye(self):
        print('Bye Ranveer')
class Child(C1,C2):
    pass
print('--------------------------Ob accessing ------------------------')
ob=Child()
ob.wishhi()
ob.wishbye()

print('----------------Ob1 accessing -------------')
ob1=A()  
ob1.sum(10,20)
print('-----------------Ob2 accessing -----------------------')
ob2=B()
ob2.sum(10,200)
ob2.sub(100,20)
print('---------------------------Ob3 accessing ---------------')
ob3=C()
ob3.mul(100,30)
ob3.sub(100,30)
ob3.sum(100,30)
print('---------------------Ob4 accessing ------------------')
ob4=D()
ob4.div(45,9)
print('----------------------Ob5 accessing --------------------------')
ob5=E()
ob5.mod(45,9)
ob5.div(45,9)
print('--------------------Ob6 accessing -------------------')
ob6=F()
ob6.power(5,3)
ob6.div(45,9)