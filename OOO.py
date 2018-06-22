class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))


        def print_size(self):
            print("""{} by {}""".format(self.width, self.len))


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)



x = AlwaysPositive(-20)
y = AlwaysPositive(10)

roger = Lion("Roger")
same_roger = roger
print(roger is same_roger)

another_roger = Lion("Tom")
print(another_roger is roger)

z = -30 + 10
print(z)

print(x + y)

lion = Lion("Dilbert")
print(lion)

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)




def none_check(x):
    if x is None:
        print("x is none :(")
    else:
        print("x is not None")


none_check(10)
none_check(None)

