# Single inheritance manea base class ar data abar child class seai data use kortea parea.


class Car:
    color = "Red"
    @staticmethod
    def start():
        print('Car is start.')
    @staticmethod
    def stop():
        print("Car Engine is stop.")
class Toyotacar(Car):           # ""Toyotacar(Car)"" এখানে "> (Car) <" দিয়ে উপরের "class Car" এর ডাটা এনহেরিট(inheritance) করা হয়।
    def __init__(self, name):               # Dunder Function >>   ""  __init__ ""
        self.name = name
car1 = Toyotacar('Forchunar')
print(car1.name)
print(car1.start())
print(car1.color)



