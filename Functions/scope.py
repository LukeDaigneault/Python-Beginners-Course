message = "a"


def greet(name):
    # bad practise
    global message
    message = "b"


greet("Test")
print(message)
