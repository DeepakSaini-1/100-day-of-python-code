# Method Overriding is a most importent fectuer of OOPs. In this case we are change the methods impletation, variables and processing ect comes to super class to sub class.

class Shape:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()

    
rec = Shape(3, 5)
print(rec.area())

c = Circle(5)
print(c.area())