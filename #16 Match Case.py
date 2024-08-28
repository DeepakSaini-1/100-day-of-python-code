num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
ch=input("Enter the your choice +,-,*./: ")
match ch:
    case "+":
        print("sum of two numbers is: ",num1+num2)
    case "-":
        print("sud of two numbers is: ",num1-num2)
    case "*":
        print("mul of two numbers is: ",num1*num2)
    case "/":
        print("div of two numbers is: ",num1/num2)
    # it is defult case
    # and you are write the many defult case using the if statement
    case _ if ch=='1': 
        print("sum of two numbers is: ",num1+num2)
    case _ if ch=='2': 
        print("sub of two numbers is: ",num1-num2)
    case _ if ch=='3': 
        print("mul of two numbers is: ",num1*num2)
    case _ if ch=='4': 
        print("div of two numbers is: ",num1/num2)
    case _:
        print("enter the valide choice")
