from .jogador import Player

class Knight(Player):
    def __init__(self, nome):
        super().__init__(nome, vida=120, stamina=80)
        self.armadura = 20

    def atacar(self):
        print(f"{self._nome} usa espada larga para um golpe poderoso!")

    def defender(self, dano):
        real_dano = max(dano - self.armadura, 0)
        self._vida -= real_dano
        print(f"{self._nome} defende com armadura pesada! Dano recebido: {real_dano}")