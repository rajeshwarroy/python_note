def average(*numbers):
    sum = 0
    for i in numbers:
        sum=sum+i
    print("average number is: ", sum/ len(numbers))

average(30,88,77)
print('\n')



def average(*numbers):
    sum = 0
    for i in numbers:
        sum=sum+i
    # print("average number is: ", sum/ len(numbers))
    return sum/len(numbers)                     # "return"    << atar manea jea man paichea or achea ayta niyea cholea jaoya,, ta "a" kea diyea dibea..
a=average(3,8,7)
print(a)
print('\n')




#keyword arditrary arguments:
def name(**name):
    print(type(name))
    print("Hello,", name['fname'],name['mname'],name['lname'],name['nname'])
name(nname="M2", mname="Book", fname="Mac", lname="Pro")
