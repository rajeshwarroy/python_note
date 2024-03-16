print(' python dictionaries')
dic = {
    10: "Welcome",                          # "10" hochea key, and "Welcome" hochea value.
    "Rajeshwar": "Good morning.",           # "Rajeshwar" hochea key, and "Good morning" hochea value.
    "Roy": "Have a good day.",
    "Roni": "Good night."
}
print(dic[10])                              # akta key ar value deakha jay, Multiple not allowed.
print(dic["Rajeshwar"])




print('\n')
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)                             # dictionary data show hobea.
# print(info[name2])                      # "name2" name kuno key nai, tai error dibea.
print(info.get("name2"))                # "name2" name kuno key nai, tai none output dibea.
print(info.keys())                      # "info" ar all key show hobea ".keys" ar madhomea.
print(info.values())                    # "values" ar madhomea "info"ar all value show hobea.

print('\n')
print(info.keys())                      # only key show
for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")         # "key" show kora jay.

print('\n')
print(info.items())                     # key and value show
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")             # "key" and "value" show kora jay.
