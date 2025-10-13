# -------------------------------
# Módulo: linkedlist.py
# -------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None


# -------------------------------
# Función: add(lista, elemento)
# Descripción: agrega un elemento al final de la lista
# -------------------------------
def add(linkedList, element):
    newNode = Node(element)
    if linkedList.head is None:
        linkedList.head = newNode
        return
    current = linkedList.head
    while current.nextNode is not None:
        current = current.nextNode
    current.nextNode = newNode


# -------------------------------
# Función: search(lista, elemento)
# Descripción: busca un elemento y devuelve su posición (índice)
# -------------------------------
def search(linkedList, element):
    current = linkedList.head
    index = 0
    while current is not None:
        if current.value == element:
            return index
        current = current.nextNode
        index += 1
    return None


# -------------------------------
# Función: insert(lista, elemento, posición)
# Descripción: inserta un elemento en una posición específica
# -------------------------------
def insert(linkedList, element, position):
    newNode = Node(element)
    if position == 0:
        newNode.nextNode = linkedList.head
        linkedList.head = newNode
        return
    current = linkedList.head
    index = 0
    while current is not None and index < position - 1:
        current = current.nextNode
        index += 1
    if current is None:
        return  # posición fuera de rango
    newNode.nextNode = current.nextNode
    current.nextNode = newNode


# -------------------------------
# Función: delete(lista, posición)
# Descripción: elimina el elemento en una posición específica
# -------------------------------
def delete(linkedList, position):
    if linkedList.head is None:
        return
    if position == 0:
        linkedList.head = linkedList.head.nextNode
        return
    current = linkedList.head
    index = 0
    while current.nextNode is not None and index < position - 1:
        current = current.nextNode
        index += 1
    if current.nextNode is None:
        return  # fuera de rango
    current.nextNode = current.nextNode.nextNode


# -------------------------------
# Función: length(lista)
# Descripción: devuelve la cantidad de elementos de la lista
# -------------------------------
def length(linkedList):
    count = 0
    current = linkedList.head
    while current is not None:
        count += 1
        current = current.nextNode
    return count


# -------------------------------
# Función: printList(lista)
# Descripción: imprime todos los elementos
# -------------------------------
def printList(linkedList):
    current = linkedList.head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.nextNode
    print("None")

from linkedlist import LinkedList, add, search, delete, insert, printList, length

L = LinkedList()
add(L, "A")
add(L, "B")
add(L, "C")

print("Lista inicial:")
printList(L)

print("Posición de 'B':", search(L, "B"))
print("Longitud:", length(L))

insert(L, "X", 1)
print("Después de insertar 'X' en posición 1:")
printList(L)

delete(L, 2)
print("Después de eliminar posición 2:")
printList(L)
