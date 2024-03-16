# class BaseClass:
#     # Base class code
#
# class DerivedClass1(BaseClass):
#     # Derived class 1 code
#
# class DerivedClass2(DerivedClass1):
#     # Derived class 2 code



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")


## Dog এর ক্ষেত্রে এসব প্রিন্ট হবে,,
## print(f"Name: {self.name}")
## print(f"Species: {self.species}")
## print(f"Breed: {self.breed}")
## print(f"Color: {self.color}")

o = Dog("tommy", "Black")
o.show_details()
print(Dog.mro())        # কোথায় কোথায় যায় তা দেখা যায়

print('\n')
## GoldenRetriever এর ক্ষেত্রে এসব প্রিন্ট হবে,,
## print(f"Name: {self.name}")
## print(f"Species: {self.species}")
## print(f"Breed: {self.breed}")
## print(f"Color: {self.color}")

o = GoldenRetriever("tyger", "white-black")
o.show_details()
print(GoldenRetriever.mro())            # কোথায় কোথায় যায় তা দেখা যায়

