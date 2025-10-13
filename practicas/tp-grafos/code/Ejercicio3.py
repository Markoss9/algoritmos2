from linkedlist import LinkedList, add
from array import Array
from Ejercicio1 import createGraph
from Ejercicio2 import isConnected

def isConnected(Graph):
    """
    Determina si el grafo es conexo.
    Entrada:
        Graph: Array de listas de adyacencia
    Salida:
        True si el grafo es conexo, False en caso contrario
    """
    n = len(Graph)
    if n == 0:
        return False

    visited = [False] * n

    # --- Función interna recursiva DFS ---
    def dfs(index):
        visited[index] = True
        node = Graph[index].head.nextNode
        while node is not None:
            # buscar índice del vecino
            neighbor_index = None
            for j in range(n):
                if Graph[j].head.value == node.value:
                    neighbor_index = j
                    break
            # seguir recorriendo
            if neighbor_index is not None and not visited[neighbor_index]:
                dfs(neighbor_index)
            node = node.nextNode

    # 1️⃣ Comenzar DFS desde el primer vértice
    dfs(0)

    # 2️⃣ Si todos los vértices fueron visitados → conexo
    for i in range(n):
        if not visited[i]:
            return False
    return True

# Grafo 1 — Conexo
vertices1 = LinkedList()
add(vertices1, "A")
add(vertices1, "B")
add(vertices1, "C")

edges1 = LinkedList()
add(edges1, "A"); add(edges1, "B")
add(edges1, "B"); add(edges1, "C")

G1 = createGraph(vertices1, edges1)
print("Grafo 1 es conexo:", isConnected(G1))  # True

# Grafo 2 — No conexo
vertices2 = LinkedList()
add(vertices2, "A")
add(vertices2, "B")
add(vertices2, "C")
add(vertices2, "D")

edges2 = LinkedList()
add(edges2, "A"); add(edges2, "B")
add(edges2, "C"); add(edges2, "D")

G2 = createGraph(vertices2, edges2)
print("Grafo 2 es conexo:", isConnected(G2))  # False
