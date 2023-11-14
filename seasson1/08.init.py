# class Homework:
#     def __init__(self, descripcion):
#         self.descripcion = descripcion
#         self.subtasks = []

#     def add_subtask(self, subtask):
#         if subtask != "1.4 - Read a book":
#             self.subtasks.append(subtask)

# task1 = Homework("1. Learn English")
# task1.add_subtask("1.1 - Practice with Duolingo")
# task1.add_subtask("1.2 - Listen to a song")
# task1.add_subtask("1.3 - Talk in free4talk")
# task1.add_subtask("1.4 - Read a book")

# print(task1.descripcion)
# print(task1.subtasks)

# class Person:
#     def __init__(self, name, age, sex) -> None:
#         self.name = name
#         self.age = age
#         self.sex = sex
#         pass

# # We create an instance of the class


# person1 = Person('Johan', 29, 'Man')
# person2 = Person('Fernanda', 28, 'Women')

# print(person1.name)
# print(person2.name)


# class Car:
#     def __init__(self, company, model, price, year, color="white") -> None:
#         self.company = company
#         self.model = model
#         self.price = price
#         self.year = year
#         self.color = color
#         pass


# car1 = Car("Chevrolet", "Onix Turbo", 56000000, 2023)
# car2 = Car("Chevrolet", "Onix Turbo", 46000000, 2021)

# print(car1.price, car2.price)
# print(car1.color, car2.color)

# class MainNinja():
#     # These are default attributes
#     hp = 10
#     endurance = 50
#     xp = 1
#     lives = 3
#     # This is a method

#     def GameOver(self):
#         print(f'Game Over')
#         return True


# hero_ninja = MainNinja()
# enemy_ninja = MainNinja()


# print(f'{hero_ninja.endurance} {enemy_ninja.endurance}')
# enemy_ninja.GameOver()
