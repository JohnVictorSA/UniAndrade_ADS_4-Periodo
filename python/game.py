import random
import time

class PersonagemGame:
    def __init__(self, nome, classe, nivel, vida, ataque):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.inventario = []

    def exibir_status(self):
        print(f"{self.nome} | Classe: {self.classe} | Nível: {self.nivel} | Vida: {self.vida} | Ataque: {self.ataque}")
        print(f"Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}\n")

    def atacar(self, outro):
        dano = random.randint(self.ataque - 2, self.ataque + 3)
        outro.vida -= dano
        print(f"{self.nome} atacou {outro.nome} causando {dano} de dano!")

    def usar_item(self):
        if "Poção de Cura" in self.inventario:
            self.vida += 20
            self.inventario.remove("Poção de Cura")
            print(f"{self.nome} usou uma Poção de Cura! (+20 de vida)")
        elif "Espada Extra" in self.inventario:
            self.ataque += 5
            self.inventario.remove("Espada Extra")
            print(f"{self.nome} usou uma Espada Extra! (+5 de ataque)")
        else:
            print(f"{self.nome} não tem itens utilizáveis.")

# Criando personagens
jogador1 = PersonagemGame("Drako", "Guerreiro", 10, 100, 15)
jogador2 = PersonagemGame("Mira", "Feiticeira", 9, 90, 13)

# Adicionando itens
jogador1.inventario = ["Poção de Cura", "Espada Extra"]
jogador2.inventario = ["Poção de Cura"]

# Exibindo início do jogo
print("🎮 BATALHA INICIADA 🎮\n")
jogador1.exibir_status()
jogador2.exibir_status()

# Loop do jogo
turno = 1
while jogador1.vida > 0 and jogador2.vida > 0:
    print(f"=== TURNO {turno} ===")

    # Jogador 1 ataca
    jogador1.atacar(jogador2)
    if jogador2.vida <= 30:
        jogador2.usar_item()

    time.sleep(1)

    if jogador2.vida <= 0:
        print(f"\n🏆 {jogador1.nome} venceu a batalha!")
        break

    # Jogador 2 ataca
    jogador2.atacar(jogador1)
    if jogador1.vida <= 30:
        jogador1.usar_item()

    time.sleep(1)

    if jogador1.vida <= 0:
        print(f"\n🏆 {jogador2.nome} venceu a batalha!")
        break

    print()
    jogador1.exibir_status()
    jogador2.exibir_status()
    turno += 1

print("\n👊 FIM DO JOGO 👊")
