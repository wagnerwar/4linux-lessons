#/usr/bin/python


# Isto so para python 3
"""
class Minha(object):
    pass

objeto = Minha()

print(objeto)
"""

class servidores(object):
    memoria = None # Variavel publica
    _ram = None # Variavel protegida
    __ram = None # Variavel privada
    cpu = None

    def alterarMemoria(self, memoria):
        self.memoria = memoria
    
    # Metodo construtor
    def __init__(self, memoria=None, cpu=None):
        self.memoria = memoria
        self.cpu = cpu

    """
    Cada classe so pode ter apenas um metodo construtor
    
    """
    # Metodo executado quando 
    def __str__(self):
        return (str(self.memoria) + "  "+ str(self.cpu))
     
    def __int__(self):
        return 100

class cloud(servidores):
    def alterarMemoria(self, memoria=None):
        self.memoria = memoria
        print("Executado metodo da classe-filha")

# MAIN
objeto = servidores(5, 2)
clonado = cloud(6, 2)

print(str(objeto.cpu) + " " + str(objeto.memoria))


objeto.alterarMemoria(3)

print(objeto.memoria)


# Metodo __str__ sera executado
print(objeto.__str__())

# Metodo __int__ sera executado
print(int(objeto))

del(objeto) # Liberacao de memoria


print(clonado)
clonado.alterarMemoria(7)
