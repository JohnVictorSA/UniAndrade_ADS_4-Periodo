from .inimigo import Enemy

class Undead(Enemy):
    def __init__(self, nome, dano, podridao, velocidade):
        super().__init__(nome, dano)
        self.podridao = podridao
        self.velocidade = velocidade

    def morder(self):
        print(f"{self.nome} morde com podridão {self.podridao}!")