class Student:
    #Class Variables
    institute_name='Ashok-It'
    fee=6000
    trainer_name='Ranveer'
    def __init__(self,rlno,name,age):
        #Object Variables
        self.roll_number=rlno
        self.name=name
        self.age=age
    def show_student_info(self):
        print('Name={},Age={},SNO={},Institute={},Fee={},Trainer={}'.format(self.name,self.age,self.roll_number,Student.institute_name,Student.fee,Student.trainer_name))

student1=Student(1,'Ajay',23)
student2=Student(2,'Deepak',26)


student1.show_student_info()
student2.show_student_info()