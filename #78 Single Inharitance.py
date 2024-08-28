class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("Sound madev by the animal")

    def animal_name(self):
        print("This animal name is ",self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed=breed
         
    def make_sound(self):
        print("Bark !")




b=Dog("Dog", "Doggerman")
b.make_sound()
b.animal_name()

a=Animal("Dog", "Doggerman")
a.make_sound()
a.animal_name()