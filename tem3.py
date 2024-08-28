# class i:
#     def fun(num1, num2):
#         print("hello word")
#         print(f"the sum of {num1} and {num2} is {num1+num2}")
#         print("sum = ",num1+num2)

#     def wel():
#         print("Welcome to python programmming and why do you learn this language")


# # i.fun(5,6)
# obj=i()
# i.wel()
# obj.wel()

# q = '5 + 6 + 7 - 4 + 6 * 2 * 4'
# a = 0
# a = int(q.split(" ")[0])
# for i in range(1, int(len(q)/2), 2):
#     o = q.split(" ")[i]
#     v = int(q.split(" ")[i+1])
#     match o:
#         case "+":
#             a += v
#         case "-":
#             a -= v
#         case "*":
#             a += int(q.split(" ")[i-1])*v-int(q.split(" ")[i-1])
#         case "/":
#             a += int(q.split(" ")[i-1])/v-int(q.split(" ")[i-1])
# print(5 + 6 + 7 - 4 + 6 * 2*4)
# print(a)
import random as r
ip=str(r.randint(000000,1000000))
for i in range(1000000):
    p=str(i)
    if(len(p)<=6):
        for j in range(len(p),6):
            p='0'+p
    if(p==ip):
        print("your password is ",p)
        break

print(ip)