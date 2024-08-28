# Decorators :- Decorators are the function which htlps to change and return other functions. It is a function whic takes another function, updates it and then return it.


def greet(fx):
    def mfx():
     print("Good MOrning")
     fx()
     print("Thanks for using this functons")
    return mfx

def add_deco(fx):
   def mfx(*args , **kwargs):   # one start get all the argument as a tuple and two star get all the argument as a dictionary 
      print("Wlcome to add funtion with decoration funtion")
      fx(*args , **kwargs)
      print("Thanks for usint the add functio")
    # return mfx

@greet
def Hello():
    print("Hello world")

@add_deco
def add(a, b):
    print(a+b)

# greet(Hello)
# Hello()
#  or
Hello()

add(9,9)