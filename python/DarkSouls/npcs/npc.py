class NPC:
    def __init__(self, dialogo, amizade):
        self.dialogo = dialogo
        self.amizade = amizade

    def falar(self):
        print(f"NPC diz: '{self.dialogo}' (nível de amizade: {self.amizade})")