# For loop

name = 'Rajeshwar'
for i in name:
    print(i)
    if i== "j":
        print("This is something special!")         # i = j pailea j ar datar porea ayta print hobea.
print('\n')

colors = ["Red", "Blue", "Green", "White", "Black"]
for color in colors:
    print('\n', color)
    for i in color:
        print(i)

print('\n\n')
# Range()
for k in range(9):
    print(k)            # range(9) boltea ..... 0-8 porjonto print hobea
    # print(k+1)          # range(9) boltea ..... 1-9 porjonto print hobea.... k+1 boltea ka ar man 0, 0+1=1, tai 1st man 1 hobea. 1 thakea print hoyea cholbea
    # print(k+2)          # range(9) boltea ..... 3-10 porjonto print hobea.... k+2 boltea ka ar man 0, 0+2=2, tai 1st man 2 hobea. 2 thakea print hoyea cholbea


# for k in range(100, 200):           # start number 100 and end number 200..
#     print(k)


print('\n\n')
# stape
for i in range(1, 20, 3):
    print(i)
