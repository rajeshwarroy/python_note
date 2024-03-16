names = 'rajeshwar,roy'
print(names[0:9])       # 0 thaeka start hoy and 8 number porjonto print hobea. 9 number print hobea na.

# we can find the length of a string using len() function.
print(len(names))       # lenth print hobea kotogulo achea, 0 theka start hobea.
print('\n')

fruit = 'Mango'
len1 = len(fruit)
print('Mango is a', len1, 'letter word.')
print(fruit[0:5])       # including 0 but not 5
print(fruit[:3])        # Python very intelligent, oyjonno 0 na likleao python 0 automatic niyea nay.
                        # 0 including 0 but not 3

print('\n')

# 2 tai akoy bujhay
print(fruit[0:-3])                      # 0 thaeka print and last 3 word bad jay
print(fruit[0:len(fruit) - 3])          # 0 thaeka print and last 3 word bad jay
print(fruit[-4:])                       # Slicing using negative index.

print('\n')
apple = 'mackbook'
print(apple)
print(apple[-7:len(apple) - 3])         # aylkhan a -7 hochea, length of -7, last thakea 0-7 ta word and 7 number word kokhono print hoy na,
                                        # -3 hochea length of -3, ja last thakea -3, -3 word tao print hobea...
                                        # taholea -7:-3 hobea,, mackbook ar -7(ackbook) and -3(mackb) ....output "ackb"
print(apple[-3:-1])                     # -3 = ook and -1 = mackboo ...... output ""oo""


