# Write a funcion that finds a smallest number in a list

numberslist = [1, 4, 2, 1, 5, 3, 1, -13, -42, -12, 0]

# Cycle 1 i = 1

# print(numberslist)
firstnumber = numberslist[0]

for i in numberslist:
    if i < firstnumber:
        firstnumber = i

print(firstnumber)
