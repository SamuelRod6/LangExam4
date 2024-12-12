# Programa de la pregunta 1.b.i

from abc import ABC, abstractmethod

# CLASES
# Clase abstracta Secuencia con un método abstracto remover
class Secuencia(ABC):
    def __init__(self):
        self.elementos = []
        
    def agregar(self, elemento):
        self.elementos.append(elemento)

    @abstractmethod
    def remover(self):
        pass

    def vacio(self):
        return len(self.elementos) == 0

# Subclases Pila y Cola que heredan de Secuencia
class Pila(Secuencia):
    def remover(self):
        if self.vacio():
            raise IndexError("La pila está vacía")
        return self.elementos.pop()


class Cola(Secuencia):
    def remover(self):
        if self.vacio():
            raise IndexError("La cola está vacía")
        return self.elementos.pop(0)
    