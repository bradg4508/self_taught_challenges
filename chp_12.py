#1
class Apple():
    def __init__(self, c, w, s, t):
        self.color = c
        self.weight = w
        self.shape = s
        self.taste = t

apple = Apple("Red", 10, "Circle", "Yummy")


#2
import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi*self.radius**2

circle = Circle(4)
print(circle.area())


#3
class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return .5*self.base*self.height

triangle = Triangle(2,5)
print(triangle.area())


#4
class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
        

    def calculate_perimeter(self):
        return (self.side1 + self.side2 + self.side3 +
                self.side4 + self.side5 + self.side6)

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
