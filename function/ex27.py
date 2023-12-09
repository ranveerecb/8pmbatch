def mygen1():
    '''yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    '''
    for i in range(1,6):
        yield str('955')+''+str(i)

x=mygen1()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
#print(x.__next__())   #StopIteration