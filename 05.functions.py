def myFunction():
    print('Inside my first function in python')
# myFunction()


# netlunaContainer = ['API Netluna', 2, 4]  # "/bin/sh start.sh"


# def createContainer(name, cpu, memory, entrypoint="/bin/sh start.sh"):
#     print('Name: ', name)
#     print('CPU: ', cpu)
#     print('Memory: ', memory)
#     print('Entrypoint: ', entrypoint)

# createContainer(*netlunaContainer)

# def createContainer2(*args, ):
#     print('Name: ', args[0])
#     print('CPU: ', args[1])
#     print('Memory: ', args[2])
#     print('Entrypoint: ', args[3])

# createContainer(*netlunaContainer)

# def createContainer2(*args, **kwargs):
#     print('Name: ', kwargs['name'])
#     print('CPU: ', kwargs['cpu'])
#     print('Memory: ', kwargs['memory'])
#     print('Entrypoint: ', kwargs['entrypoint'])

# Suponiendo que tienes un objeto netlunaContainer con los valores necesarios

# netlunaContainer = {  # Dictionary
#     'name': 'MiContenedor',
#     'cpu': 2,
#     'memory': '4GB',
#     'entrypoint': '/ruta/a/tu/entrada'
# }

# netlunaContainerList = ['MiContenedor', 2, 4, '/ruta/a/tu/entrada']  # List
# # netlunaContainerList2 = ('MiContenedor', 2, 4, '/ruta/a/tu/entrada')  # Tuple


# # createContainer2(**netlunaContainer)
# print(type(netlunaContainerList))
# # print(type(netlunaContainerList2))


# def createNameContainer(list):
#     i = ' '
#     for e in list:
#         i = i + str(e) + ' '
#     print(i)
#     return i

# returnDatos = createNameContainer(netlunaContainerList)

# print(returnDatos)

def welcome(name):
    return f'Welcome {name} to Netluna!'


welcomeUser = welcome('Johan')

print(welcomeUser)
