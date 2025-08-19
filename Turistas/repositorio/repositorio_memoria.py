from repositorio.repositorio_interface import RepositorioTurista

class RepositorioTuristaMemoria(RepositorioTurista):
    def __init__(self):
        self._turistas = []

    def salvar(self, turista):
        if turista.validar():
            self._turistas.append(turista)

    def listar(self):
        return self._turistas
