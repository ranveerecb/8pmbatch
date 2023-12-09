#Write a python app to create a file & write some data into the file
def writeDataIntoFile():
    f1 = open('data1.txt','w')
    data='ranveer'
    f1.write(data)
    f1.close()


writeDataIntoFile()