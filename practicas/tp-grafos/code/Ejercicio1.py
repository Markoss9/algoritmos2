from array import Array
from linkedlist import *

def createGraph(vertices, edges):
    """
    Crea un grafo representado por listas de adyacencia.
    Entradas:
        vertices: LinkedList con los vértices
        edges: LinkedList con pares de vértices (u, v)
    Salida:
        Graph: Array(n, LinkedList())
    """

    # 1️⃣ Crear el arreglo principal del grafo
    n = len(vertices)
    Graph = Array(n, LinkedList())

    # 2️⃣ Copiar cada vértice a una posición del array
    # Ej: si vertices = [A, B, C] → Graph[0] = LinkedList(A)
    current = vertices.head
    i = 0
    while current is not None:
        # Creamos la lista de adyacencia para cada vértice
        Graph[i] = LinkedList()
        add(Graph[i], current.value)  # agregamos el propio vértice como referencia
        current = current.nextNode
        i += 1

    # 3️⃣ Recorrer la lista de aristas para agregar adyacencias
    edge = edges.head
    while edge is not None and edge.nextNode is not None:
        u = edge.value
        v = edge.nextNode.value

        # Buscar las posiciones de u y v en vertices
        pos_u = search(vertices, u)
        pos_v = search(vertices, v)

        # Agregar v en la lista de adyacencia de u
        if pos_u is not None:
            add(Graph[pos_u], v)

        # Agregar u en la lista de adyacencia de v (grafo no dirigido)
        if pos_v is not None:
            add(Graph[pos_v], u)

        # Pasar al siguiente par
        edge = edge.nextNode.nextNode

    return Graph


# Lista de vértices: A, B, C
vertices = LinkedList()
add(vertices, "A")
add(vertices, "B")
add(vertices, "C")

# Lista de aristas: A-B, B-C, A-C
edges = LinkedList()
add(edges, "A")
add(edges, "B")
add(edges, "B")
add(edges, "C")
add(edges, "A")
add(edges, "C")

G = createGraph(vertices, edges)

# Mostrar el grafo
for i in range(len(vertices)):
    print("Adyacentes de", G[i].head.value, "→", end=" ")
    node = G[i].head.nextNode
    while node is not None:
        print(node.value, end=" ")
        node = node.nextNode
    print()
