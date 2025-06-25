from .inimigo import Enemy

class Boss(Enemy):
    def ataque_especial(self):
        print(f"{self.nome} usa um ataque especial devastador!")