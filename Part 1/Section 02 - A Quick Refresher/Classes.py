class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive, please go again to 1st calss to understand the digits! ')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)


    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10,10)

print(r1.perimeter())

print(str(r1))

print(r1)

print(repr(r1))

r2 = Rectangle(10,200)

print(r2.area())

print(r1 == r2)

r3 = Rectangle(10, 20)

print(r3)

print(r3.width)

r1.width = 1000

print(r1.width)

r1 = Rectangle(1, 10)
r2 = Rectangle(2, 10)