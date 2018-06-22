class Square:
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

    def print_side(self):
        print("{} by {} by {} by {}".format(self.side, self.side, self.side, self.side))


def true_false(x, y):
    if x == y:
        return True
    else:
        return False

sq1 = Square(4)
sq2 = Square(3)
print(Square.square_list)
print(sq1)
print(sq1.print_side())

z = true_false(10, 11)
print(z)

zz = true_false(10, 10)
print(zz)

