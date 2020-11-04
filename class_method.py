# Types of Methods

class Student:

    #Class/Static variable
    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        #Instance variable
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #Instance method
    def avg(self):
        return ((self.m1 + self.m2 + self.m3)/3)

    def get_m1(self):
        return  self.m1

    def set_m1(self,value):
        self.m1 = value

    #Class method
    @classmethod #decorators
    def getSchool(cls):
        return cls.school


    #Static method
    @staticmethod
    def info():
        print("This is Student class.. ")

s1 = Student(34,67,32)
s2 = Student(54,10,29)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
