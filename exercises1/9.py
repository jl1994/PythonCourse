# Write a function that receives name and lastname and save them to a file

def addNameLastNAme(file, name, lastname):
    with open('users.txt', 'a') as file:
        # file = open(file, "w")
        print(f'Add {name} {lastname} in file {file}')
        file.write(f'\n{name} {lastname}\n')
        file.close()


while True:
    addNameLastNAme("./users.txt", "Johan", "Luna")
