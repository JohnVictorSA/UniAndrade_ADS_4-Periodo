from .npc import NPC

class Ferreiro(NPC):
    def __init__(self, dialogo, amizade, inventario, metal):
        super().__init__(dialogo, amizade)
        self.inventario = inventario
        self.metal = metal

    def vender_item(self):
        print(f"O ferreiro vende itens de {self.metal}. Inventário: {', '.join(self.inventario)}")