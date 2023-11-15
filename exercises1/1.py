# Multiply two numbers without multiplication symbol

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
counter = 0

# var1 * var2
# 2 * 3

# 0 + 2 - Cycle 1
# 2 + 2 - Cycle 2
# 4 + 2 - Cycle 3

for i in range(0, num2):
    # print(1)  # Cycle debug
    counter = counter + num1

print(counter)
