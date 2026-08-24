import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def angles(self):
        angle1 = math.degrees(math.acos(
            (self.side2**2 + self.side3**2 - self.side1**2)
            / (2 * self.side2 * self.side3)
        ))

        angle2 = math.degrees(math.acos(
            (self.side1**2 + self.side3**2 - self.side2**2)
            / (2 * self.side1 * self.side3)
        ))

        angle3 = 180 - angle1 - angle2

        return angle1, angle2, angle3


class EquilateralTriangle(Triangle):
    def calculate(self):
        area = (math.sqrt(3) / 4) * self.side1**2
        print("Area of Equilateral Triangle =", area)

    def tangent(self):
        a1, a2, a3 = self.angles()

        print("Tan of Angle 1 =", math.tan(math.radians(a1)))
        print("Tan of Angle 2 =", math.tan(math.radians(a2)))
        print("Tan of Angle 3 =", math.tan(math.radians(a3)))


class Scalene(Triangle):
    def calculate(self):
        perimeter = self.side1 + self.side2 + self.side3

        s = perimeter / 2
        area = math.sqrt(
            s * (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

        print("Perimeter =", perimeter)
        print("Area =", math.ceil(area))


side = float(input("Enter side of equilateral triangle: "))

eq = EquilateralTriangle(side, side, side)
eq.calculate()
eq.tangent()


print("\nScalene Triangle")

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

sc = Scalene(a, b, c)
sc.calculate()