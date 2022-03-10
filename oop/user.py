# DEFINING THE SIMPLEST POSSIBLE CLASS

class User:
    # the init function is the constructor of the class
    def __init__(self,first,last,age):
        # self refers to the current instance of the class (like this in js)
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe", "Smith", 21)
user2 = User("Sam", "Tucker", 22)
print(user1.first, user1.last, user1.age)
print(user2)