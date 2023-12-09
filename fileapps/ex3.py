#Write a python app to read data from the file
def readDataIntoFile():
    f1=None
    try:
        f1 = open('data3.txt','r')
    except FileNotFoundError:
        print('Given file is not available in HDD')
    else:
        data=f1.read()
        print(data)
    finally:
        if f1 is not None:
            f1.close()

readDataIntoFile()