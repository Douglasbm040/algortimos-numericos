from abc import ABC, abstractmethod

class MetodoStrategy(ABC):
    @abstractmethod
    def executar(self, X:list, y:list): pass