values = []

for x in range(5):
    values.append(x * 2)

values = [x * 2 for x in range(5)]

values = {x * 2 for x in range(5)}

print(values)

# use this to populate dictionaries.
values = {x: x * 2 for x in range(5)}
print(values)
