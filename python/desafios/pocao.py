

""" FLUXO
- Player está vivo?
- usar poção (verde, roxa)
- tratar casos (energia)
- status
- Personagem:
    [Inventário] -> Item (arma, poção) # Associação/Agregação
    [Armadura] # Composição
"""

class Item: 
    def __init__(self, tipo:str, efeito:int):
        self.tipo = tipo
        self.efeito = efeito
        
class Inventario:
    def __init__(self):
        self.itens = [] #Agregação
        
    def adicionar_item(self, item: Item):
        if not item:
            print("Escolha um item para inserir")
    
        self.itens.append(item)
            
    def listar_itens(self):
        for item in self.itens:
            print(f"Itens {item.tipo}")
            
            
# class Armadura:
#       pass

            
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 60
        self.vivo = True
        self.inventario = Inventario() # Agregação 
        
    def usar_pocao(self, pocao):
        if (self.vivo == False):
            print(f"Personagem está MORTO, não é possível usar nenhuma poção.")
            return
        
        print(f"Personagem {self.nome} usou poção {pocao.tipo}")
        print(f"Saude antes da poção: {self.saude}")
        
        if (pocao.tipo == "Cura"):
            self.saude += pocao.potencia
            print(f"Cura concedida: {pocao.potencia}\nTotal de saúde: {self.saude}\n")
        
        elif (pocao.tipo == "Dano"):
            self.saude -= pocao.potencia
            if self.saude <= 0:
                self.vivo = False
                print(f"Personagem {self.nome} morreu ao tomar a poção.")
                return
            
            print(f"Dano aplicado: {pocao.potencia}\nTotal de saúde: {self.saude}\n")
            
class PocaoVerde:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        
class PocaoRoxa:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

p1 = Personagem("Pao")
pocaoNaipe = PocaoVerde("Cura", 20)
pocaoMorte = PocaoRoxa("Dano", 20)
inventario = Inventario()
faca = Item("Faca Tramontina", 120)
escudo = Item("Escudo do rei", 90)

inventario.adicionar_item(faca)
inventario.adicionar_item(escudo)

inventario.listar_itens()

# print(p1.__dict__)




# p1.usar_pocao(pocaoTop)
# p1.usar_pocao(pocaoPaia)
# p1.usar_pocao(pocaoPaia)
# p1.usar_pocao(pocaoPaia)
# p1.usar_pocao(pocaoPaia)
# p1.usar_pocao(pocaoTop)


