# Programa de la pregunta 1.b.ii

from abc import ABC, abstractmethod


# CLASES
# Clase Grafo con un método agregar_arista
class Grafo:
    def __init__(self):
        self.adyacencias = {}

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 not in self.adyacencias:
            self.adyacencias[nodo1] = []
        if nodo2 not in self.adyacencias:
            self.adyacencias[nodo2] = []
        self.adyacencias[nodo1].append(nodo2)
        self.adyacencias[nodo2].append(nodo1)

# Clase abstracta Busqueda con un método abstracto buscar
class Busqueda(ABC):
    def __init__(self, grafo):
        self.grafo = grafo

    @abstractmethod
    def buscar(self, D, H):
        pass

# Clases DFS y BFS que heredan de Busqueda e implementan el método buscar
class DFS(Busqueda):
    def buscar(self, D, H):
        visitados = set()
        pila = [D]
        explorados = 0

        while pila:
            nodo = pila.pop()
            if nodo == H:
                return explorados
            if nodo not in visitados:
                visitados.add(nodo)
                explorados += 1
                pila.extend(self.grafo.adyacencias.get(nodo, []))
        return -1

class BFS(Busqueda):
    def buscar(self, D, H):
        visitados = set()
        explorados = 0
        cola = [D]

        while cola:
            nodo = cola.pop(0)
            if nodo == H:
                return explorados
            if nodo not in visitados:
                visitados.add(nodo)
                explorados += 1
                cola.extend(self.grafo.adyacencias.get(nodo, []))
        return -1
