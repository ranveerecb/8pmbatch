class A:
    def sum(self,n1,n2):
        print('A:sum=',(n1+n2))

class B:
    def sum(self,n1,n2):
        print('B:sum=',(n1+n2))

ob1=A()
ob1.sum(10,20)

ob2=B()
ob2.sum(10,200)