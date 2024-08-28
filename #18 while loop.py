count=1
while(count<=10):
    print("5 X ",count,' = ',count*5)
    count+=1

count=1
str=input("Enter the message: ")
num=int(input("Enter the number of send the message: "))
while(count<=num):
    print(str)
    count+=1
else: # if while condition is fales so excuted the else statement
    print("Task is complited")