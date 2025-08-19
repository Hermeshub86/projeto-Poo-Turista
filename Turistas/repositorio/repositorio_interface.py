from abc import ABC, abstractmethod
from modelo.turista import Turista

class RepositorioTurista(ABC):
    @abstractmethod
    def salvar(self, turista: Turista):
        pass

    @abstractmethod
    def listar(self):
        pass
