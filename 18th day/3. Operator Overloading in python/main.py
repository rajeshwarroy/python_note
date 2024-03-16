class Vactor:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, other):
        return f"{self.i + other.i}i + {self.j + other.j}j + {self.k + other.k}k"

    def __add__(self, x):           # type dekhar jonno
        return Vactor(self.i + x.i, + self.j + x.j, + self.k + x.k)

v1 = Vactor(4, 7, 9)
print(v1)
v2 = Vactor(2, 6, 9)
print(v2)
v3 = Vactor(1, 4, 7)
print(v3)


print('\n1st and 2nd')
print(v1+v2)

print('\n1st and 3rd')
print(v1+v3)

print(type(v1 + v2))            # type dekhi
