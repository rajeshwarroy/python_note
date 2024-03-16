# Public Access Specifier in Python
# All the variables and methods (member functions) in python are by default public.
# Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.




class Student:
    # constructor is defined
    def __init__(self, age, name):              # __init__  একে বলা হয়  initialize constructor method
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
