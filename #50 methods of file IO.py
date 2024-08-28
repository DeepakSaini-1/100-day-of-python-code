# redline method make for read any file line by line

"""f=open("MyFile.txt","r")
while True:
    line=f.readline()
    print(line)
    if not line:
        # print(line,type(line))
        break"""

'''f=open("Marks #50.txt","rt")
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    # print(line)
    """m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2] # It is string you need int using type casting"""
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2]) 
    print(f"Marks of student {i} in Maths is: {m1+6}")
    print(f"Marks of student {i} in Maths is: {m2+6}")
    print(f"Marks of student {i} in Maths is: {m3+6}")'''

f=open("Marks #50.txt","a")
list=["line 1\n","line 2\n","line 3"]
f.write(f"{list}")
f.close()