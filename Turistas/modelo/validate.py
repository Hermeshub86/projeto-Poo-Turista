from abc import ABC, abstractmethod

class Validate(ABC):
    @abstractmethod
    def validar(self):
        pass
