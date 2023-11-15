# Enter name and lastname and print it backwards

name = input('Enter name: ')
lastname = input('Enter lastname: ')

fullname = name + " " + lastname
backwardsfullname = fullname[::-1]

print(f'{backwardsfullname}')
print(f'{fullname[::-1]}')
