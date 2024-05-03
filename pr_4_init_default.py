# Write a python program to init default values for user object using __init__ method.

class user:
    def __init__(self,name=None,age=None,email=None):
        self.name = name
        self.age = age
        self.email = email
        

u = user()
print(u.__dict__)
    