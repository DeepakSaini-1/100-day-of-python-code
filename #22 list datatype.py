name=['Deepak saini','Gulvesh','Aryanesh','Asheesh','Gaurve','Hitesh','Shoeb',1,5,9]
# It is list. list is a data type in python it is use to store the data. In the list store multie same and diferent type of data in one variable. access the data using indexing.

# print(type(name))
# print(name)
# print(name[0:5]) # It is print the value of index 0-4
# print(name[:5]) # It is print the value of index 0-4
# print(name[0:]) # It is print the value of index 0-end
# print(name[0:-5]) # It is print the value of index 0-4. Explian name[0:LenghtOfList-5]
print(name[0:9:2]) # It is print the 0 to 9 but 0 after then skip 1 element and print 2 element after then print 2 skip 3 element print 4 element. becuse you given the 2

# print the value of list one-dby-one
# for i in name:
#     print(i)

# If you check the value in list
if 'Deepak saini' in name:
    print("TCA2256018")
elif 9 in name:
    print("TCA2256029")
else:
    print("not mach the value")