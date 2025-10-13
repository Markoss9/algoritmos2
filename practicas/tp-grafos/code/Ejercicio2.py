from linkedlist import search

def existPath(Graph, v1, v2):
    """
    Determina si existe un camino entre v1 y v2 en el grafo.
    Entradas:
        Graph: Array de listas enlazadas (listas de adyacencia)
        v1, v2: vértices del grafo
    Salida:
        True si existe un camino, False si no
    """

    # Crear lista de vértices visitados
    n = len(Graph)
    visited = [False] * n

    # Buscar posición de v1 en el grafo
    start_index = None
    for i in range(n):
        if Graph[i].head.value == v1:
            start_index = i
            break

    if start_index is None:
        return False  # v1 no existe en el grafo

    # --- Función interna recursiva DFS ---
    def dfs(current_index):
        visited[current_index] = True
        current_list = Graph[current_index].head

        # recorrer vecinos
        node = current_list.nextNode
        while node is not None:
            # si encontramos v2 → camino encontrado
            if node.value == v2:
                return True

            # buscar índice del vecino
            neighbor_index = None
            for j in range(n):
                if Graph[j].head.value == node.value:
                    neighbor_index = j
                    break

            # seguir recorriendo vecinos no visitados
            if neighbor_index is not None and not visited[neighbor_index]:
                if dfs(neighbor_index):
                    return True

            node = node.nextNode

        return False

    # iniciar búsqueda desde v1
    return dfs(start_index)

from linkedlist import LinkedList, add
from array import Array
from Ejercicio1 import createGraph  # tu función anterior
from Ejercicio1 import existPath      # esta función

# Crear vértices
vertices = LinkedList()
add(vertices, "A")
add(vertices, "B")
add(vertices, "C")
add(vertices, "D")

# Crear aristas
edges = LinkedList()
add(edges, "A"); add(edges, "B")
add(edges, "B"); add(edges, "C")
add(edges, "C"); add(edges, "D")

# Crear grafo
G = createGraph(vertices, edges)

# Probar caminos
print("¿Existe camino entre A y D?:", existPath(G, "A", "D"))  # True
print("¿Existe camino entre A y Z?:", existPath(G, "A", "Z"))  # False
print("¿Existe camino entre D y A?:", existPath(G, "D", "A"))  # True
