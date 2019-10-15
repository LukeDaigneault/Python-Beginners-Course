numbers = [1, 1, 2, 3, 4]

first = set(numbers)

second = {1, 6}
second.add(5)
second.remove(5)

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")

len(second)
