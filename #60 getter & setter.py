class Myclass:
    def __init__(self, value):
        self.val=value

    def show(self):
        print(f"{self.val}")

    # def show():
    #     print(f"{Myclass.value}")

    @property # use the @property this mehtod make a getter
    def value(self):
        return 10*self.val
    
    @value.setter # use this syntext make a seter method
    def value(self, new_value):
        self.val=new_value/10 # this line set or change the value of val on glovaly
        return 10*self.val
    
obj=Myclass(10)
obj.show()
obj.value=67 # it is geven the error without the setter mehtod
print(obj.value)
obj.show()

        