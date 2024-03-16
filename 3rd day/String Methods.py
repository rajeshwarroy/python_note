# string are immutable
from numpy.core.defchararray import capitalize

a = 'Rajeshwar'
print(len(a))
print(a.upper())            # existing string, not change, existing string operation then create a new string.
print(a.lower())            # existing string, not change, existing string operation then create a new string.
print('\n')

# rstrip()
b = '!!!@Macbook!!!!@@'
print(len(b))
print(b.rstrip('!@'))           # sudhu last ar dikea kaj korea thakea.
print('\n')

# replace
a = 'Rajeshwar is a boy, and Rajeshwar good boy.'
print(a.replace('Rajeshwar', 'Roni'))           # Rajeshwar<<< name a joto word thakbea sob change hoyea jabea..

# split()
print(a.split(' '))

# capitalize
blog = 'introduction to js.'
blog1 = 'intRoduction tO jS.'
print(blog.capitalize())                        # 1st word capital and other sentence and Character lower case korea dibea.
print(blog1.capitalize())                       # kothao capital thaklea ta lower-case korea dibea.
print('\n')


# center()
# the center() method aligns the string to the center as per the parameters given by the user.
print(len(blog))
print(blog.center(50))
print(a.count('Rajeshwar'))                     # akhanea ''Rajeshwar'' kotobar achea ta count hobea and ta dekhabea.


# endswith()
# the endswith() method checks if the string ends with a given value. If yes then return True, else return false.
str1 = 'Welcome to the Cousole !!!'
str2 = 'Welcome me facebook to the Cousole !!!'
print(str1.endswith('!!!'))                     # akhanea '''!!!''' ar madhomea line end hochea kina ta dekteachea. jodi hoy taholea true..
print('\n')

print(str1.endswith('to', 4, 10))               # 4-10 ar modhea ""to"" diyea ses hochea kina, hoylea true hobea.
print(str2.endswith('to', 4, 10))               # 4-10 ar modhea ""to"" diyea ses hochea kina, hoylea true hobea.

str3 = "He's name is Dan. He is an honest man."
print(str3.find('is'))                          # akhanea dakbea "is" koto number a achea ta print hobea. and first a ja pabea oytai nibea
                                                # Because Python is interpreting, that's why he cannot detected, aykhanea koyta "is" achea.
print(str3.find('iss'))                         # khujea na pailea ""-1"" return korea dibea.
print(str3.index('is'))

print('\n')
str4 = 'WelcomeToTheConsole'
str5 = 'Welcome00'
# isalnum()
print(str4.isalnum())                           # The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
                                                # If any other characters or punctuations are present, then it return False.

# isalpha()
print(str5.isalpha())                           # The isalpha() method returns True only if the entire string only consists of A-Z, a-z.
                                                # If any other characters or punctuations or numbers(0-9) are present, then it return False.

# islower()
print(str4.islower())                           # lower-case badetea upper-case pailea False return korbea.

print('\n isprintable() ')
str6 = 'we wish you a Merry Christmas'
str7 = 'We wish you a Merry Christmas\n'
print(str6)
print(str6.isprintable())
print(str7)
print(str7.isprintable())
print('\n')

# title()
print(str6.title())                             # all string first word capital and all word lower korea dibea.
print(str7.swapcase())                          # Lower to capital and capital to lower korea dibea "swapcase".





