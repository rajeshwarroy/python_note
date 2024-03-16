class Employee:
  def __init__(self, name):     # initialize constractor create.
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):    # initialize constractor create.
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):    # initialize constractor create.
    self.dance = dance
    self.name = name

o = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())         # print(class_name.mro())     # method kothay kothay dhujbea ta dekha jay.
