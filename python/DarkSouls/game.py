from jogadores.knight import Knight
from jogadores.thief import Thief
from jogadores.pyromancer import Pyromancer
from inimigos.chefe import Boss
from inimigos.morto_vivo import Undead
from itens.arma import Weapon
from itens.pocao import Potion

def menu():
    print("\n-- Dark Souls RPG --")
    artorias = Knight("Artorias")
    lautrec = Thief("Lautrec")
    quelana = Pyromancer("Quelana")
    boss = Boss("Ornstein", 30)
    zumbi = Undead("Hollow", 10, podridao=5, velocidade=3)
    espada = Weapon("Espada Longa", dano=25, resistencia=100)
    pocao = Potion("Poção de Cura", cura=20)

    for jogador in [artorias, lautrec, quelana]:
        jogador.status()
        jogador.atacar()
        jogador.defender(dano=25)
        jogador.status()
        print("-" * 30)

    espada.usar()
    pocao.usar(artorias)
    zumbi.morder()

if __name__ == "__main__":
    menu()