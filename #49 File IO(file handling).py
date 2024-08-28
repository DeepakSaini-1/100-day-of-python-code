# w for write
# r for read and it is default

# if you make file useing also w keybord use this syntext
# create=open("file-name.Extension","w")
# if you open file on write mode. but file not exist so it's create the file

"""
#     read
f=open("PyWhatKit_DB.txt",'rb')
# print(f) // Print detail of the file
text=f.read()
print(text)
f.close()
"""

# you open file in w mode so clear all writen text and after then write, but you are write the text end of the file and all text are writen so you use the append (a) mode

# x :- this mode creates a file and given an error if the file already exists.

# rt :- open file in text mode but it is default add t 

# rb :- opne file as a binary digites. if you open the jpg, pdf, image file use the rb.


# *** Write to a file***

"""f= open("MyFile.txt","a")
f.write("Hello, How are you ")
# f.close()

# use it is in short
# in this use need to f
with open("MyFile.txt","w"):
    f.write("\nuseing the short mehtoud of write txt in our file and not need to add closed")"""

# not nedd any thinf
# with open("MyFile.txt","a") as g:
#     g.write("\nuseing the short mehtoud of write txt in our file and not need to add closed")