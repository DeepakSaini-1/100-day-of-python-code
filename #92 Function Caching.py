import functools
import time

# @functools.lru_cache(maxsize=None)
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1)+fib(n-2)

# print(fib(20))

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(20))

print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

# In this function your are given the same number it is not reu it return old value so you save you time 