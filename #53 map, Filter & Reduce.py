# This function get the sequence of elements and return the sequence of elements
# if any function get the function as a argument is called higher order function

"""        Map
def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,3,4,5,6,7]
# newl=[]
# for i in l:
#     newl.append(cube(i))

# It is long term

# newl=list(map(lambda X: x*x*x,l))  
newl=list(map(cube,l))  #   using mpa function, Then give the name of the list on which you want to apply that functio. it is also lambdafuction.
# It is short term

print(l,"\n",newl)"""

'''
        # FILTER
def filter_function(a):
    return a>5

l=[1,2,5,4,8,7,9,6,3]

# newl=list(map(filter_function,l))   False
# newl=list(filter(lambda x: x>3, l)) 
newl=list(filter(filter_function, l)) #   filter function filer you list, dictionay and other or types accoding you requardmain. you gentar your method
print(newl)'''

'''from functools import reduce

number = [1,2,5,4,9,6,8,7,3]

mul = reduce(lambda x,y: x*y, number)
sum = reduce(lambda x,y: x+y, number)

print(sum)
print(mul)'''


m=1
for i in range(30):
    m*=2

print(m)