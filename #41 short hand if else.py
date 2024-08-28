a=330
b=33
print("A") if a>b else print("=") if a==b else print("B")

print(a) if a<b else "" # you are use this syntext

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

print(a) if a>b and a>c else print(b) if b>a and a>c else print(c) if c>a and c>b else print("==")