#Square of a number & Cube of a number
def square(num):
    return num*num

def cube(num):
    res1=square(num)
    res2=res1*num
    print(res2)

cube(5)