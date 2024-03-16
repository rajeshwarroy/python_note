class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee('Rajeshwar', 12000)
print(e1.name)
print(e1.salary)

string = 'Roni-150-00'              # স্ট্রিং ফাইল থাকে ডাটা বের করতে  হইলে এইভাবে বের করা  যাবে।
e2 = Employee(string.split("-")[0], string.split("-")[1])           # (string.split("-") এখানে ("-") পেলে তা আলাদা আলাদা এলিমেন্ট করে ভাগ করে দিবে। যতবার "-" ডেস পাবে কয়টি এলিমেন্ট এ ভাগ করবে।
print(e2.name)
print(e2.salary)




print('\n')
class Employee:
    # কনস্ট্রাক্টর ডাটাকে এনিসিলাইজ করে দিয়ে থাকে।
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # self.model = model
    @classmethod
    def fromStr(cls, stringg):
        return cls(stringg.split("-")[0], stringg.split("-")[1])        # (string.split("-") এখানে ("-") পেলে তা আলাদা আলাদা এলিমেন্ট করে ভাগ করে দিবে। যতবার "-" ডেস পাবে কয়টি এলিমেন্ট এ ভাগ করবে।

e1 = Employee('Rajeshwar', 12000)
print(e1.name)
print(e1.salary)

stringg = 'Macbook_Pro-m2'              # স্ট্রিং ফাইল থাকে ডাটা বের করতে  হইলে এইভাবে বের করা  যাবে।

e3 = Employee.fromStr(stringg)           #  ফাইল  থাকে ডাটা নিয়ে, সেটাকে ক্লাসমেথড এ পাঠিয়ে ওইখান থাকে ডাটা এলিমেন্ট গুলো আউটপুট করানো হোছে।
print(e3.name)
print(e3.salary)





print('\n')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)
