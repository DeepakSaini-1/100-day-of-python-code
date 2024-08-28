# you are not change the tupe but is is converd into list and after then change into tuple.
countries=('Spain','italy','india','england','germany')
temp=list(countries)
temp.append('Russia')
temp.pop(3)
temp[2]='finland'
countries=tuple(temp)
print(countries)

countries2=('Spain','italy','india','england','germany')
countries3=countries+countries2
print(countries3)

print(countries3.count('italy'))
print(countries3.index('italy')) # if it is not get the value it return the error.
print(countries3.index('italy',5,9))    # it is chck the value in index 5 to 9 