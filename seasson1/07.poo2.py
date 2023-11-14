"""
Now, we let's create a 'super' class for cats
"""


class DomesticAnimals:
    def __init__(self, name, onomatopoeia) -> None:
        self.name = name
        self.onomatopoeia = onomatopoeia

    def greeting(self):
        print(
            f'Hi, I am {self.type} Sound: {self.onomatopoeia} Type: {self.type}')

# Our animal class by species


class Cats(DomesticAnimals):
    type = "cat"


class Dogs(DomesticAnimals):
    type = "dog"


class Parrot(DomesticAnimals):
    type = "parrot"


# Instantiate a new object
taro = Cats('Taro', 'Miau')
sky = Dogs('Sky', 'Guau')
roberto = Parrot('Roberto', 'Do you want cocoa')

# Execute the method
taro.greeting()
sky.greeting()
roberto.greeting()
