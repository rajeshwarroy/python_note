ep1 = {111: 34, 222: 54, 333: 52, 444: 98, 555:76}
ep2 = {232: 74, 343: 36, 454: 76}
ep1.update(ep2)             # "ep1" upgrade hochea "ep2" ar kachea data niyea.
print(ep1)
ep2.clear()                 # "ep2" ar Dictionary ar data clear korea dibea,
print(ep2)                  # "ep2" ka "empty Dictionary" print hobea.

ep1.pop(222)                # "pop()"hochea, "ep1" ar "222" ar key and value remove korea dibea.
print(ep1)

ep1.popitem()               # "popitem()" ar kaj hochea, last "key" and "value" remove korea dibea,
print(ep1)



# del ep1                     # "key" na dilea puro Dictionary delete korea dibea.
del ep1[444]                # string hoylea <""> use kortea lagbea, intger hoylea <""> use korar lagbea na.
print(ep1)                  # "del" ar madhomea jeakuno Position ar key and value delet kora jay.

