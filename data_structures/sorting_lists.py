numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

new_numbers = sorted(numbers, reverse=True)
print(new_numbers)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
