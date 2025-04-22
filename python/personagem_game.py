class PersonagemGame:
    def __init__(self, nome, classe, nivel, vida):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.vida = vida
        self.inventario = []  # estrutura de dados opcional (lista)

    def exibir_status(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.vida}")
        print(f"Inventário: {self.inventario}")

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{item} foi adicionado ao inventário de {self.nome}.")

# Instanciando dois personagens diferentes
personagem1 = PersonagemGame("Arthus", "Guerreiro", 10, 100)
personagem2 = PersonagemGame("Luna", "Arqueira", 8, 85)

# Adicionando itens aos inventários
personagem1.adicionar_item("Espada de Fogo")
personagem1.adicionar_item("Escudo de Ferro")

personagem2.adicionar_item("Arco Elétrico")
personagem2.adicionar_item("Flechas Mágicas")

# Imprimindo os dados dos personagens
print("\n--- Personagem 1 ---")
personagem1.exibir_status()

print("\n--- Personagem 2 ---")
personagem2.exibir_status()
