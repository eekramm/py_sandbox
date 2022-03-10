# _name - signify that this is supposed to be private pure convention
# __name - not convention this makes python do name mangling where it puts the class name first
# __name__ - used for python spicific methods

class Person:
    # dunder method - used when referencing something or over writing something already used in python
    def __init__(self):
        self.name = "Tony"
        # single underscore is a convention to tell other developers that this is supposed to be a private method
        # python does not have a way of making something private 
        self._secrit = "hi!"
        # double underscores does something called name mangling
        # if you tried to print (in this example) p.__msg you will get an error
        # the way to access this would be p._Person__msg
        # double underscore makes the data specific to this class 
        self.__msg = "I like turtles!"

p = Person()