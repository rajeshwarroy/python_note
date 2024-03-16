class Car:
    def __init__(self, type):                   # Dunder Function >>   ""  __init__ ""
        self.type = type

    @staticmethod                   # decorator
    def start():
        print('Your car is started')
    @staticmethod                   # decorator
    def stop():
        print('Your car engine stop')


class ToyotaCar(Car):
    def __init__(self, name, type):             # Dunder Function >>   ""  __init__ ""
        super().__init__(type)
        # self.name = name
        # super().start()

car1 = ToyotaCar("Prius", "Electric")
print(car1.type)


