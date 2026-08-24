import math

class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def calculate(self):
        area = math.pi * self.radius ** 2
        print("Area of Circle =", area)


class Sphere(Shape):
    def calculate(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        print("Volume of Sphere =", volume)


r = float(input("Enter radius: "))

c = Circle(r)
c.calculate()

s = Sphere(r)
s.calculate()