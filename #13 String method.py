# a="dEEpak sAiNi"  #   String are immutabilty
# # print(len(a))

# # This method change the upper lower to upper case
# print(a.upper())    # String are not change( immutabilty ) and it is cerate the copy and change the upper case

# # This method change the upper upper to lower case
# print(a.lower())

# # b="aadeepakaaaaa"
# # print(b.rstrip("a"))    # It is method remove the last same character same the argument

# c="deesaini dee"    # all occurrences change
# print(c.replace("dee","Deepak "))   # change the all plac the given the string to other given string

# print(c.split())    # It is string to change the list. If it is given the space start the new element


# print(a.capitalize())   # It is given change the first later to upper case and othe lowes case

# print(a.capitalize().center(50))     # It is center the String acoding to given lenth EX:- 50-12=38, 18 space starting and 18 space ending

# print(a.endswith("Ni"))     # It is chack the string are end the given argument and return the True or False case sensitiv
# print(a.startswith("dE"))   # It is chack the string are start the given argument and return the True or False case sensitiv
# print(a.endswith("ak",3,6)) # It is chack the index 3 to 6 end the 'ak' return True or False
# print(a.startswith("sA",7))   # It is chack the index 7 to end or number start the 'sA' return True or False

# print(a.find("Ni"))         # It is return the index of first of given arguments if not got the argument return the -1
# print(a.index("Ni"))         # It is return the index of first of given arguments if not got the argument return the error

# This methods are return the bool.
d="DeePak18"
print(d.isalnum()) # your String is aplha numerical or not means your string make the useing A-Z, a-z & 0-9. If has string space return the false.

print(d.isalpha())  # It is chack the string are the make using the A-Z or a-z. 