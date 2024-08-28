# magic mehtods are def on your class it is for performe task as magicly

class Emmployee:
    def __init__(self, name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+i
        return i
    
    def __str__(self):
        return (f"the name of the employe is {self.name} str")
    
    #if any condition not given str method so it is run or rwturn repr method also 

    def __repr__(self):
        return (f"the name of the employe is {self.name} repr")
    
    def __call__(self):
        print("Hey i am good")

e=Emmployee("harry")
print(e.name)
print(e)
print(repr(e))
print(str(e))
# print(len(e))

# If e call object like this for eg. By writing "e()"
e()

# reviwe this video 