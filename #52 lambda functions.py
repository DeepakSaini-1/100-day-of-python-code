
'''def double(x):
    return x*2'''

# you should use this method noly if your logic is completed by one line
doub = lambda x: x*3
cube = lambda x: x*x*x
avr = lambda a,b,c: a+b/c
sum = lambda a,b: a+b

def appl(fx, value):    # function given to a function
    return 6 + fx(value)

# you are also use multiple line but you are use this method so you logic is complex

print(doub(5))
print(cube(5))
print(sum(5,6))
print(avr(1,2,3))
print(appl(cube,2))
print(appl(lambda x: x*x*x,2))
