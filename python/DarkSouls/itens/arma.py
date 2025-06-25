from .item import Item

class Weapon(Item):
    def __init__(self, nome, dano, resistencia):
        super().__init__(nome, tipo="arma")
        self.dano = dano
        self.resistencia = resistencia

    def usar(self):
        print(f"{self.nome} usada. Dano: {self.dano}")