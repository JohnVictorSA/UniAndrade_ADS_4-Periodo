from .jogador import Player

class Thief(Player):
    def __init__(self, nome):
        super().__init__(nome, vida=85, stamina=110)
        self.sorte = 25

    def atacar(self):
        print(f"{self._nome} realiza um ataque furtivo com chance crítica!")

    def defender(self, dano):
        self._vida -= dano
        print(f"{self._nome} tenta esquivar, mas recebe {dano} de dano.")