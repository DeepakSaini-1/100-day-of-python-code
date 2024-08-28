def my_generator():
    for i in range(5):
        yield i


gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)



gen2=my_generator()
print(next(gen2))