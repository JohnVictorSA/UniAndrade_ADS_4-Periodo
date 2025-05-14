class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 10
        self.vivo = True
        
    def usar_pocao(self, pocao):
        self.saude += pocao.potencia
        print(f"Personagem {self.nome} usou poção {pocao.tipo}")
        print(f"Dano {pocao.potencia} saude {self.saude}")
        
        
class PocaoVerde:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        
# Crie uma nova PocaoRoxa

# Instanciar Jogador
p1 = Personagem("Chaves")
pocao1 = PocaoVerde("Cura", 15)
p1.usar_pocao(pocao1)

del p1
print(pocao1)

# Se o personagem ainda está vivo, decremente ao usar poção veneno
    # Pode usar poção veneno
    # Pode usar poção saúde
# Se a saúde for <= 0 
    # personagem vivo=False)
    # informe personagem está morto, foi de "arrasta"
    # cancele a possibilidade de incrementar ou decrementar saúde
    

