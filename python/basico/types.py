class A:
    ...  # Ellipsis = código omitido

class B:
    ...

class C(A, B):
    ...


# Type Annotations
idade: int = 32
salario: float = 35000.50 
nome: str = "Julius"
casado: bool = True

dados: dict = {"nome": nome, "salario": salario, "idade": idade}
array: list = [2, 5, "ju", 25, 25, 25]
tupla: tuple = (2, 5, 25, 25)
unico: set = {2, 5, "ju", 25, 25, 25}

# Prints e testes
print(unico)               # set elimina duplicatas
print(nome.upper())        # Método builtin -> JULIUS
print(vars(C))             # Imprime atributos da classe C (herança)
# help(C)                  # Mostra informações da classe no console

# Mudando valores
nome: str = "Ana Paula"
eh_casado: bool = True

# Instanciando classe
pessoa: A = A()            # Tipo personalizado

# Atributo dinâmico na classe A
A.cargo = "diretor"

# Verificando os atributos da classe A
print(A.__dict__)          # Mostra atributos da classe
