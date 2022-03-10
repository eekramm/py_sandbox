# class method start with the decorator @classmethod (syntax suger)
# class Person:
#     # ... 

#     @classmethod
#     def from_csv(cls, filename):
#         return cls(*params)

# Person.from_csv(my_csv)

# class method have no conventional method of where in the class they should go it's up to the dev - be consistent 

class User:
    active_users = 0

    # standard is to pass in cls 
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users!"

    @classmethod
    def from_string(cls, data_string):
        first,last,age = data_string.split(",")
        return cls(first, last, int(age))



    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out!"
    
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, Birthday {self.first}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

# user1 = User("Joe", "Smith", 21)
# user2 = User("Sam", "Tucker", 22)
# print(User.display_active_users())
# user3 = User("Joe", "Smith", 21)
# user4 = User("Sam", "Tucker", 22)
# print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())