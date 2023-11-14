# Gestor de instalación de modulos
# Import module as mpets
from module import gretings, pets  # -> New form to import modules
from camelcase import CamelCase

# Then we create an instance of camelcase

c = CamelCase()

# I create an string

name = 'johan ederlien luna bermeo'
nameCamelCase = c.hump(name)

# print(pets)
# gretings("Johan Luna")

print(nameCamelCase)
