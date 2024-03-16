class Student:
    college_name = 'Mathurapuur high School'
    def __init__(self, name, roll):             # Dunder Function >>   ""  __init__ ""      # __init__  একে বলা হয়  initialize constructor method
        self.name = name
        self.roll = roll
    def welcome(self):                          #method
        print('welcome student,', self.name)
    def get_roll(self):                         # method
        return self.roll


print(Student.welcome)
s1 = Student('Rajeshwar', 47)                   # method use for the objects
print(s1.get_roll())                            # method use For the objects
