letter = "Hey my name is {} and i am from {}"
country = "Bangladesh"
name = "Rajeshwar"
print(letter.format(name, country))  # format ar madhomea "name" cholea jabea first "{}" and "country" cholea jabea "{}" tea

print('\n')
letter = "Hey my name is {1} and i am from {0}"
country = "Bangladesh"
name = "Rajeshwar"
print(letter.format(country, name))         # "number" ar madhomea format thik korea dioyea jay.    ....



# *****         F-String        ******
letter = f"Hey my name is {name} and i am from {country}"     # 'f' likhar manea ayta "f-string". Directly Variable "{}" lika jay.
country = "Bangladesh"                                    # "country" sora sori variable a use kora jay 'f-string' ar madhomea.
name = "Rajeshwar"
print(letter)





#   format ar madhomea
tex = "For only {price:.2f} dollers!"
print(tex.format(price=49.43534))               # ".2f" atar manea,, <point two decimal> porjonto number neaoya
tex = "For only {price:.2f} dollers!"
print(tex.format(price=49))


#   f-string ar madhomea
print('\n')
price = 76.9584
tet = f"For only {price:.2f} dollars!"
print(tet)








print('\n')
val = "Geeks"
print(f"{val}for{val} is a portal for {val}.")

name = 'Rajeshwar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
