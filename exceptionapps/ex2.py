def divide():
    a,b = 100 , 30
    c = None
    try:
        print('############TRY#############')
        c=a/b
    except ZeroDivisionError:
        print('###########EXCEPT##########')
        print('Cannot divide by zero')
    else:
        print('############ELSE############')
        print(c)
    finally:
        print('##########FINALLY##########')
        del a,b,c

divide()