class Enemy:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def atacar(self):
        print(f"{self.nome} ataca com {self.dano} de dano!")