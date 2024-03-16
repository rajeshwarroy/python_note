# list data
l = [22,44,88,66,3,8,9,5,54]
print('normal list data print')
print(type(l))                  # "l" ata kun type ar data ta dekteachi.
print(l)

# sort data print
l.sort()                        # "l" data takea sort korteachi.
print('sort data print')
print(l)                        # data print


# reverse sort data print
print('revers data print')      # "l" data takea reverse sort korteachi.
l.sort(reverse=True)
print(l)


# list data
print('\n')
k = [12,14,18,26,3,8,9,5,44]
print(k)
k.reverse()
print('new list data')
print(k)                    # k data print
print(k.index(3))           # "3" koto number index a achea.
# count method
print(k.count(3))           # akhanea "3" kotobar achea ta dekha jay 'count' diyea.



# copy method
print('\n')
print('copy method')
print(k)
m = k                   # ""m = k"" akhanea aderkea refarence korea niyeachi.
m[0]=0                  # man "0" korea diyeachi
print(k)                # output

print('\n')
k = [12,14,18,26,3,8,9,5,44]
m = k.copy()            # "k" ar data kea copy korea "m" ar modhea niyea nichi.
m[0]=0                  # copy 'm' data ar '0' ar data '0' korea diyeachi.
print(m)                # output





# insert()
print('\n\n')
print('Insert()')
p = [12,14,18,26,3,8,9,5,44]
p.insert(3, 99)                 # data insert kora,,, '3' number position a '99' data insert kora.
print(p)                        # data output.

q = [222, 333, 444, 555]        # new data here.
w = [777, 888, 999, 1000]

p.extend(q)                     # "q" ar data niyea, ta "p" ar 'list data' ar ses/end a add korea deaoya.
print(p)                        # data output.

g = p + w + q                   # Multiple data add/sum.
print(g)
