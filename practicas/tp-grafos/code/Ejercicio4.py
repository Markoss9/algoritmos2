def isTree(Graph):
    """
    Determina si un grafo no dirigido es un árbol.
    Entradas:
        Graph: Array de listas enlazadas (listas de adyacencia)
    Salida:
        True si el grafo es un árbol, False si no
    """

    n = len(Graph)
    if n == 0:
        return False

    visited = [False] * n

    # --- Función interna recursiva DFS ---
    def dfs(current_index, parent_index):
        visited[current_index] = True
        node = Graph[current_index].head.nextNode

        while node is not None:
            # buscar el índice del vecino
            neighbor_index = None
            for j in range(n):
                if Graph[j].head.value == node.value:
                    neighbor_index = j
                    break

            # Si el vecino fue visitado y no es el padre → ciclo
            if neighbor_index is not None:
                if visited[neighbor_index] and neighbor_index != parent_index:
                    return True  # ciclo detectado

                # Si no fue visitado → continuar DFS
                if not visited[neighbor_index]:
                    if dfs(neighbor_index, current_index):
                        return True
            node = node.nextNode

        return False

    # 1️⃣ Empezamos desde el primer vértice
    if dfs(0, -1):
        return False  # hay ciclo

    # 2️⃣ Verificar que todos los vértices fueron visitados (grafo conexo)
    for i in range(n):
        if not visited[i]:
            return False  # no es conexo

    return True
from linkedlist import LinkedList, add
from array import Array
from Ejercicio1 import createGraph
from Ejercicio3 import isTree

# Grafo 1 — Árbol (conexo y sin ciclos)
vertices1 = LinkedList()
add(vertices1, "A")
add(vertices1, "B")
add(vertices1, "C")
add(vertices1, "D")

edges1 = LinkedList()
add(edges1, "A"); add(edges1, "B")
add(edges1, "A"); add(edges1, "C")
add(edges1, "B"); add(edges1, "D")

G1 = createGraph(vertices1, edges1)
print("Grafo 1 es árbol:", isTree(G1))  # True

# Grafo 2 — No es árbol (tiene ciclo A-B-C-A)
vertices2 = LinkedList()
add(vertices2, "A")
add(vertices2, "B")
add(vertices2, "C")

edges2 = LinkedList()
add(edges2, "A"); add(edges2, "B")
add(edges2, "B"); add(edges2, "C")
add(edges2, "C"); add(edges2, "A")

G2 = createGraph(vertices2, edges2)
print("Grafo 2 es árbol:", isTree(G2))  # False
