# from itens import arma, armadura, pocao
# print(arma.Arma("Espada").usar())
# from itens import *
from itens import Pocao, Arma, Armadura

def main():
    pocaoKilla = Pocao("Cura 1000%")
    pocaoKilla.usar()

    faca = Arma("Katana")
    faca.usar()

    escudaoBrabo = Armadura("Peito de aço ativado")
    escudaoBrabo.usar()

if __name__ == "__main__":
    main()