
'''
class Person:
    name = "Harry"
    occupation = "cloud engineer"
    networth = 10
a=Person()
    
print(a.name)
print(a.occupation)
print(a.networth)
print("************************************************************")

# I am chenge data also

# This statement delete the old data and store new of this data 
a.name="rohan"
a.occupation="hacker"
a.networth="50"
print(a.name)
print(a.occupation)
print(a.networth)
print("************************************************************")

# but we are create new object access the old data esly
n=Person()
print(n.name)
print(n.occupation)
print(n.networth)
print("************************************************************")

# In this aproch we are create object and fell the data and not delet the old data
my=Person()
my.name="Deepak siani"
my.networth=30
my.occupation="software developer"

print(my.name)
print(my.occupation)
print(my.networth)
print("************************************************************")'''

class Details:
    name = "Rohan"
    age = 20
    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")
obj1 = Details()
obj1.desc()

class Deepak:
    name = "Deepak saini"
    age = 19
    college="TMU"
    occupesion="cloud developer"
    def desc(self):
        self.occupesion="student"
        print("my name is ",self.name,"and my age is ",self.age,"\nor i am a ",self.occupesion)
        print("My college name is ",Deepak.college)

saini=Deepak()
saini.desc()

n=Deepak()
n.name="Rohane saini"
n.age=25
n.occupesion="software engineer"
n.desc()


# self parameter :-
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

                # or

# self means that objects for which this method is called