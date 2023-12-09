#Write a python app to append data into the file
def appendDataIntoFile():
    f1 = open('data2.txt','a')
    data='How are you ?'
    f1.write(data)
    f1.close()


appendDataIntoFile()