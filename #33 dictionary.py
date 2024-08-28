dic={
    "name":"deepak saini",
    4: 45,
    45: "TCA2256018"
}
# print(dic["name"],dic[4],dic[45])

# it is geven the value of get key
print(dic[4]) # key is not found geven the error
print(dic.get(5)) # if key is not get return the none

print(dic.keys()) # it is given the all key of dictionary
print(dic.values()) # it is given the all values of dictionary

for key in dic:
    print(key,end=" ") # it is given the key
    print(":",dic[key]) # it is given the valu

for key in dic.values():
    print(key,end=" ") # it is given the value
    # print(":",dic[key]) # it is given the valu

print("\n",dic.items())

for key,value in dic.items():
    print("This is ",key," and it is ",value)