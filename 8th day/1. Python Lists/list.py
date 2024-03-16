#>>        colors = ["Red", "Green", "White", "Blue", "Yellow"]
#>>          #       [0]      [1]     [2]       [3]     [4]


marks = [4, 5, 6, "Rajeshwar", True, False]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print('\n')
#>>        colors = ["Red", "Green", "White", "Blue", "Yellow"]
#>>          #       [-5]    [-4]     [-3]     [-2]     [-1]
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[-5])
print(marks[-6])
print('\n')




number = [44, 55, 66, "Rajeshwar"]
print(number[-3])                       # Negative index
print(number[len(number)-3])            # positive index
print(number[5-2])                      # positive index
print(number[3-2])                      # positive index
print(number[1])                        # positive index
print('\n')
if 'Rajeshwar' in number:
    print('yes')
else:
    print('no')
if 44 in number:
    print('yes')
else:
    print('no')

if '66' in number:
    print('yes')
else:
    print('no')




## jump index

# Same thing applies for string as well!
if 'ajeshwar' in number:
    print('yes')
else:
    print('no')



print('\n')
marks = [1, 2, 3, "Rajeshwar", 4, 5, 6]
print(marks)            # normal ayvabea print kori
print(marks[:])         # but avabeao print kora jay
print(marks[1:])         # len dhorea print kora jay
print(marks[1:6])        # len dhorea print kora jay
print(marks[1:-1])       # len dhorea print kora jayx                    #Negative
print(marks[1:7:2])      # len dhorea print kora and 2ta korea lafiyea jabea.
print(marks[-3:])
print(marks[:-3])



print('\n')
lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
