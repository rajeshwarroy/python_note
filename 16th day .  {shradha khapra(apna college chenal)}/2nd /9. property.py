class Student:
    def __init__(self, phy, chams, math, bio):      # Dunder Function >>   ""  __init__ ""
        self.phy = phy
        self.chams = chams
        self.math = math
        self.bio = bio

    @property
    def percentage(self):
        return str((self.phy+self.bio+self.math+self.chams) / 4) + " %"

result = Student(95, 92, 97, 94)

print(result.percentage)




result.math = 55
print(result.percentage)
result.chams = 33
print(result.percentage)
