# one class all method and variable access or extend to othe class it is called inheritance.

class Employee:
    def __init__(self, name , id):
        self.name =name
        self.id=id

    def showDetails(self):
        print(f"The name os Employee : {self.id} is {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default language is Python")

e1 =Employee("Rohan Das", 400)
e1.showDetails()
# e1.showlanguage()  it is geven error becuse employee not have showlanguage mthod but programmer calls hava also
e2 =Programmer("Rahule", 402)
e2.showDetails()
e2.showlanguage()