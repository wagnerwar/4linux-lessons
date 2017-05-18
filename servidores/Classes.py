class servidor(object):
    _memoria = None # Variavel publica
    _nome = None
    _cpu = None
    _so = None

    def definirAtributos(self, mem, nome, cpu, so):
        self._memoria = mem
        self._nome = nome
        self._cpu = cpu
        self._so = so
    
    def getCpu(self):
        return self._cpu
    
    def getName(self):
        return self._nome

    def getMemoria(self):
        return self._memoria
    
    def getSo(self):
        return self._so


class fisico(servidor):
    id_servidor = None
    localidade = None
    
    def getId(self):
        return self.id_servidor
    
    def getLocalidade(self):
        return self.localidade

class cloud(servidor):
    UUID = None
    ambiente = None

    def getId(self):
        return self.UUID

    def getAmbiente(self):
        return self.ambiente
