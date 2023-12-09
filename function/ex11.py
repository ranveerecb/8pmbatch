#PS1: total and average and grade of 6 subject marks
def totalmarks(s1,s2,s3,s4,s5,s6):
    total=s1+s2+s3+s4+s5+s6
    return total
def averagemarks(s1,s2,s3,s4,s5,s6):
    avg=totalmarks(s1,s2,s3,s4,s5,s6)/6
    return avg
def grademarks(s1,s2,s3,s4,s5,s6):
    result=averagemarks(s1,s2,s3,s4,s5,s6)
    if result>70:
        print('A grade')
    elif result<70 and result>60:
        print('B grade')
    elif result<60 and result>50:
        print('C grade')
    else:
        print('D grade')

grademarks(44,55,66,77,33,55)