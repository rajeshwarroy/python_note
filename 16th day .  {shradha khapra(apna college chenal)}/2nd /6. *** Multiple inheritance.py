class A:
    varA ="welcome to a"
class B:
    varB ="welcome to b"
class C(A, B):
    varC = "welcome to c"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
