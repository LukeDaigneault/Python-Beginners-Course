class Point:
    # class attribute
    default_colour = "red"

    def __init__(self, x, y):
        # instance level attribute
        self.x = x
        self.y = y

    # magic method
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # decorator factory pattern
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(10, 20)
other = Point.zero()

print(point < other)
