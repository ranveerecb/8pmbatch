def divide():
    a,b,c,name,index,x=100,2,None,'Ranveer',0,0
    try:
        x = int('9.8')
        c=a/b
        index=name[30]
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except IndexError:
        print('Given char index is not found')
    except Exception as e:
        print('You got ',e,' exception in try block')
    else:
        print(c)
        print(index)
    finally:
        del a,b,c,index,name

divide()