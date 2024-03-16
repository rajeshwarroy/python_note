class Car():
    def __init__(self):                     # Dunder Function >>   ""  __init__ ""          # __init__  একে বলা হয়  initialize constructor method
        self.key = False
        self.clutch = False
        self.accelerator = False
        self.handbreak = False
    def start(self):
        self.key = True                     # unnecessary data not print
        self.clutch = True                  # unnecessary data not print
        self.handbreak = True               # unnecessary data not print
        print('Your Car is start.')
my_car = Car()
my_car.start()             # "Necessary data print" and "unnecessary data not print" or "Unnecessary data height"
