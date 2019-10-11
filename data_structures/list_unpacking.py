numbers = [1, 2, 3, 4, 4, 4, 4]

first, second, *other, last = numbers
print(first, last)
print(other)
first = numbers[0]
second = numbers[1]
third = numbers[2]


def multiply(*numbers):
    print(numbers)


multiply(1, 2, 3)
