from jogador import Jogador

class Cavaleiro(Jogador):  #Herança
    def __init__ (self, nome:str, dano:int):
        super().__init__(nome, dano)

        # self.__saude = 100  #Encapsulamento
    
    @property  #Decorador retorna apenas com propriedade
    def saude(self):
        return self.__saude

    @saude.setter  #Decorador retorna apenas com propriedade
    def saude(self, valor):
        self.saude += max(0, valor)

    def atacar(self):
        print("Atacar Polimorfico")
        print(f"{self.nome} atacou!")

    def defender(self):
        print("Defender Polimorfico")
        print(f"{self.nome} defendeu!")

if __name__ == '__main__':
    cavaleiro = Cavaleiro("Rei Artur", 80)
    cavaleiro.atacar()



