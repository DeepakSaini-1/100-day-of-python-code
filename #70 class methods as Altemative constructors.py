# How to use class methods as altemative constructors

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod        # it is also called Alternative constructors
    def fromsr(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))


e= Employee("Harry", 12000)
print(e.name)
print(e.salary)

string="deepak saini-50,000"

e2=Employee.fromsr(string)
print(e2.name)
print(e2.salary)

"""        # split
# This function divided the string into list and it is geven one argunment and you are geven this argunments it is deveded the srting wased on geven argunments. it is case sensitive
str="Deepak saini-18 -BCA- CTIS"
l=str.split("a")
print(str.split("-"))
print(l)"""