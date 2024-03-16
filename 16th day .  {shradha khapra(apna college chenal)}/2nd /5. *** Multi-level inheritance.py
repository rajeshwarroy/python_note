class Car:
    @staticmethod
    def start():
        print('Car is start.')
    @staticmethod
    def stop():
        print("Your car engine is stop.")

class ToyotaCar(Car):
    def __init__(self, brand):                  # Dunder Function >>   ""  __init__ ""
        self.brand = brand

class Premeo(Car):
    def __init__(self, type):                   # Dunder Function >>   ""  __init__ ""
        self.type = type

c1 = Premeo("Hybrid")
c1.start()
