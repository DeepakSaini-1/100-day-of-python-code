list=['Deepak saini','Gulvesh','Aryansh']

# single for loop It is use to print the elements of list, dectionary and tuple
for i in list:
    print(i)

print('*****************')

# nested for loop
for i in list:
    print(i)
    for j in i:
        print(j)

# for loop is excute the by-defult 0 to n-1.
# It is excute the 0 to 4 
for i in range(5):
    print(i,', ',end='')
print('')

# assinge the value of i and given the rang or n
for i in range(1,6):
    print(i,', ',end='')
print('')

# assinge the value of i and given the rang or n and increment or decrement
for i in range(2,21,2):
    print(i,', ',end='')