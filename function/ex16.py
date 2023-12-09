#Aim: Orbitary parameters or Variable length arguments
def totalItems(*items):
    total_bill=0
    for i in items:
        total_bill=total_bill+i
    print(total_bill)

totalItems(100,250)
totalItems(100,200,300)
totalItems(100,200,500,300,600,700,800)