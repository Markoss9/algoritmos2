from linkedlist import LinkedList, add
from array import Array

def convertToDFSTree(Graph, root):
    """
    Convierte un grafo en un árbol DFS (Depth-First Search Tree)
    usando 'root' como vértice raíz.
    Entrada:
        Graph: Array de listas enlazadas (representación de lista de adyacencia)
        root: vértice raíz
    Salida:
        Nuevo grafo (lista de adyacencia) con estructura del árbol DFS
    """
    n = len(Graph)
    if n == 0:
        return None

    # Crear nuevo grafo vacío con los mismos vértices
    dfsTree = Array(n, LinkedList)
    for i in range(n):
        dfsTree[i] = LinkedList()
        add(dfsTree[i], Graph[i].head.value)

    # Buscar índice de la raíz
    root_index = None
    for i in range(n):
        if Graph[i].head.value == root:
            root_index = i
            break
    if root_index is None:
        print("Error: raíz no encontrada en el grafo.")
        return None

    visited = [False] * n

    # --- Función recursiva DFS ---
    def dfs(u_index):
        visited[u_index] = True
        node = Graph[u_index].head.nextNode
        while node is not None:
            # Buscar índice del vecino
            v_index = None
            for j in range(n):
                if Graph[j].head.value == node.value:
                    v_index = j
                    break

            # Si el vecino no fue visitado, agregar arista y seguir DFS
            if v_index is not None and not visited[v_index]:
                add(dfsTree[u_index], Graph[v_index].head.value)
                add(dfsTree[v_index], Graph[u_index].head.value)  # grafo no dirigido
                dfs(v_index)

            node = node.nextNode

    # Iniciar DFS desde la raíz
    dfs(root_index)

    return dfsTree

from linkedlist import LinkedList, add
from Ejercicio1 import createGraph
from Ejercicio8 import convertToDFSTree

# Crear vértices
vertices = LinkedList()
add(vertices, "A")
add(vertices, "B")
add(vertices, "C")
add(vertices, "D")
add(vertices, "E")

# Crear aristas
edges = LinkedList()
add(edges, "A"); add(edges, "B")
add(edges, "A"); add(edges, "C")
add(edges, "B"); add(edges, "D")
add(edges, "C"); add(edges, "E")
add(edges, "B"); add(edges, "E")

# Crear grafo original
G = createGraph(vertices, edges)

# Convertir a árbol DFS desde "A"
dfsTree = convertToDFSTree(G, "A")

# Mostrar el árbol DFS
for i in range(len(dfsTree)):
    print(f"{dfsTree[i].head.value} -> ", end="")
    node = dfsTree[i].head.nextNode
    while node is not None:
        print(node.value, end=" -> ")
        node = node.nextNode
    print()
