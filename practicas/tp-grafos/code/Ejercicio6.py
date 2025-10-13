from linkedlist import LinkedList, add

def convertTree(Graph):
    """
    Determina qué aristas deben eliminarse para que el grafo se convierta en un árbol.
    Entrada:
        Graph: Array de listas de adyacencia (grafo no dirigido)
    Salida:
        LinkedList con las aristas (pares de vértices) que deben eliminarse
    """

    n = len(Graph)
    visited = [False] * n
    edges_to_remove = LinkedList()

    # --- Función interna recursiva DFS ---
    def dfs(current_index, parent_index):
        visited[current_index] = True
        node = Graph[current_index].head.nextNode

        while node is not None:
            # buscar índice del vecino
            neighbor_index = None
            for j in range(n):
                if Graph[j].head.value == node.value:
                    neighbor_index = j
                    break

            if neighbor_index is not None:
                if not visited[neighbor_index]:
                    dfs(neighbor_index, current_index)
                elif neighbor_index != parent_index:
                    # arista repetida (ciclo detectado)
                    # evitar duplicados (ej: A-B y B-A)
                    exists = False
                    current_r = edges_to_remove.head
                    while current_r is not None and current_r.nextNode is not None:
                        u = current_r.value
                        v = current_r.nextNode.value
                        if (u == Graph[current_index].head.value and v == node.value) or \
                           (u == node.value and v == Graph[current_index].head.value):
                            exists = True
                            break
                        current_r = current_r.nextNode.nextNode

                    if not exists:
                        add(edges_to_remove, Graph[current_index].head.value)
                        add(edges_to_remove, node.value)

            node = node.nextNode

    # 1️⃣ Iniciar DFS desde el primer vértice
    dfs(0, -1)

    return edges_to_remove

from linkedlist import LinkedList, add, printList
from Ejercicio1 import createGraph
from Ejercicio4 import convertTree

# Grafo con ciclo: A-B-C-A-D
vertices = LinkedList()
add(vertices, "A")
add(vertices, "B")
add(vertices, "C")
add(vertices, "D")

edges = LinkedList()
add(edges, "A"); add(edges, "B")
add(edges, "B"); add(edges, "C")
add(edges, "C"); add(edges, "A")
add(edges, "A"); add(edges, "D")

G = createGraph(vertices, edges)

# Buscar aristas a eliminar
edges_to_remove = convertTree(G)

print("Aristas que deben eliminarse para convertir el grafo en árbol:")
current = edges_to_remove.head
while current is not None and current.nextNode is not None:
    print(f"{current.value} - {current.nextNode.value}")
    current = current.nextNode.nextNode
