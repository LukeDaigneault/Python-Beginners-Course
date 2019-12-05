def calculate_xfactore(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactore(-1)
except ValueError as error:
    print(error)
