# we are also use else with for loop and we are also use with while loop

for i in range(5):
    print(i)
else:
    print("for loop is end")

# else condition is executed by if for loop condition is wrong.

for i in range(5):
    print(i)
    if i==3:
        break

else:
    print("loop is complited executed")

# else condition not executed becuse loop is break not wrong contitio