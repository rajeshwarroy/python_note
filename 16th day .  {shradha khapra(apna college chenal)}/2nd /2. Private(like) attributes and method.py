class Account:
    def __init__(self, account_no, account_pass):       # __init__  একে বলা হয়  initialize constructor method
        self.account_no = account_no
        self.__account_pass = account_pass              # ""__account_pass"" এর সামনে '__' দিয়ে প্রাইভেট কোরিয়া দিয়েছি, বাইরে থেকে কেউ এক্সেস না করতে পারে।
    def resset_pass(self):
        print(self.__account_pass)
acc = Account(678543, "ghdg78")
print(acc.account_no)
print(acc.resset_pass())                                # ক্লাস আর মধ্যে থাকলে প্রাইভেট ডাটা এইভাবে দেখা যায় ।
# print(acc.__account_pass)                               # প্রোটেট প্রাইভেট ডাটা বাইরে থাকে এক্সেস কড়া যায়  না ।



print('\n\n')
class Public:
    __name = 'Rajeshwar'

    def __hello(self):# এইটা মেথড
        print("Hello person!", '__name')
    def welcome(self):               # এখানে "__hello" কাজ করবে কারণ প্রাইভেট মেথড কে শুধু "class" এর মধ্যে ব্যবহার করা যায়।
        self.__hello()
p1 = Public()
# print(p1.__name)                   # error দেখবে ""__"" এটা দেওয়ার জন্য কারণ এইটা প্রাইভেট করে দেয়
# print(p1.__hello)                  # error দেখবে ""__"" এটা দেওয়ার জন্য কারণ এইটা প্রাইভেট করে দেয়
print(p1.welcome())
