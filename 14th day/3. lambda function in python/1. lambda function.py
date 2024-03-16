# Lender function, single expression hoyea thakea.

# #normal code:
def double(x):
  return x*2
print(double(3))

# #single line code:
double = lambda x: x*2
square = lambda x: x*x
cube = lambda x: x*x*x
ave = lambda x, y, z: (x+y+z)/3
print(double(7))
print(square(6))
print(cube(5))
print(ave(7, 9, 14))
print('\n\n')



def appl(fx, value):            # function.
  return 6 + fx(value)          # "fx(value)=16" + 6 = "24" ar man return hobea.

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x * x * x, 2))     # x ar man ="2" ,,, 2 X 2 X 2 X 2 = 16 ;   return data print hobea.
