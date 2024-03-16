class Employee:
    companyName = 'Apple'           # কোম্পানির নাম এখানে ক্লাস আর সাথে এসোসিয়েট হয়ে আছে
    noOfEmployees = 0               # ০ সেট করে দেই প্রথম ও তো
    def __init__(self, name):       # __init__  একে বলা হয়  initialize constructor method
        self.name = name            # নেম এখানে __init__ আর সাথে এসোসিয়েট হয়ে আছে
        self.raise_amount = 0.2
        Employee.noOfEmployees +=1     # এমপ্লয়ী সংখ্যা বাড়বে এক এক করে
    def ShowDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}.")

emp1 = Employee('Roni')         # এমপিএলের নাম দিচ্ছি
# Employee.ShowDetails(emp1)      # এভাবেও দেখা যায়                # এই নিয়মটা আকটু কঠিন।
emp1.ShowDetails()              # আউটপুট এভাবে দেখতে হয়

print(Employee.companyName)     # কোম্পানির নাম এভাবেও দেখা যায়।

Employee.companyName = 'Bangladesh apple'         # এখানে কোম্পানির নাম ক্লাস আর সাথে এসোসিয়েট হয়ে আছে। এখন থেকে সব সময় জন্য এইটা নেম সেট কড়া হইল। আবার চেঞ্জ করলিয়া তক্ষণ আবার চেঞ্জ হবে।


emp1.companyName = "India apple"                  # এখানে কোম্পানির নাম emp1 আর সাথে এসোসিয়েট হয়ে আছে। তাই emp1 এর জন্য এই নাম সেট হবে অন্য দেড় জন্য হবে না।
emp1.raise_amount = 0.4         # এভাবে ডাইরেকলী এক্সেস নিয়ে মান  চেঞ্জ কোরতে পারি
emp1.ShowDetails()              # আউটপুট এভাবে দেখতে হয়


emp2 = Employee("Rajeshwar")    # এমপিএলের নাম দিচ্ছি
emp2.ShowDetails()              # আউটপুট এভাবে দেখতে হয়


Employee.companyName = 'ঠাকুরগাঁও আপেল '         # এখানে কোম্পানির নাম ক্লাস আর সাথে এসোসিয়েট হয়ে আছে। এখন থেকে সব সময় জন্য এইটা নেম সেট কড়া হইল। আবার চেঞ্জ করলিয়া তক্ষণ আবার চেঞ্জ হবে।
emp2.raise_amount = 2.2         # এভাবে ডাইরেকলী এক্সেস নিয়ে মান  চেঞ্জ কোরতে পারি
emp2.ShowDetails()              # আউটপুট এভাবে দেখতে হয়


