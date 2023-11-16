# Write a function that allows us to know vowels a word has

string = input('Enter a string: ')
string_lower = string.lower()

print(string_lower)
vowels = ['a', 'e', 'i', 'o', 'u']
counter = 0
counter2 = 0

for i in vowels:
    for j in string_lower:
        if i == j:
            counter = counter + 1

for x in string_lower:
    counter2 += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

print(f'The word {string} has {counter} vowels')

print(counter2)
