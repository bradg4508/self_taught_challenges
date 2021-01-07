#1
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return 2*self.length + 2*self.width

class Square():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4*self.side

one_rec = Rectangle(3,8)
one_sq = Square(4)

print(one_rec.calculate_perimeter())
print(one_sq.calculate_perimeter())


#2
class Square():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4*self.side

    def change_size(self, c):
        self.change = c
        self.side += self.change

two_sq = Square(5)
print(two_sq.side)

two_sq.change_size(4)
print(two_sq.side)


#3
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return 2*self.length + 2*self.width
    
class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4*self.side

two_rec = Rectangle(7,4)
three_sq = Square(9)

two_rec.what_am_i()
three_sq.what_am_i()


#4
class Horse():
    def __init__(self, name, color, owner):
        self.name = name
        self.color = color
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name

the_rider = Rider("Robby")
the_horse = Horse("Lucky", "brown", the_rider)

print("The name of the Horse is {}.".format(the_horse.name))
print("The name of the Rider is {}.".format(the_horse.owner.name))
