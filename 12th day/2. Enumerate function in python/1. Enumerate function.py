marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0                             # index declare korea ditea hobea, 1st number koto number index,
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Rajeshwar, awesome!")
#   index +=1                           # loop jeavabea cholbea, satha sathea index ar value update korar lagbea,


for index, mark in enumerate(marks):    # "Enumerate( )" function bolea aytakea, ; "mark" dibea value & "index" dibea index ar man,
  print(mark)
  if(index == 3):
    print("Rajeshwar, awesome!")



print('\n')
for index, mark in enumerate(marks, start=1):       # "Enumerate( )" function bolea aytakea, "start=1" manea 1 thakea start hobea;
  print(mark)                                       # "mark" dibea value & "index" dibea index ar man,
  if(index == 3):                                   # "mark" ar 3 number, "3 number position" por print hobea ayta bujhaichea,
    print("Harry, awesome!")
print('\n')






# 2nd program

fruits =['apple', 'banana', 'mango', 'Jackfruit']
for index, fruit in enumerate(fruits, start=1):
  print(index, fruit)


print('\n')
fruits =['apple', 'banana', 'mango', 'Jackfruit']
for index, fruit in enumerate(fruits):
  print(f'{index+1}: fruit')
