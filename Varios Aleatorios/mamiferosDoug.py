class Mamiferos:
    def __init__(self, nome, especie, caracteristica):
        self.s_nome_mamifero = nome
        self.s_specie_mamifero = especie
        self.s_ambiente = caracteristica
        self.max_patas = 0

    def descobre_numero_patas(self):
        if self.s_ambiente == "voa":
            self.max_patas = 2
            return self.max_patas
        if self.s_ambiente == "nada":
            self.max_patas = 0
            return self.max_patas
        if self.s_ambiente == "terra":
            self.max_patas = 4
            return self.max_patas


cavalo = Mamiferos("Cavalo","cavalus equatorius", "terra")
print(cavalo.descobre_numero_patas())

morcego = Mamiferos("Morcego", "batman", "voa")
print(morcego.descobre_numero_patas())



class Humanos(Mamiferos):
    def __init__(self, nome, idade):
        #self.
        pass