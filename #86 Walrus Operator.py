a=True
# print(a=False) error

"""print(a)
print(a:=False)
print(a)"""

# := it allows you to assin a value to avariavle within an expression

numbers=[1,2,3,4,5]

while (n := len(numbers)) > 0:
    print(numbers.pop())


# foods=list()
# while True:
#     food=input("Enter the food do you like?: ")
#     if food == e:
#         break
#     foods.append(food)

# In short, using the walrus operator
foods=list()
while (food := input("What food do you like?: ")) != "e":
    foods.append(food)