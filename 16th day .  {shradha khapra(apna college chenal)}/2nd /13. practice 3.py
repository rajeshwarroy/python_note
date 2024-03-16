class Order:
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

ord1 = Order('potato', 30)
ord2 = Order("Orange", 24)

print(ord1 > ord2)
