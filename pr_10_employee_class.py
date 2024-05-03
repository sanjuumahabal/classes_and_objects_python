# Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values

class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.Empid = empid
        self.Name = name
        self.Salary = salary
        
    def setValues(self):
        print("Enter EmpId, Name and Salary: ")
        self.Empid = int(input())
        self.Name = input()
        self.Salary = float(input())
    def getValues(self):
        print(f"EmpId: {self.Empid}, Name: {self.Name}, Salary: {self.Salary}")
        
e = Employee()
e.setValues()
e.getValues()
