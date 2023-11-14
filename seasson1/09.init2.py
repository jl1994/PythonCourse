class Animal:
    def __init__(self, name, onomatopeia):
        self.name = name
        self.onomatopeia = onomatopeia

    def greetings(self):
        print(f'Hi!, I am a {self.name} {self.onomatopeia}')


class Cat(Animal):
    type = "Cat"

    def __init__(self, name, onomatopeia):
        Animal.__init__(self, name, onomatopeia)
        print("Aditional code Cat Class")


class Dog(Animal):
    type = "Dog"

    def __init__(self, name, onomatopeia):
        super().__init__(name, onomatopeia)
        print("Aditional code Dog Class")


taro = Cat('Taro', 'Miau')
sky = Dog('Sky', 'Wuau')

taro.greetings()
sky.greetings()
