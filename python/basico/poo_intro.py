class Player:
    host = "localhost:8080"  # Atributo de classe (global)

    # Inicializador do objeto
    def __init__(self, nome, arma):
        self.nome = nome   # Atributo de instância
        self.arma = arma   # Atributo de instância


# Criando os objetos
kratos = Player("Kratos", "Lâminas do Caos")
hades = Player("Hades", "Stygius")

# Impressão dos atributos
print(kratos.nome, kratos.arma)
print(hades.nome, hades.host)  # host é atributo da classe
