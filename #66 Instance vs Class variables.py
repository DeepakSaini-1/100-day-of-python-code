class Employee:
    companyname="apple"
    no_of_employee=0
    def __init__(self, name):
        self.name=name
        self.raise_amount = 0.02
        Employee.no_of_employee+=1

    def wel():
        print("Welcome to Employee showDetails function")

    def showDetails(self):
        Employee.wel()
        print(f"The name of the Employee is {self.name} and the rasise amount in {self.companyname} is {self.raise_amount} and employye number {self.no_of_employee}")

emp1=Employee("Deepak saini")
print(emp1.raise_amount, emp1.companyname)
emp1.showDetails()
emp1.raise_amount=0.03
emp1.companyname="apple india"
emp1.showDetails()

print(emp1.raise_amount, emp1.companyname)
# Employee.showDetails(emp1)

emp2=Employee("Rohan")
emp2.showDetails()

Employee.companyname="oppo"
Employee.raise_amount=0.04
Employee.name="not"

emp3=Employee("new user")
emp3.showDetails()
print(emp1.raise_amount, emp1.companyname)