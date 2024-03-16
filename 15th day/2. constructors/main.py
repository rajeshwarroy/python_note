# constructors ak object kea banatea sahajjo korea thakea. 'constructors' initialization kortea help korea thakea,


class Person:
    def info(self):
        print(f'{self.name} is a {self.occation}')
a = Person()
a.name = "rajeshwar"
a.occation = "developer"
a.info()




print('\n')

class Person:
    def __init__(self):             # ""__init__"" full from "initialization"
        print('Hey baby, Keyachea ho ap lok.')

    def info(self):                 # class ar vitorea method banailea 'self' lektea hobea sob somoy,
        print(f'{self.name} is a {self.occation}')
a = Person()
b = Person()
#       "def __init__(self):"  ata print hochea, atar manea  Constructors call hoy jokhon amaara akta object banai,




print('\n\n')
class Person:
    # __init__  একে বলা হয়  initialize constructor method
    def __init__(self, name, occation):                 # 'n' & 'o' hochea 2 ta argument ja aykhanea pass kora hochea.
        # "a" and "b" ar achea "name" and "occation" achea ta self ar madhomea aykhan a pass hoy,,

        print('Hey baby, Keyachea ho ap lok.')
        self.nm = name              # 'name' data 'nm' ar moodhea rakha hoy,
        self.occ = occation         # 'occation' data 'occ' ar modhea rakha hoyeachea,

    def info(self):                 # class ar vitorea method banailea 'self' lektea hobea sob somoy,
        print(f'{self.nm} is a {self.occ}.')
a = Person('rajeshwar', 'developer')
b = Person('rajeshs', 'doctor')

a.info()        # "a.info" run hochea, "f'{self.name}'" ar madhomea 'name' data niyea asea, and 'occation' and output koray.
b.info()
