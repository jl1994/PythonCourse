# Concept
# i = 0
# while i <= 5:
#     print(i)
#     i = i + 1

# Exercises

# 1. Contador Regresivo: Crea un programa que cuente regresivamente desde 10 hasta 1, imprimiendo cada número en la pantalla.

# i = 10
# while i > 0:
#     print(i)
#     # i = i - 1 # Code refactor
#     i -= 1

# # Other Option
# contador = 10
# while contador >= 1:
#     print(contador)
#     contador -= 1

# Adivina el número: Desarrolla un juego donde el usuario tiene que adivinar un número secreto. El bucle se ejecuta hasta que el usuario adivina correctamente.


num = 7

while True:
    try:
        numUser = int(input('Insert a number from 1 to 10: '))
    except:
        numUser = 'string'
        continue

    if numUser == 'string':
        print('Won! the number', numUser, 'is correct')
    elif numUser < num:
        print('More to the rigth')
    elif numUser > num:
        print('More to the left')
    else:
        print('Won! the number', numUser, 'is correct')
        break

# Other Option

import random

numero_secreto = random.randint(1, 100)
adivinanza = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número: "))
    if adivinanza < numero_secreto:
        print("Demasiado bajo")
    elif adivinanza > numero_secreto:
        print("Demasiado alto")
    else:
        print("¡Adivinaste!")
        
        
Validación de entrada de usuario: Solicita al usuario que ingrese una contraseña y utiliza un bucle while para asegurarte de que la contraseña tenga al menos 8 caracteres.
