# Tuples are immutable, hence if you went to add remove or change tuple items, then first you must convert
# the tuple to a list. Then perform operation on that list and convert it back to tuple.



countries = ("Spain", "Italy", " India", "Bangladesh", "Germany", "Nepal")
temp = list(countries)                  # change tuple to list item
temp.append("Russia")                   # add item in last position.
temp.pop(3)                             # remove item.
temp[2] = "Finland"                     # change item.
countries = tuple(temp)                 # change list to tuple.
print(countries)
print('\n')


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)                         # count in tuple1 "3" item
# res = tuple1.index(31)                        # koto number position a achea.
# res = tuple1.index(311)                       # error
# res = tuple1.index(3, 4 , 8)                  #
res = len(tuple1)                             # tuple length.
print('Count of 3 in tuple1 is:', res)
