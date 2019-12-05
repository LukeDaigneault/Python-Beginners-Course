from sys import getsizeof

values = [x * 2 for x in range(1000)]
print("list:", getsizeof(values))

for x in values:
    print(x)

# generator object better for memeory
values = (x * 2 for x in range(10000))
print("gen:", getsizeof(values))
