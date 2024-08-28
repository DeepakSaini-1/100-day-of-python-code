set1 = {1, 4, 5, 9}
set2 = {3, 7, 5}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1, set2)

# chenge the set1 values
# set2.intersection_update(set1)
# print(set2)

# set1.update(set2)
# print(set1, set2)

newset=set1.symmetric_difference(set2) # not given the same elements
print(newset) 

print(set1.isdisjoint(set2)) # if any elements are the same on the set it retures false

set1.add(7)
set1.add(3)
print(set2.issubset(set1)) # it is chack the all elements are given the set1

print(set1)
set1.remove(3) # not get the value guven the error
set1.discard(7) # not get error
set1.pop()
print(set1)

del set1 # delete the set
set2.clear() # remove all values
print(set2)
print(set1)