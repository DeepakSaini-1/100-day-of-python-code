# if edit 6 character of file you use also f.open and f.write but is is not efficent method yuo shulde use tell and seek method

# these functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.

'''
with open("File.txt","r") as f:
    print(type(f))

    # Move to the 10th byte in the file
    f.seek(10)  # this method not count start laters 10 or given number laters

    print(f.tell())     # this methoud tel you know which later to start the reding the contean
    # read the next 5 bytes 
    data=f.read(5)  # this method noly count 5 laters or gevne numbers of laters
    print(data)
'''

with open("sample.txt","w") as f:
    f.write("Hello world")
    f.truncate(5) # truncate method stor only 5 bytes data and other save data are deleted outomaticly so this is store only 'Hello'

with open("sample.txt","r") as f:
    print(f.read())