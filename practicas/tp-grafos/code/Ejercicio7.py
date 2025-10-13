def countConnections(Graph):
    """
    Calcula la cantidad de componentes conexas en un grafo no dirigido.
    Entrada:
        Graph: Array de listas enlazadas (listas de adyacencia)
    Salida:
        Número de componentes conexas (int)
    """
    n = len(Graph)
    if n == 0:
        return 0

    visited = [False] * n
    components = 0

    # --- Función interna recursiva DFS ---
    def dfs(index):
        visited[index] = True
        node = Graph[index].head.nextNode
        while node is not None:
            # Buscar índice del vecino
            neighbor_index = None
            for j in range(n):
                if Graph[j].head.value == node.value:
                    neighbor_index = j
                    break

            if neighbor_index is not None and not visited[neighbor_index]:
                dfs(neighbor_index)

            node = node.nextNode

    # --- Recorremos todos los vértices ---
    for i in range(n):
        if not visited[i]:
            dfs(i)
            components += 1

    return components
from linkedlist import LinkedList, add
from Ejercicio1 import createGraph
from Ejercicio6 import countConnections

# Grafo con 2 componentes: (A-B-C) y (D-E)
vertices = LinkedList()
add(vertices, "A")
add(vertices, "B")
add(vertices, "C")
add(vertices, "D")
add(vertices, "E")

edges = LinkedList()
add(edges, "A"); add(edges, "B")
add(edges, "B"); add(edges, "C")
add(edges, "D"); add(edges, "E")

G = createGraph(vertices, edges)

print("Cantidad de componentes conexas:", countConnections(G))
