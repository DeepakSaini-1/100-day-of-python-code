# if you use any class and you are not know to this class. you are using this methods find out more avout the class
# you are using this three methods 'dir()', '_dict_' & help()

"""# ** dir() **
# Using this method we are find the all of the function of class and any datatype function
x=[1,2,3]
print(dir(x))
print(x.__add__)"""

# ** __dict__ **

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.version=1

p = Person("deepak", 18)
print(p.__dict__)
# you are define whatever using the self it is show all of them

# ** help **
print(help(Person))