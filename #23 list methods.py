l=[1,7,9,4,5,6]
print(l)

l.append(7) # add the an element in last of list
print(l)
l.insert(0,2) # add the an element in list. (index,value)
print(l)

l.sort() # sort the list
print(l)
l.sort(reverse=True)
print(l)

print(l.index(7)) # it is retun the index of first element match

l.reverse() # it is reverse the liat elements
print(l)
l.reverse()
print(l)

print(l.count(7)) # it is count the 7. hoe many time repet

# if you change m so i will also be changed because you made m a reference for l. so use the copy method
# m=l
# m[0]=8
# print(l)
m=l.copy()
m[0]=8
print(l,"\n",m)

l2=[12,13,4,15,1]
l.extend(l2) # it is add the l2 list in end of l list
print(l)
print(l2)

newl=l+l2   # add the two or more list and create the new list
print(newl)