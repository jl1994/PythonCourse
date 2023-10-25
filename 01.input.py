
# Array containing a list of options and we are going to try to guess what is on this list
data = int(input('Enter a number: '))

# Let's create the list of numbers for the game
numbers = [1, 3, 5, 6, 8, 9]

# Conditional to validate if the number exists
if numbers.count(data) >= 1:
    print('The number: ',data, 'exists')
else:
    print('The number: ',data, ' not exists')
