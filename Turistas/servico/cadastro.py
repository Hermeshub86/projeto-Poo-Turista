class CadastroTurista:
    def __init__(self, repositorio):
        self._repositorio = repositorio

    def cadastrar(self, turista):
        self._repositorio.salvar(turista)
