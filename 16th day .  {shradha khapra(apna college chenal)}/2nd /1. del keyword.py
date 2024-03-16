class Student:
    def __init__(self, name):               # Dunder Function >>   ""  __init__ "" # __init__  একে বলা হয়  initialize constructor method
        self.name = name

s1 = Student('Roni')
print(s1)
print(s1.name)
del s1.name             # "del" diyea 'name' delete korea daoya hoyeachea.
print(s1.name)
