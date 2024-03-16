class Complex:
    def __init__(self, real_num, imaginary_number):             # Dunder Function >>   ""  __init__ ""
        self.real_number = real_num
        self.imaginary_number = imaginary_number

    def ShowNumber(self):
        print(self.real_number, "i +", self.imaginary_number, "j")

    def __add__(self, other):                                   # Dunder Function >>   ""  __add__ ""
        newReal_number = self.real_number + other.real_number
        newImaginary_number = self.imaginary_number + other.imaginary_number
        return Complex(newReal_number, newImaginary_number)

    def __sub__(self, other):                                   # Dunder Function >>   ""  __sub__ ""
        newReal_number = self.real_number - other.real_number
        newImaginary_number = self.imaginary_number - other.imaginary_number
        return Complex(newReal_number, newImaginary_number)

num = Complex(6, 3)
num.ShowNumber()

number = Complex(3, 5)
number.ShowNumber()

number2 = Complex(2, 6)
number2.ShowNumber()

print('\n\none + two')
sum_number = num + number
sum_number.ShowNumber()

print('\n\none - three')
sum_number = num - number2
sum_number.ShowNumber()
