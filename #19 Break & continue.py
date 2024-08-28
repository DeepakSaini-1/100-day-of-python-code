sum=0
for i in range(100):
    if(i%2!=0):
        continue # It is use to skip the any statement
    sum+=i
    if(i==50):
        break   # It is use to exit the loop for any statement
print("sum of even number at the 50: ",sum)

# while loop use as a do-while loop useing the break

while(True):
    print("Helllo world")
    i+=1
    if(i==55):
        break