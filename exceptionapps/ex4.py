def divide():
    a,b,c,name,index = 100, 2, None, 'Ranveer', 0
    try:
        try:
            index=name[2]
        except IndexError:
            print('Given char index is not found')
        else:
            print(index)
        finally:
            del index,name
        c=a/b
    except ZeroDivisionError:
        print('Cannot devide by zero')
    else:
        print(c)
    finally:
        del a,b,c

divide()