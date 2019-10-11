total = 0

for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        total += 1
else:
    print(f"We have {total} even numbers")
