try:
    with open("app.py") as file, open("another.txt") as target:
        print("File opened.")

    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
