"""
in python not any public, provate and protected keyword but we are also use public, private and protected mehtod use the some symbles.

In python, every variable is public.

python are geven three type of Access Specifier
1. public :- access any location, By default, if you make any variable in python it is accessible from outside. All the variables methods in python are by default public.
2. private :- access only class, 
    private variable means that it cannot be accessed outside of class, declaer the private use the duble'_', use this __
3. protected :- access only class and subclass of this class, In python the convertion for indicating that is a single underscore ( _ ) use the set protected.
"""


class Employee:
    def __init__(self):
        self.__name = "Deepak saini"

a = Employee()
# print(a.__name) Cannot be accessed directly 
print(a._Employee__name)    # but accessed indirectly, using this syntext. It is calling 'name mangling'
# name mangling in python is a technique used to protect class-private and super class-private attributes from being accidentally overwritten

print(a.__dir__())  # it is geven all of the method and variable we are access 

# Python not support the access modifiers but we are our tasli use the single and duble underscore, so python is not support privace so java is best for privace