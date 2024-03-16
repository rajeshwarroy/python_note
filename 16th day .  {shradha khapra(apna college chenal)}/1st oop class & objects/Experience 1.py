class Student:
    def __init__(self, name, marks):            # Dunder Function >>   ""  __init__ ""
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for valu in self.marks:
            sum += valu
        print("hello, ", self.name, "Your average mark is ", sum/3)

s1 = Student('Rajeshwar', [45, 76, 86])
s1.get_avg()

s1.name = 'Roni'
s1.get_avg()

