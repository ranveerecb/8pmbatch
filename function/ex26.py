#req1:prepare a flat50 decorator which sub 50/- from total bill
def flat50(total1):
    def inner(i1,i2,i3,i4):
        res=total1(i1,i2,i3,i4)-50
        return res
    return inner
#req2: prepare a package20 decorator which add 20/- from total bill
def package20(foo):
     def inner(v1,v2,v3,v4):
        res=foo(v1,v2,v3,v4)+20
        return res
     return inner
@package20
@flat50
def total(a,b,c,d):
   result=a+b+c+d
   return result

print(total(100,200,250,450))

#req3:prepare a tip10 decorator which add 10/- to total bill
#req4:prepare a aug15 decorator which gives 15% to total bill
#req5:prepare a gst decorator which add 18%- to total bill