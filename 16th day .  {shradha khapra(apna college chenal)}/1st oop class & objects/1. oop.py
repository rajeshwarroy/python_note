class Student:              # class name "Student"
    name = "Rajeshwar"
    old = 23
s1 = Student()              # "s1" is a object, "Student" is a class name and add in last 'parentheses'
print(s1)                   # print object 's1'
            # output        # ""<__main__.Student object at 0x100c3dd10>""  aykhana 'main' ar 'student on=bject' print hoyeachea,
                            # "0x100c3dd10" ay location a.
print(s1.name)
s2 = Student()
print(s2.old)





print('\n\n')
# start class
class Student:
    # start Default constructors                      #We are not create default contractor, otherwise Python, automatic create this
    def __init__(self):                             # Dunder Function >>   ""  __init__ ""
        pass
    print('Default constructors')
    # end Default constructors

    # start Parameterized Constructor                 # Parameterized Constructor hochhea, 'self parameterixed' ar sathea aro kicu 'parameterized' thakbea
    # __init__  একে বলা হয়  initialize constructor method
    def __init__(self, fullname, marks):            # 1st create a Constructor / Otherwise Why python create automatic Constructor. Hare 'fullname' is Variable.
        self.fullname = fullname                    # "self.marks" and ""__init__(self, marks)""    "marks" name same rakea sob Programmer ra
        # self.name = fullname      # XX              # ay vabea use hoyna softer company tea, Because onno programar ar bujtea problem hoyea thakea.

        self.marks = marks                  # "self.marks" and ""__init__(self, marks)""    "marks" name same rakea sob Programmer ra
        print('Adding new student id database.')
    # end Parameterized Constructor
# end class

s3 = Student('Roni', 44)                    # ""('')"" Is a constructor.     'Roni' we are passing the name.
print(s3.fullname, s3.marks)                # output === Roni 44

s3 = Student('roy', 47)
print(s3.fullname, s3.marks)                # output === Roy 47
print(s2.name)                              # output === Rajeshwar      ... aykhan a "s2" object ar data print hoyeachea.
