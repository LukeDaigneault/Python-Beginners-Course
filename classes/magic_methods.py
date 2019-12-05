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

    # decorator
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# factory method
point = Point.zero()

print(point)

point.draw()
