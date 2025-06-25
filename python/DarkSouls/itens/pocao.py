from .item import Item

class Potion(Item):
    def __init__(self, nome, cura):
        super().__init__(nome, tipo="pocao")
        self.cura = cura

    def usar(self, jogador):
        jogador._vida += self.cura
        print(f"{jogador._nome} recuperou {self.cura} de vida!")