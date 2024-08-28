# constructor :- If you are use the constructor in python use the __init__ method it is in python a constructor and it is also called dunder method.
# __init__ :- this method call automaticly if you create object of the class


"""class Person:
    name = "Deepak saini"
    age = 19
    def info(self):
        print(f"Age of {self.name} is {self.age}")

obj = Person()
obj.info()
other=Person()
other.name="rohan"
other.age=20
other.info()"""


"""class Person:
    def __init__(self): # in this method requared to geven ' self ' argument, it is not a argument it is a reference of class use this reference we are use the class methodes and variables
        self.wel()  # but in this method mostly requared geven the self argument

     # using this method we set the variable values and i thing python not support multi constructors aproch

    def wel(self):
        print("Welcome to python programming and it is also 100% OOPs based programming")

    def info(self):
        print(f"Age of {self.name} is {self.age}")

# obj = Person()
# obj.info()
other=Person()
other=Person()
other.name="rohan"
other.age=20
other.info()"""

class Person:
    def __init__(self,name,age) -> None:    #   this method automaticly get the reference of you create object in thic this case self get the a reference.
        self.name=name
        self.age=age

    def check(self):
        print(type(self.name))
        print(type(self.age))
        print(self.name)

    def info(self):
        print(f"Age is {self.age}")
        print(f"Name is {self.name}")

a=Person(18,"deepak saini")
a.check()
a.info()
