def isComplete(Graph):
    """
    Determina si un grafo no dirigido es completo.
    Entrada:
        Graph: Array de listas enlazadas (listas de adyacencia)
    Salida:
        True si el grafo es completo, False en caso contrario
    """
    n = len(Graph)
    if n == 0:
        return False

    for i in range(n):
        count = 0
        current = Graph[i].head.nextNode

        # Contar cantidad de vecinos (adyacencias)
        while current is not None:
            count += 1
            current = current.nextNode

        # En un grafo completo, cada vértice debe estar conectado con todos los demás
        if count != n - 1:
            return False

    return True

from linkedlist import LinkedList, add
from array import Array
from Ejercicio1 import createGraph
from Ejercicio4 import isComplete

# Grafo 1 — Completo (A, B, C con todas las conexiones)
vertices1 = LinkedList()
add(vertices1, "A")
add(vertices1, "B")
add(vertices1, "C")

edges1 = LinkedList()
add(edges1, "A"); add(edges1, "B")
add(edges1, "A"); add(edges1, "C")
add(edges1, "B"); add(edges1, "C")

G1 = createGraph(vertices1, edges1)
print("Grafo 1 es completo:", isComplete(G1))  # True

# Grafo 2 — No completo (A-B, B-C, pero falta A-C)
vertices2 = LinkedList()
add(vertices2, "A")
add(vertices2, "B")
add(vertices2, "C")

edges2 = LinkedList()
add(edges2, "A"); add(edges2, "B")
add(edges2, "B"); add(edges2, "C")

G2 = createGraph(vertices2, edges2)
print("Grafo 2 es completo:", isComplete(G2))  # False
