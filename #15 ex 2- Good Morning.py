import time as t
print(t.strftime('%H:%M:%S'))
time=t.strftime('%H:%M:%S')
if(t.strftime('%H:%M:%S')>"18:00:00"):
    print("Good evening")
elif(t.strftime('%H:%M:%S')>"12:00:00"):
    print("Good afternoun")
else:
    print("Good morning")