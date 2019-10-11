def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fizz"
    return input


print(fizz_buzz(15))
print(fizz_buzz(12))
print(fizz_buzz(10))
