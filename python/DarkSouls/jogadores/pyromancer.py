from .jogador import Player

class Pyromancer(Player):
    def __init__(self, nome):
        super().__init__(nome, vida=90, stamina=100)
        self.fogo = 30

    def atacar(self):
        print(f"{self._nome} lança uma bola de fogo (Dano mágico: {self.fogo})!")

    def defender(self, dano):
        self._vida -= dano
        print(f"{self._nome} tenta se proteger com fogo. Dano recebido: {dano}")