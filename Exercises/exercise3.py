from pprint import pprint
sentence = "This is a common interview question"

# my solution
count_dictionary = {}
highest_count = 0
highest_letters = []

for letter in sentence:
    count_dictionary[letter] = count_dictionary.get(letter, 0) + 1


for letter in count_dictionary:
    if count_dictionary[letter] > highest_count:
        highest_count = count_dictionary[letter]

for letter in count_dictionary:
    if count_dictionary[letter] == highest_count:
        highest_letters.append(letter)

print(count_dictionary)
print(highest_count)
print(highest_letters)

# his solution
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

        pprint(char_frequency, width=1)

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)


print(char_frequency_sorted[1])
