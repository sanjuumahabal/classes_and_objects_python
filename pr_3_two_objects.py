# Write a python program to create 2 objects of the user class and assign different
# values.

class user:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email


u1 = user("viraj",23,"viraj@email.com")
u2 = user("sam",20,"sam@gmail.com")

print(u1.__dict__)
print(u2.__dict__)