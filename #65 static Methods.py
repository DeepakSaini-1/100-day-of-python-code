'''# As i already told you, 'Static Methods' are used when We are do not use class instance

class Math:
    def __init__(self, num, num2):
        Math.num=num
        Math.num2=num2

    def addtonum(self,n):
        Math.num = Math.num + n

    @staticmethod
    def add(a, b):
        return a+b
    
# result = Math.add(1,2)
# print(result)

a=Math(5,9)
print(a.num)
print(a.num2)
a.addtonum(6)
print(a.num)

print(a.add(5,5))'''

 
# It self
#  if you call class function using the reference so you need to geven self argument in our method but you are call the method useing class so you not need to geven the self argument.
# It is example

class tem:
    def add(a,b):
        print(f"1. The sum of two number of {a} and {b} is {a+b}")

    def wel():
        print("1. Welcome to python programming and why do you learn the language ????")

    def add2(self,a,b):
        print(f"2. The sum of two number of {a} and {b} is {a+b}")

    def wel2(self):
        print("2. Welcome to python programming and why do you learn the language ????")

    @staticmethod
    def add3(a,b):
        print(f"3. The sum of two number of {a} and {b} is {a+b}")

    @staticmethod
    def wel3():
        print("3. Welcome to python programming and why do you learn the language ????")

    @staticmethod
    def add4(self,a,b):
        print(f"4. The sum of two number of {a} and {b} is {a+b}")

    @staticmethod
    def wel4(self):
        print("4. Welcome to python programming and why do you learn the language ????")

"""
tem.add(5,18)
tem.wel()

obj=tem()
# this line geven the error becuse this lien call the method use the Reference of call so you need do geven the self argument on you mehtod, but you are access the method useing class check the uper lines
# obj.add(13,8)   
# obj.wel()"""

tem.add(5,18)
# tem.add2(5,8) #error
tem.add3(5,1)
# tem.add4(5,1) # error

tem.wel()
# tem.wel2()    # error
tem.wel3()
# tem.wel4()    # error

o=tem()
# o.add(5,2)    # error
o.add2(5,2)
o.add3(5,2)
# o.add4(5,2)   # error

# o.wel()   # error
o.wel2()
o.wel3()
# o.wel4()  # error