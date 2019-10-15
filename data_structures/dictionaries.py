point = {"x": 1, "y": 2}

point = dict(x=1, y=2)

point["x"] = 10
point["z"] = 20

print(point)

print(point["x"])

if "a" in point:
    print("a")

print(point.get("a", 0))

del point["x"]

print(point)

for key in point:
    print(key, point[key])


for key, value in point.items():
    print(key, value)

# return tuples from dictionary
print(point.items())
