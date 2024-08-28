# if i have to differentiate between the keyword "is"  and operator "==" in one line.
# So, the "is" keyword compares the exact location of object in memory and the "==" operator compare the values.


a=4
b="4"

print(a is b)   # it is compares the exact location of the object in memory.
print(a == b)   # it is compares the value 

a=[1,5,9]
b=[1,5,9]

print(a is b)   # it is compares the exact location of the object in memory.
print(a == b)   # it is compares the value 

a=9
b=9

print(a is b)   # it is compares the exact location of the object in memory.
print(a == b)   # it is compares the value 

# both are store one location of memory of object, python not waset the memory both are point one memory 

'''a=4
b=4
c="4"
d="4"
print(a is b)
print(a is c)
print(c is d)
print(c is b)
print(a == b)
print(a == c)
print(c == d)
print(c == b)'''

# when any lement are immutable so you are create two variable  but get the same value so it is create one memory and both are point this memory object