class Employee:
    def __init__(self, name):               # __init__ constractor
        self.name = name

    def __len__(self):                      # __len__ method
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):                      # __str__ method
        return (f'The name of employee is {self.name} str')         # ekhanea print() hobea na return hobea().


    # def __repr__(self):
    #     return (f'The name of employee is {self.name} repr')         # ekhanea print() hobea na return hobea().

    def __repr__(self):                     # __repr__ method
        return f"Employee({self.name})"




    # def __call__(self):    # __call__ method
    #     print("hey I am good")
