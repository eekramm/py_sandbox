# DEFINING THE SIMPLEST POSSIBLE CLASS

class User:
    # the init function is the constructor of the class
    def __init__(self,first,last,age):
        # self refers to the current instance of the class (like this in js)
        self.first = first
        self.last = last
        self.age = age

    # write all the instance methods after init (convention)

    # instance method - every instance of the class has it's own method
    # simply defining a method within a class 
    # any time we define an instance method you have to pass self as the first param even if not accessed in the method
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, Birthday {self.first}"

    # when passing in data that is not an instance attribute you do not have to use self to access the data 
    def likes(self, thing):
        return f"{self.first} likes {thing}"



user1 = User("Joe", "Smith", 21)
user2 = User("Sam", "Tucker", 22)
print(user1.full_name())
print(user1.initials())
print(user1.is_senior())
print(user1.birthday())
print(user1.likes("Ice Cream"))