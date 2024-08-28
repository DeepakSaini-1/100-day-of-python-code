# Finally block code always executed
# use finally keyword in function and return the value but finally block code ren always

def function():
    try:
        l=[3,5,7,8,]
        i=int(input("Enter the index number: "))
        print(l[i])
        return i
    except:
        print("some error accurres")
        return -1
    finally:
        # print(10/0) It is given the error
        print("I am always executer")

x=function()
print(x)

try:
    l=[3,5,7,8,]
    i=int(input("Enter the index number: "))
    print(l[i])
    
except:
    print("some error accurres")
    
finally:
    print("I am always executer")