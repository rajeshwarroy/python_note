class Persion:
    name = 'anonymous'
    def ChangeName(self,name):              # self = object
        self.name = name
p1 = Persion()
p1.ChangeName('Rajeshwar')
print(p1.name)
print(Persion.name)







print('\n\n')
class Persion:
    name = 'anonymous'
    def ChangeName(obj,name):
        Persion.name = name
p1 = Persion()
p1.ChangeName('Rajeshwar')
print(p1.name)
print(Persion.name)




print('\n\n')
class Persion:
    name = 'anonymous'
    def ChangeName(obj,name):
        obj.__class__.name = "Roy"
p1 = Persion()
p1.ChangeName('Rajeshwar')
print(p1.name)
print(Persion.name)






print('\n\n')
class Persion:
    name = 'anonymous'

    @classmethod
    def ChangeName(cls, name):
        cls.name = name
p1 = Persion()
p1.ChangeName('Rajeshwar')
print(p1.name)
print(Persion.name)
