s1 = {1, 2, 3, 4, 5}            # integer data
s2 = {3, 6, 7, 2, 9}
print(s1.union(s2))             # "s1.union(s2)" akhanea s1 & s2 ar combination korea output.
s1.update(s2)                   # 's1' kea Upgrade korea 's2' ar data niyea. 's1' ar kachea ja nai ta 's2' ar kach thakea niyea upgrade hoy.
print(s1, s2)                   # "s1" and "s2" 2tai aksatha output.
print('\n')


#   union section
print('\n Union Section')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Bangkok', 'Kundu'}
# cities3=cities.update(cities2)                 # string daata update hoyna, integer data hoy.
cities3=cities.union(cities2)                   # 'union' korea ta 'cities3' tea reakha dichi.
print(cities3)



#   intersection section
print('\n Intersection Section')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Bangkok', 'Kundu'}
cities3=cities.intersection(cities2)            # intersection hochea, 'cities' & 'cities2' 2tar modhea ja comon achea ta neaoya.
print(cities3)



#   symmetric_difference
print('\n Symmetric_Difference')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Bangkok', 'Kundu'}
cities3=cities.symmetric_difference(cities2)            # symmetric_difference hochea, 'cities' & 'cities2' 2tar modhea ja comon nai ta neaoya.
print(cities3)




#   symmetric_difference_update
print('\n Symmetric_Difference_Update')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Kundu'}
cities3=cities.symmetric_difference_update(cities2)            # symmetric_difference hochea, 'cities' & 'cities2' 2tar modhea ja comon nai ta neaoya.
print(cities)                               # upgrade korchi, abar ta cities3 ta rakchi but output cities diyea print koreachi.




#   difference
print('\n Difference')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Kundu'}
cities3=cities.difference(cities2)            # difference hochea, 'cities' - 'cities2'/ [a-b] hobea..
print(cities3)




#   Difference_Update
print('\n Difference_Update')
cities = {'Tokyo', 'Madrid', 'Delhi', 'Berlin'}
cities2 = {'Tokyo', 'Dhaka', 'Delhi', 'Kundu'}
cities3=cities.difference_update(cities2)            # Difference_Update hochea, 'cities' & 'cities2' 2tar modhea ja comon nai ta neaoya.
print(cities)







print('\n')
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
