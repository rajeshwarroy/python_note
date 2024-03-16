class Employee:
    company = 'Apple'
    def show(self):
        print(f'The name is {self.name} and company is {self.company}')

    @classmethod                # ক্লাসমেথড ডেকোরেটর, ক্লাস কে এডিট করতে সাহায্য করে থাকে, ক্লাস আর যে কোম্পানি আছে তা চেঞ্জ করতে  সাহায্য কোরিয়া থাকে
    def ChangeCompany(self, NewCompany):
        self.company = NewCompany       # NewCompany এর মাধমে নতুন নাম নিয়ে তা Company এর মধ্যে সেট করে ডে

e1 = Employee()
e1.name = 'Rajeshwar'
e1.show()

print(Employee.company)

e1.ChangeCompany('Nokia')
e1.show()

print(Employee.company)
