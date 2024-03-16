class Employee:
    def __init__(self, role, dept, salery):
        self.role = role
        self.dept = dept
        self.salery = salery

    def showDetails(self):
        print("role =", self.role)
        print("department = ", self.dept)
        print("salery =", self.salery)

class Engineering(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__('Engineer', 'IT', '60,000')

    def engDetails(self):
        print('name =', self.name)
        print('role =', self.role)
        print('dep =', self.dept)
        print('age =', self.age)
        print('salary =', self.salery)

empl = Employee ("Software", "CSE", "35,000")
empl.showDetails()

print('\n\n')
eng = Engineering('Rajeshwar', '23')
eng.engDetails()
