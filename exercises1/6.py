# That a function that allows you to validate  if a number is even or odd

number = int(input('Enter a number to validate: '))

def esPar(number):
    return number % 2 == 0


operation = esPar(number)

print(operation)

def esPar2(number):
    if number % 2 == 0:
        return f'Number {number} is even'
    else:
        return f'Number {number} is odd'
    
operation2 = esPar2(number)

print(operation2)