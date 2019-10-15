numbers = [1, 2, 3]
print(numbers)
# unpacking operator example
print(*numbers)

values = list(range(5))
print(values)

values = [*range(5), *"Hello World"]
print(values)

first = [1, 2]
second = [3, 4]

values = [*first, *second]

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}

print(combined)
