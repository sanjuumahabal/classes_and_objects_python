# Write a python program to create 3 user objects and find the youngest of all.
from user import user

def youngest(u1, u2, u3):
    if u1.age < u2.age:
        if u1.age < u3.age:
            return u1
        else:
            return u3
    else:
        if u2.age < u3.age:
            return u2
        else:
            return u3   
    
user1 = user("ajay",21,"ajay@gmail.com")
user2 = user("vijay",18,"vijay@gmail.com")
user3 = user("sanjay",19,"sanjay@gmail.com")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(youngest(user1, user2, user3).name," is Youngest amongst all!!")

