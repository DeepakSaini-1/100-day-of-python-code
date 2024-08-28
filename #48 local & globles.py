# globle variable :- if any variable make the out of functions and blocks it called globle variable. it is access all program.
# local variable :- if any variable maki in any block is called local variable. it is access only in this block.

b=1    # globle variable
print(b)

def fun1():
    a=2    # local variable
    print(a)
    print(b)  # b is global variable it is accesss in this functio. 
    # b=4 # Error, b is global variable so not change value of v.

def fun2():
    a=3   # local variable
    print(a)
    global b # it get the global variable and you are change this variable value change globaly.
    b=4
    print(b)


fun1()    
fun2()    
print(b)
# print(a) # error