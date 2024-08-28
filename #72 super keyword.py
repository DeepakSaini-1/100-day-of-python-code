"""# we are using super keyword access super class method and variables

class parentClass:
    def parent_method(self):
        print("This is the parent method.")

class Childclass(parentClass):
    def parent_method(self):
        print("i am a child class but my name is parent_method also.")
        super().parent_method()

    def chuild_method(self):
        print("This is the cild mehtod.")

        super().parent_method()

child_object= Childclass()
child_object.chuild_method()
# child_object.parent_method()"""


class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

class programmer(Employee):
    def __init__(self, name, id, lang):
        self.lang=lang
        super().__init__(name, id)

deepak=Employee("Rohan Das", "420")
harry=programmer("harry", "2345",  "python")

print(deepak.id)
print(harry.id)
print(harry.name)
print(harry.lang)