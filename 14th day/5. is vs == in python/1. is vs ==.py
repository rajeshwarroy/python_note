# # "is" compare korea thakea "adject location object" in "memory"
# # and
# # "==" compare korea thakea "value kea", 2 object ar value thik achea ki na.


e = 4
w = "4"

print(e is w)           # exact location of object in memory
print(e == w)           # exact location of object in memory
print('\n')


q = 3
p = 3
print(q is p)
print(q == p)
print('\n')


u = "hello"
v = "hello"
print(u is v)
print(u == v)
print('\n')




a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value
