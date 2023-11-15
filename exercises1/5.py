def esMayor(edad):
    if edad < 18:
        return False
    else:
        return True


class aspirante():
    def __init__(self, edad) -> None:
        self.edad = edad
        pass


johan = aspirante(29)
jose = aspirante(17)

print(esMayor(jose.edad))
print(esMayor(johan.edad))
