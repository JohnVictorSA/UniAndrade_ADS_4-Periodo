from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, nome, vida, stamina):
        self._nome = nome
        self._vida = vida
        self._stamina = stamina

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self, dano):
        pass

    def status(self):
        print(f"{self._nome} | Vida: {self._vida} | Stamina: {self._stamina}")