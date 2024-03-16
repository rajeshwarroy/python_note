
def add(a, b):      # "staticmethod" a 'self' diyea lagea na,
    return a + b


class Math:                             # class
    def __init__(self, num):            # method            # __init__  একে বলা হয়  initialize constructor method
        self.num= num                   # name set
    def addtonum(self, n):              # method ar modhea Always'self' ditea hoy,
        self.number = self.num + n

    @staticmethod       # "staticmethod" sob somoy class ar modhea thakea,
    def add(a, b):      # "staticmethod" a 'self' diyea lagea na,
        return a + b

a = Math(5)             # "Math(5)" num a jabea self ar madhomea, "class Math" ar "def __init__(self, num)" akheana,
print(a.num)            # "self.num" ata print hochea, "num" ar data ta,

a.addtonum(6)           # "class Math" ar "def addtonum(self, n)" a "n" ar man "6" hoy 'self' ar madhomea,
print(a.number)         # "self.number" print hoy,; "self.num + n" akhanea 'def __init__(self, num)' ar 'num' + "def addtonum(self, n)" ar 'n' ar sathea,
                        # self.num + n = 6 +5 = 11;  "self.number" a set hoy oytai print hoy.

print(a.add(8, 9))      # class name change and function name dhorea run kora jay,
print(Math.add(3, 5))   # class name dhorea and function name dhorea run kora jay,
print(add(5, 5))        # class ar bairea, ayvabea run kora jay.
