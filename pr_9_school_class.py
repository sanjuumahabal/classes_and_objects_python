# Write a python program to create a School class and 3 instance variables and 1 class variable.

class School:
    school_name = "I.E.S. Katrap"
    def __init__(self,sname=None,tname=None,hname=None):
        self.stud_name = sname
        self.teacher_name = tname
        self.hod_name = hname

    def show(self):
        print(f"Student Name: {self.stud_name}, Teacher Name: {self.teacher_name}, HOD Name: {self.hod_name}, School Name: {self.school_name}")
        

s1 = School("Kunal","RK Sir","Prof. Vipul Dalal")
s1.show()