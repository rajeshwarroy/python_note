### Super Method এর কাজ হচ্ছে "চাইল্ড ক্লাস" থাকে উপরের ক্লাস এ "পেরেন্ড ক্লাস" এ যেয়ে "পেরান্ড ক্লাস এর মেথড" কে কল করা

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()     # super().parent_method() << এর মাধমে parent_method ক্লাস কল হবে, ক্লাস রান হবে।

child_object = ChildClass()
child_object.child_method()         # child_method সবটাই রান হোছে।






print('\n')
class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()






print('\n')
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__(name, id)     # এখানে "" __init__( name, id) "" 'ফাংশন' টা "পেরেন্ড ক্লাস" এর মাধমে চালাই নিয়েছি "সুপার কী" আর মাধমে
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)

q1 = Programmer("Rajeshwar", "4567", "Data science")
print('\n')
print(q1.name)
print(q1.lang)
print(q1.id)
