class Student:
    college_name = 'Mathurapur Public High School'      # "college_name" class attribute
    create = 10                                          # class attribute
    # start Parameterized Constructor               # Parameterized Constructor hochhea, 'self parameterixed' ar sathea aro kicu 'parameterized' thakbea
    def __init__(self, fullname, marks):            # 1st create a Constructor / Otherwise Why python create automatic Constructor. Hare 'fullname' is Variable.
        self.fullname = fullname                    # Object attribute
        self.marks = marks                          # Object attribute
    # end Parameterized Constructor
# end class

s1 = Student('Roni', 44)                    # ""('')"" Is a constructor.     'Roni' we are passing the name.
print(s1.fullname, s1.marks)                # output === Roni 44

s3 = Student('roy', 47)
print(s1.fullname, s1.marks)                # output === Roy 47
print(Student.college_name, ", Since", Student.create)                      # output === Mathurapur Public High School
