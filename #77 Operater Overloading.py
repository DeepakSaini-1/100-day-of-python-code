class verctor:
    def __init__(self, i, j, k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    # it return string but our verctor is not a string use other method
    # def __add__(self, x):
    #     return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k"
    
    def __add__(self, x):
        return verctor(self.i+x.i, self.j+x.j, self.k+x.k)
    
v1=verctor(3, 5, 6)
print(v1)

v2=verctor(1, 2, 3)
print(v2)

print(v1+v2)
print(type(v1+v2))

# see the python doce for operator overloding