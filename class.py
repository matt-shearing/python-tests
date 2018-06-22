import math


class Apple:
    def __init__(self, w, c, t, s):
        """weights are in grams"""
        self.weight = w
        self.colour = c
        self.type = t
        self.country = s


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius * self.radius)


class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height) / 2


class Hexagon:
    def __init__(self, l):
        # length is 1 hexagon side in cm
        self.length = l

    def perimeter(self):
        return self.length * 6


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))


    def what_am_i(self):
        print("I am a shape!")


class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

    def calculate_perimeter(self):
        return (self.width * 2) + (self.len * 2)

    def change_size(self, change):
        self.width = self.width + change
        self.len = self.len + change


class Rectangle(Shape):
    def calculate_perimeter(self):
        return (self.width * 2) + (self.len * 2)

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, name, type, rider):
        self.name = name
        self.rider = rider
        self.type = type


class Rider:
    def __init__(self, name):
        self.name = name


a_rider = Rider("Jon")
a_horse = Horse("Bobby", "Gelding", a_rider)

print(a_horse.rider.name)
print("A {} named {}".format(a_horse.type, a_horse.name))


matt = Person("Matt Llew")
piper = Dog("Piper", "Border Collie", matt)

print(piper.owner.name)
print(piper.name)


my_shape = Shape(20, 25)
my_shape.print_size()
my_shape.what_am_i()

a_square = Square(20, 20)
print(a_square.area())
print(a_square.print_size())
print(a_square.calculate_perimeter())
a_square.change_size(5)
print(a_square.width)
a_square.change_size(-5)
print(a_square.width)
a_square.what_am_i()



a_rectangle = Rectangle(20, 30)
print(a_rectangle.calculate_perimeter())
a_rectangle.what_am_i()


circle1 = Circle(4)
print(circle1.area())

triangle1 = Triangle(3, 4)
print(triangle1.area())

hexagon1 = Hexagon(20)
print(hexagon1.perimeter())


