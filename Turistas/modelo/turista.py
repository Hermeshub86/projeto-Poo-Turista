from datetime import datetime

#criar funcao Turista
class Turista:
    def __init__(self, nome, estado_origem, data_chegada, transporte):
        self._nome = nome
        self._estado_origem = estado_origem
        self._data_chegada = data_chegada
        self._transporte = transporte

    @property
    def nome(self):
        return self._nome

    @property
    def estado_origem(self):
        return self._estado_origem

    @property
    def data_chegada(self):
        return self._data_chegada

    @property
    def transporte(self):
        return self._transporte

    def validar(self):
        return isinstance(self._data_chegada, datetime) and len(self._nome.strip()) > 0
