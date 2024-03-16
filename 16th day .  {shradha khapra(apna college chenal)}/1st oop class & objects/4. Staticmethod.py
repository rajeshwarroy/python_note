class Student:
    def __init__(self, name, marks):            # Dunder Function >>   ""  __init__ ""       # __init__  একে বলা হয়  initialize constructor method
        self.name = name
        self.marks = marks

    # start Static function -> method
    @staticmethod              # '(self)' na liktea chailea    and  error kea hatanor jonno use kora hoy,  # ata staticmethod
                               # Static function -> method
    def my():
        print('I learn Python')
    # end Static function -> method


    def get_avg(self):
        sum = 0
        for valu in self.marks:
            sum += valu
        print("hello, ", self.name, "Your average mark is ", sum/3)

s1 = Student('Rajeshwar', [45, 76, 86])
s1.get_avg()

s1.name = 'Roni'
s1.get_avg()

s1.my()
