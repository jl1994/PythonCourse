# Write a function that allows to user enter a infinity numbers until him enter the word 'stop', then add all the numbers

def numbers_luna():  # Function name
    numbers = []  # Empty list to save the numbers.
    total = 0

    while True:  # Infinite loop with True
        # Prompted the user to enter a random number
        user_input = input('Enter a number: ')
        # Conditional to validate it what the user entered is and string equal to 'stop'
        if user_input == 'stop':
            break
        else:
            try:  # Use this expression to capture and handle exceptions.
                number = float(user_input)  # Convert string to float
                numbers.append(number)  # Add elements to list
            except ValueError:
                print('Value error')
                # exit() # Exit program (Optional)
    # We can sum the numbers with a for cycle
    for i in numbers:
        total += i
    # total = sum(numbers)  # The sum of the elements
    return total  # Return sum


# It calls a function named numbers_luna and assigns the result of the function
result = numbers_luna()

print(f'The sum of the elements of the array is: {result}')  # Print result
