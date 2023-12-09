class Addition:
    def sum(self,*items):
        s=0
        for item in items:
            s=s+item
            print(s)
ob=Addition()
ob.sum(1,2)
ob.sum(1,2,3)
ob.sum(1,2,3,4)
