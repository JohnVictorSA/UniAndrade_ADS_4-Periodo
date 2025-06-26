# game.py - Jogo interativo com teclado baseado em Dark Souls
from jogadores.knight import Knight
from jogadores.thief import Thief
from jogadores.pyromancer import Pyromancer
from inimigos.chefe import Boss
from inimigos.morto_vivo import Undead
from itens.arma import Weapon
from itens.pocao import Potion
from npcs.ferreiro import Ferreiro
import random
import time

def print_lento(texto, delay=0.03):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def escolher_personagem():
    print("\n🛡️ Escolha seu personagem:")
    print("1 - Knight (Alta defesa e vida)")
    print("2 - Thief (Ágil e furtivo)")
    print("3 - Pyromancer (Ataques mágicos)")
    escolha = input("-> ")
    if escolha == "1":
        return Knight("Artorias")
    elif escolha == "2":
        return Thief("Lautrec")
    elif escolha == "3":
        return Pyromancer("Quelana")
    else:
        print("Opção inválida. Cavaleiro escolhido por padrão.")
        return Knight("Artorias")

def batalha(jogador, inimigo):
    print_lento(f"\n⚔️ Um {inimigo.nome} aparece no caminho!")
    while jogador._vida > 0 and inimigo.dano > 0:
        print("\n📜 Escolha sua ação:")
        print("1 - Atacar")
        print("2 - Defender")
        acao = input("-> ")

        if acao == "1":
            jogador.atacar()
            print(f"{inimigo.nome} revida!")
            jogador.defender(random.randint(inimigo.dano - 3, inimigo.dano + 3))
        elif acao == "2":
            print(f"{jogador._nome} se defende com estratégia!")
            jogador.defender(random.randint((inimigo.dano // 2) - 2, (inimigo.dano // 2) + 2))
        else:
            print("Ação inválida! Você perde o turno...")
            jogador.defender(inimigo.dano)

        jogador.status()
        if jogador._vida <= 0:
            print("💀 Você morreu...")
            return

    print_lento(f"\n🏆 Você derrotou {inimigo.nome}!")

def loja(ferreiro, jogador):
    print("\n🛠️ Você encontra um ferreiro misterioso...")
    ferreiro.falar()
    ferreiro.vender_item()
    print("O ferreiro oferece uma poção por sua bravura!")
    usar = input("Deseja usar a poção agora? (s/n): ")
    if usar.lower() == 's':
        pocao = Potion("Poção do Ferreiro", cura=30)
        pocao.usar(jogador)
        print("Você sente sua energia restaurada!")
    else:
        print("Você decide guardar sua força para depois.")

def main():
    print("\n==============================")
    print("        DARK SOULS")
    print("==============================")
    jogador = escolher_personagem()
    print_lento(f"\nBem-vindo ao mundo sombrio, {jogador._nome}! Prepare-se para a jornada...\n")

    espada = Weapon("Espada Longa", dano=25, resistencia=100)
    espada.usar()

    inimigos = [
        Undead("Zumbi Podre", 10, podridao=4, velocidade=2),
        Boss("Ornstein", 30)
    ]

    ferreiro = Ferreiro("Bem-vindo, guerreiro.", amizade=5, inventario=["poção"], metal="aço")

    for inimigo in inimigos:
        batalha(jogador, inimigo)
        if jogador._vida <= 0:
            return
        loja(ferreiro, jogador)

    print_lento("\n🎉 Parabéns, você sobreviveu às trevas e derrotou todos os inimigos!")

if __name__ == "__main__":
    main()
