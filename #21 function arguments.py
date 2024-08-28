# Type of Arguments
#1. Default Arguments
#2. Keyword Arguments
#3. Variable length Arguments 
#4. Required Arguments


# 1. default arguments

# def average(a=3,b=5):   # if you are not given the arguments it is consider the by-default you are assignment  the value
#     print("The average is ",(a+b)/2)

# average(4,6)
# average() # you are not given the value function by-defould assingent the a=2 & b=9
# average(5) # if you are given the only one value it value assignment  the first variable and second variable use the by-default value
# average(b=4) # but you are given the value second variable use it sentext


# def name (fname, mname='jhon',lname='whatson'):
#     print('Hello,',fname,mname,lname)

# name('Any','Agarwal','jain')
# name('Any','Agarwal')
# name('Agarwal')


# # It is wrong
# def name (fname, mname='jhon',lname):   # if you assignment  the default value so compalsere you assignment  the last ariable value
#     print('Hello,',fname,mname,lname)

# name('Any','Agarwal')


# # 2. Keyword Arguments
# # you are assignment the value useing the keyword
# def sum(a=6,b=9):
#     print("The value of a is: ",a)
#     print("The value of b is: ",b)
#     print("sum of a & b is: ",a+b)

# sum()
# sum(b=3,a=6)

# # 3. Required Arguments
# # in the required arguments you are require the given value Ex:-

# def sum(a,b,c=1):
#     print("sum of three numbers is: ",a+b+c)

# sum(5,3)

# # you are not given the value of a & b so you required to given minimum two arguments and c is optional

# 4. variable lenght arguments

# def average(*number):   # It is get the arguments as a tuple. you are given the 1-99.. arguments
#     print(type(number))
#     sum=0
#     for i in number:
#         sum+=i
#     print("Average is: ",sum/len(number))

# average(5)
# average(5,5)
# average(5,5,5)
# average(5,5,5,5)
# average(5,5,5,5,5)

def average(**name):   # It is get the arguments as a dictionary. you are given the 1-99.. arguments
    print(type(name))
    sum=0
    for i in name:
        print(i," : ",name[i])


average(n1='deepak',n2='gulvesh',n3='Aryanesh')
