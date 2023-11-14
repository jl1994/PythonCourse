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


# num = 7
# while True:
#     try:
#         numUser = int(input('Insert a number from 1 to 10: '))
#     except:
#         numUser = 'string'
#         continue

#     if numUser == 'string':
#         print('Won! the number', numUser, 'is correct')
#     elif numUser < num:
#         print('More to the rigth')
#     elif numUser > num:
#         print('More to the left')
#     else:
#         print('Won! the number', numUser, 'is correct')
#         break

# Other Option

# import random

# numero_secreto = random.randint(1, 10)
# adivinanza = 0
# # print(numero_secreto)

# while adivinanza != numero_secreto:
#     # Capturo el numero po
#     adivinanza = int(input('Enter a number'))
#     if adivinanza < numero_secreto:
#         print("Numero demasiado bajo")
#     elif adivinanza > numero_secreto:
#         print('Numbero demasiado alto')
#     else:
#         print('Won')

# while adivinanza != numero_secreto:
#     adivinanza = int(input("Adivina el número: "))
#     if adivinanza < numero_secreto:
#         print("Demasiado bajo")
#     elif adivinanza > numero_secreto:
#         print("Demasiado alto")
#     else:
#         print("¡Adivinaste!")


# 03. Validación de entrada de usuario: Solicita al usuario que ingrese una contraseña y utiliza un bucle while para asegurarte
# de que la contraseña tenga al menos 8 caracteres.


# Loop to validate min characters

# password = input('Enter a password: ')
# length_password = 0

# while length_password < 8:
#     password = input('Enter a password: ')
#     length_password = len(password)
# print('Password complete!')

# password = input('Enter a password: ')

# while len(password) < 8:
#     password = input('Enter a password: ')

# print('Password complete!')


###################
#### Exercises ####
###################

# Calculadora de Suma: Crea una calculadora que sume números ingresados por el usuario hasta que este decida detenerse.

# Generador de secuencia Fibonacci: Crea un programa que genere la secuencia de Fibonacci hasta un número específico ingresado por el usuario.
# python

# Lista de tareas pendientes: Implementa una lista de tareas pendientes que el usuario puede agregar y eliminar elementos de la lista.

# Cuenta regresiva de lanzamiento de cohete: Simula una cuenta regresiva para el lanzamiento de un cohete espacial.

# Calculadora de interés compuesto: Crea una calculadora que determine cuánto dinero tendrás después de ciertos años con una tasa de interés compuesto.

# Simulación de juego de dados: Simula un juego de dados donde el jugador lanza dos dados y gana si obtiene un 7.

# Control de temperatura de un horno: Simula el control de temperatura de un horno. El programa ajusta la temperatura hasta que alcance un valor deseado.