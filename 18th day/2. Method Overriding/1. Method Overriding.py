class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)            # super().__init__(radius, radius) << এর মাধমে parent_method ক্লাস এর ইনিটিয়লিজে কল হবে, ক্লাস রান হবে।

    def area(self):
        return 3.14 * super().area()                # 𝝅r^2


a = Shape(4, 8)
print(a.area())


c = Circle(5)
print(c.area())
