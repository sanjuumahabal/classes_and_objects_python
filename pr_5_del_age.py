# Write a python program to delete the age property of the user.

class user:
    def __init__(self,name=None,age=None,email=None):
        self.name = name
        self.age = age
        self.email = email
        
u = user()
print("This is u before deleting age")
print(u.__dict__) 
del u.age
print("u after deleting age")
print(u.__dict__) 

u1 = user()
print(u1.__dict__) 
  