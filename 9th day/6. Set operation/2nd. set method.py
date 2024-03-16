print(' Isdisjoint')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Bangkok', 'Kundu'}
cities3=cities.isdisjoint(cities2)            # same hoylea false hobea.
print(cities3)


cities = {'Tokyo1', 'Madrid', 'Delhi1', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Bangkok', 'Kundu'}
cities3=cities.isdisjoint(cities2)            # mil na thaklea true hobea.
print(cities3)




print('\n Issuperset')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Dhaka', 'Bangkok', 'Kundu'}
cities3 = {'Tokyo', 'Delhi'}
print(cities.issuperset(cities2))            # "Issuperset" hochea, 2jaygay data mill acha ki na. nai tai "false" hoyeachea
print(cities.issuperset(cities3))            # "Issuperset" hochea, 2jaygay data mill achea tai "true" hoyeachea.


print('\n Issubset')
print(cities3.issubset(cities))             # "cities3" ar sob data "cities" ka vitor achea. tai "true" hoyeachea.
print(cities3.issubset(cities))             # "cities3" ar sob data "cities" ka vitor achea. tai "true" hoyeachea.






print('\n Add')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities.add("Dhaka")       # "Add" diyea 1kta data add hoyea thakea.
print(cities)




print('\n update')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Dhaka', 'Bangkok', 'Kundu'}
cities.update(cities2)                  # "update" ar madhomea "Multiple data" add kora jay.
print(cities)



print('\n remove / discard')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities.remove('Tokyo')              # "remove" ar madhomea "data" remove kora jay.
print(cities)

# cities.remove('Tokyo2')           # "remove" ar madhomea "data" remove kora jay. but oy "data" na thaklea "error" dekhabea.
# print(cities)

cities.discard('Delhi')             # "discard" ar madhomea "data" remove kora jay. "data na thakleao error chara" kora jay
print(cities)
cities.discard('Delhi2')             # "discard" ar madhomea "data" remove kora jay. "data na thakleao error chara" kora jay
print(cities)





# print('\n Del')
# citiess = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
# del citiess                # "del" ar madhomea sob data delete korea deaoya jay.
# print(citiess)



print('\n')
print('\n clear')
cities11 = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities11.clear()                # "clear" ar madhomea set ar sob data delete korea deaoya jay.
print(cities11)





print('\n')
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
