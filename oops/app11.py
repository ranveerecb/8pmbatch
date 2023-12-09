class ParentClass:
    def sub(self,a,b):
        print(a-b)

class ChildClass(ParentClass):
    def sub(self,a,b):
        super().sub(a,b)
        if a>b:
            print(a-b)
        else:
            print(b-a)

ob=ChildClass()
ob.sub(100,600)