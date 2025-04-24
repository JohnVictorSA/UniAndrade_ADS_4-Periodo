import time
import random

class Lutador:
    def __init__(self, nome, estilo, vida, ataques):
        self.nome = nome
        self.estilo = estilo
        self.vida = vida
        self.ataques = ataques  # dicionário: {"Ataque": dano}
    
    def mostrar_status(self):
        barra = "█" * (self.vida // 5) + "-" * ((100 - self.vida) // 5)
        print(f"{self.nome} [{self.estilo}] | VIDA: {self.vida}/100")
        print(f"[{barra}]")
        print()

    def atacar(self, outro):
        print(f"\nEscolha um ataque de {self.nome}:")
        for i, (nome, dano) in enumerate(self.ataques.items(), 1):
            print(f"{i}. {nome} (dano: {dano})")

        while True:
            try:
                escolha = int(input("→ Ataque: "))
                if 1 <= escolha <= len(self.ataques):
                    break
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Digite um número válido.")

        nome_ataque = list(self.ataques.keys())[escolha - 1]
        dano = self.ataques[nome_ataque]

        print(f"\n{self.nome} grita: \"{nome_ataque.upper()}!\" 💥")
        time.sleep(1)
        print(f"{outro.nome} recebe {dano} de dano!\n")
        outro.vida -= dano
        if outro.vida < 0:
            outro.vida = 0

# Criando os lutadores
ryu = Lutador("Ryu", "Karate", 100, {
    "Hadouken": 25,
    "Shoryuken": 30,
    "Chute Giratório": 20
})

ken = Lutador("Ken", "Karate Flamejante", 100, {
    "Hadouken Flamejante": 27,
    "Shoryuken Explosivo": 33,
    "Soco Cruzado": 18
})

# Início da luta
print("\n🎮 STREET FIGHTER - BATALHA INICIADA 🎮\n")
time.sleep(1)
ryu.mostrar_status()
ken.mostrar_status()

turno = 1
while ryu.vida > 0 and ken.vida > 0:
    print(f"\n========== ROUND {turno} ==========\n")
    if turno % 2 == 1:
        ryu.atacar(ken)
    else:
        ken.atacar(ryu)

    time.sleep(1)
    ryu.mostrar_status()
    ken.mostrar_status()
    turno += 1

# Resultado final
print("\n🏁 FIM DA LUTA 🏁")
if ryu.vida > 0:
    print("🏆 RYU VENCEU O COMBATE!")
else:
    print("🏆 KEN VENCEU O COMBATE!")

print("\n👊 Obrigado por jogar Street Fighter (terminal edition) 👊\n")
