class Employee:                     # class create name of employee
    # __init__  একে বলা হয়  initialize constructor method
    def __init__(self, name, id):       # methord, akhanea amader dorkor "name and id" oy jonno "name" and 'id' neaoya hoyea chea,
        self.name = name                # name ar name name a rakchi
        self.id = id                    # id ar name id a rakchi.

    def showData(self):                 # again Method create
        print(f'The name  of Employee: {self.id} is {self.name}')

e1 = Employee('Rajeshwar', 34)          # "'Rajeshwar',34" data pass "'def __init__(self, name, id)'" aykhanear 'name' & 'id' tea.
                                        # "self.name=name" & "self.id=id" akhanea asea; {self.id}{self.name} akhan diyea print hoy.
e1.showData()                           # "class Employee:" name class ar "def showData(self):" name function method print hoy.

e2 = Employee('Roni', 400)
e2.showData()
print('\n')






# rename #

class Employee:
    def __init__(self, name, id):           # __init__  একে বলা হয়  initialize constructor method
        self.name = name
        self.id = id
    def showData(self):
        print(f'The name  of Employee: {self.id} is {self.name}')
class Programmer(Employee):             # "Programer" ar father "Employee", oyjonno "Employee" class ar all data and nijear sob data "Programmer" ar kachea achea.
    def showlanguage(self):
        print("The default language is Python.")

e1 = Employee('Rajeshwar', 34)
e1.showData()
e2 = Programmer('Roni', 400)    # ""'Roni', 400"" data "class Programmer" ar father "class Employee" ar  "def __init__(self, name, id)" function ar kaachea pathiyea diyeachea. [father ar kachea data/value chilo na, akhon oyta modify korea hochea.]
e2.showData()
e2.showlanguage()               # "class Programmer" ar "def showlanguage" print hoyeachea,
