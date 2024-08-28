# String create useing single-quotes('') and double-quotes("") both
first_name="Deepak"
last_name='Saini.'
# print(type(first_name),type(last_name))
print(first_name,last_name)

# if you print the double-quotes useint start and ending single-quotes
# if you print the single-quotes useint start and ending double-quotes
a='hello "python" programming.'
b="hello 'python' programming."
print(a)
print(b)

# apple="welcome to python jprogramming 
# Deepak saini" #It is given the error becuse you are not print multipe lines

# If you print the multiple lines useing the Triple single-quotes(''' ''') and Triple double-quotes(""" """)

SMS="""
Hello use!
wellcome to python programming in vs code.
It is esye to you work."""
print(SMS)

# print the character of String useinr []
print(first_name[0],".",last_name[0])

#print the character one by one useing for loop in sort
for character in first_name:
    print(character)
for last in first_name:
    print(last)