#PS1: total and average of 6 subject marks
def totalmarks(s1,s2,s3,s4,s5,s6):
    total=s1+s2+s3+s4+s5+s6
    return total

def average(s1,s2,s3,s4,s5,s6):
    avg=totalmarks(s1,s2,s3,s4,s5,s6)/6
    print('Average =' ,avg)

average(44,55,66,77,33,55)