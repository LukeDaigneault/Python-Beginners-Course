from collections import namedtuple
# these are immutable
Point = namedtuple("Point", ["x", "y"])


p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

print(p1 == p2)
print(p1.x)

print(id(p1))
print(id(p2))
