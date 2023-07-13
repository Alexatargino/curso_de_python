class Exemplo():
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
    def apresentar (self):
        print("Olá eu tenho",self.altura, "e peso", self.peso,"Kg.")

mãe = Exemplo("Altura", 1.78)
mãe.apresentar()
mãe = Exemplo("Peso", 80)

print(mãe.altura, mãe.peso)


