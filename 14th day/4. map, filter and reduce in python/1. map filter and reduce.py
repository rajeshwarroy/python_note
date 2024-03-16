# # MAP
# # here is an example of hew to use the map function:
# #   map(function, iterable)


def cube(x):
  return x * x * x


print(cube(2))

l = [1, 2, 4, 6, 4, 3]              # every item in "l"
newl = []                           # First of all we create a empty list in "newl" name a,
newll = []                          # First of all we create a empty list in "newl" name a,

for item in l:                      # 'for loop' banaichi 'item' name a,
  newl.append(cube(item))           #   "cube" hochea function name,, 'l' hochea list jai list ar element ar upor 'cybe function' apply kortea chachi,
  newl= list(map(cube, l))          # "cube" hochea function name,, 'l' hochea list jai list ar element ar upor 'cybe function' apply kortea chachi,
                                    # 'map object' return korbea, ta list a convert kora hoy 'list' ar madhomea,
print(newl)

# #  use proper rules:
for item in l:                                  # 'for loop' banaichi 'item' name a,
  newll.append(cube(item))                      #   "cube" hochea function name,, 'l' hochea list jai list ar element ar upor 'cybe function' apply kortea chachi,
  newll = list(map(lambda x: x*x*x, l))         # 'map object' return korbea, ta list a convert kora hoy 'list' ar madhomea,
                                                # 'cube' and 'lambda' same work korea thakea,
print(newll)
print('\n')





# # FILTER
# # here is an example of hew to use the filter function:
# #   filter(predicate, iterable)

def filter_function(a):                         # 'filter_function' function create,
  return a>2                                    # condition and return function diyea return korbea,

newnewl = list(filter(filter_function, l))      # "filter function" nai ja filter korbea, and name dai 'filder_function' ; list a convert kora hoy,
                                                # function 'true or false' return korbea base on 'valu' [ 'valu' akhanea 'l'] ja deaoya hoyea thakea, ;
                                                # onno takea 'l' diyea dichi,
print(newnewl)
print('\n')





# # reduce
# # here is an example of hew to use the reduce function:
# #   reduce(function, iterable)

from functools import reduce        # 'reduce' kea prothomea import kortea hoy,

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y

# sum = reduce(mysum, numbers)        # 'reduce' diyea 'reduce' korteachi, 'mysum' function ar madhomea, r 'numbers' a ja achea oy element gulo diyea,
# "or" jea kuno akta  use korlea hobea, but nichear ta use korea Professional ra
sum = reduce(lambda x, y: x + y, numbers)       # 'reduce' diyea 'reduce' korteachi, lambda function ar madhomea number sum korteachi,
# Print the sum
print(sum)
