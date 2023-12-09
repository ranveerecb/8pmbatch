def divide():
    a,b = 100,0
    c = None
    name='Ranveer'
    index = None
    try:
        c=a/b
        index=name[30]
    except ZeroDivisionError:
        print('Cannot devide by zero')
    except IndexError:
        print('Given char index is not found')
    else:
        print(c)
        print(index)
    finally:
        del a,b,c,index,name

divide()