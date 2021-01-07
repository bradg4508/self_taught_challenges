#1
class Square():
    square_list = []
    
    def __init__(self, s):
        self.side = s
        self.square_list.append(self)

one_sq = Square(5)
print(Square.square_list)
two_sq = Square(12)
print(Square.square_list)


#2
class Square():
    def __init__(self, s):
        self.side = s

    def __repr__(self):
        return "{} by {}".format(self.side,self.side)

three_sq = Square(14)
print(three_sq)
four_sq = Square(18)
print(four_sq)


#3
def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))
print(compare("c", "c"))
        
