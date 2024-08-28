import time

"""def usingwhile():
    i=0
    while i<500:
        i+=1
        print(i)

def usingfor():
    for i in range(500):
        print(i)

init=time.time()
usingwhile()
t=time.time() - init
init=time.time()
usingfor()
print(time.time() - init, t)"""

# print(4)
# time.sleep(2)
# print(4)


t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)

print(formatted_time)