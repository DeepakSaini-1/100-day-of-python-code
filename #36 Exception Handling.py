num=input("Enter the number: ")

try: # you are not use only try. try block use with the finally or excpte block or keyword
    num=int(num)
    for i in range(1,11):
        print(f"{num} X {i} = {i*num}")
except:
    print("Invalid Input!")

# Exception handling also use to handle the run time error then program executed normal without terminet

# use multiple except
num1=input("Enter th number: ")
num2=input("Enter th number: ")
try:
    # ans=num1/num2   #   tyep Error in your proram
    ans=int(num1)/int(num2)
    print("you ans is ",ans)
except ValueError:
    print("Value Error in your proram")
except IndexError:
    print("Index Error in your proram")
except IOError:
    print("IO Error in your proram")
except TypeError:
    print("tyep Error in your proram")

