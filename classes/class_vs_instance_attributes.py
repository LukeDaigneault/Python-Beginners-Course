class Point:
    # class attribute
    default_colour = "red"

    def __init__(self, x, y):
        # instance level attribute
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# override class attribute
Point.default_colour = "Yellow"


point = Point(1, 2)
print(point.default_colour)
print(Point.default_colour)

point.draw()

another = Point(3, 4)
another.draw()

print(another.default_colour)
