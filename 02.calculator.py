# We captured our first number
num1 = input('Enter first number: ')

# We validated if the data entered is an integer
try:
    num1 = int(num1)
except:
    num1 = 'string'

if num1 == 'string':
    print('Invalid number, try again only with numbers')
    exit()  # We exit the program if it is not an integer

# We captured our second number
num2 = input('Enter second number: ')

# We validated if the data entered is an integer
try:
    num2 = int(num2)
except:
    num2 = 'string'

if num2 == 'string':
    print('Invalid number, try again only with numbers')
    exit()  # We exit the program if it is not an integer

# We capture the operation to calculate the result

simbol = input('What operation do you want? [ + , - , * , / ]: ')

if simbol == '+':
    print('[ Addition ]', num1, '+', num2, ' = ', num1+num2)

elif simbol == '-':
    print('[ Subtraction ]', num1, '-', num2, ' = ', num1-num2)

elif simbol == '*':
    print('[ Multiplication ]', num1, '*', num2, ' = ', num1*num2)

elif simbol == '/':
    print('[ Division ]', num1, '/', num2, ' = ', num1/num2)

else:
    print('Invalid Operation')
