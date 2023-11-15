# Write a function that returns the volume of a sphere time its radio

radio = int(input("Enter a radio: "))
pi = 3.14


def volume(radio):
    print((4/3)*pi*radio**3)


volume(10)
