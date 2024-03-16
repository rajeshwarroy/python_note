class MyClass:
    def __init__(self, value):              # __init__  একে বলা হয়  initialize constructor method
        self._value = value
    def show(self):                 # methode
        print(f'value is {self._value}')
    @property                           # "@" lagailea seta property methord hoyea jay.
    def ten_value(self):
        return 10* self._value
# setters #
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

obj = MyClass(10)           # "myclass" name a class kea "obj" name a raklam.
obj.show()                  # 'obj' ar 'show' name ar jea "def function" achea oyta run hochea.
# "myclass" a "value" peyeachea "10" oy manta "def show" function a print hoyeachea.

obj.ten_value = 67          # 'myclass' ar class ar 'ten_value' name a 'def function' value pass kora

# print(obj._value)           # "MyClass()" a jea "(10)" jea valu ta niyeachi, ta "_value" tea store hoyea achea, oytai print hochea.
print(obj.ten_value)        # 'MyClass' name ar class ar .. 'ten_value' name jea def function achea oyta run hochea,
# jea man ta pass hoy oytar sathea 10 vag korano hoy, oyta abar '_value' tea rakha hoy, and 'def ten_value' function a dara print kora hoy,

obj.show()                  # 'obj' ar 'show' name ar jea "def function" achea oyta run hochea.
# 'def ten_value' name ar "function" a dara "new man" ber hoy oy value kea , 'def show' function a run korano hoy.










