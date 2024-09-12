class Parente:
    def __init__(self, id=0, nome="", pais=None, filhos=None, irmaos=None, conjuge=None):
        self.id = id
        self.nome = nome
        self.pais = pais if pais else []
        self.filhos = filhos if filhos else []
        self.irmaos = irmaos if irmaos else []
        self.conjuge = conjuge

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        return self

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        if pais is not None:
            self._pais = pais
        else:
            self._pais = []
        return self

    @property
    def filhos(self):
        return self._filhos

    @filhos.setter
    def filhos(self, filhos):
        if filhos is not None:
            self._filhos = filhos
        else:
            self._filhos = []
        return self

    @property
    def irmaos(self):
        return self._irmaos

    @irmaos.setter
    def irmaos(self, irmaos):
        if irmaos is not None:
            self._irmaos = irmaos
        else:
            self._irmaos = []
        return self

    @property
    def conjuge(self):
        return self._conjuge

    @conjuge.setter
    def conjuge(self, conjuge):
        self._conjuge = conjuge
        return self
