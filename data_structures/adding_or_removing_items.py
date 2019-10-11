letters = ["a", "b", "c"]

# add
letters.append("d")
letters.insert(0, "_")

print(letters)

# remove
letters.pop()
letters.pop(0)

letters.remove("b")
del letters[0:2]

letters.clear
print(letters)
