from linkedlist import LinkedList, add
from array import Array

def convertToBFSTree(Graph, root):
    """
    Convierte un grafo en un árbol BFS usando 'root' como raíz.
    Entrada:
        Graph: Array de listas enlazadas (grafo original)
        root: vértice raíz desde donde iniciar BFS
    Salida:
        Nuevo grafo (lista de adyacencia) con la estructura del árbol BFS
    """
    n = len(Graph)
    if n == 0:
        return None

    # Crear nuevo grafo vacío con los mismos vértices
    bfsTree = Array(n, LinkedList)
    for i in range(n):
        bfsTree[i] = LinkedList()
        add(bfsTree[i], Graph[i].head.value)

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
    queue = [root_index]
    visited[root_index] = True

    while len(queue) > 0:
        u_index = queue.pop(0)
        u_node = Graph[u_index].head.nextNode

        while u_node is not None:
            # Buscar índice del vecino
            v_index = None
            for j in range(n):
                if Graph[j].head.value == u_node.value:
                    v_index = j
                    break

            # Si no fue visitado, agregar arista (u, v)
            if v_index is not None and not visited[v_index]:
                visited[v_index] = True
                add(bfsTree[u_index], Graph[v_index].head.value)
                add(bfsTree[v_index], Graph[u_index].head.value)  # No dirigido
                queue.append(v_index)

            u_node = u_node.nextNode

    return bfsTree

from linkedlist import LinkedList, add
from Ejercicio1 import createGraph
from Ejercicio7 import convertToBFSTree

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

# Convertir a árbol BFS desde "A"
bfsTree = convertToBFSTree(G, "A")

# Mostrar el árbol BFS
for i in range(len(bfsTree)):
    print(f"{bfsTree[i].head.value} -> ", end="")
    node = bfsTree[i].head.nextNode
    while node is not None:
        print(node.value, end=" -> ")
        node = node.nextNode
    print()
