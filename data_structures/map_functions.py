items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


prices = list(map(lambda item: item[1], items))
[item[1] for item in items]

print(list(filter(lambda item: item[1] >= 10, items)))
