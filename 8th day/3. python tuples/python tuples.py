# tuples kokhono change kora jay na

# tuple are ordered collection of data items. they store multiple items in a single variable. tuple items ate separated by  commas and enclosed within round brackets (). tuples are unchangeable meaning, we cannot alter them after creation.

tup = ( 1 )
print(type(tup), tup)

tup = (1, 3, 5, 'Red', 'Green')
# tup[1] = 9                # not changeable.
print(type(tup), tup)

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-4])


if 5 in tup:
    print("Yes 5 is present in this tuple")


# Range of index
print('\n\nRange of index')
tup2= tup[1:5]
print(tup2)
