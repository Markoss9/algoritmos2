# ----------------------------
# Estructura de Lista Enlazada, comoo vamos a usar listas enlazadas, necesitás tener definida una LinkedList y Node
# ----------------------------
class Node:
    def __init__(self, value=None):
        self.value = value   # Puede ser un TrieNode
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        """Inserta un nuevo nodo al inicio"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        """Busca un TrieNode con cierto key dentro de la lista"""
        current = self.head
        while current:
            if current.value.key == key:
                return current.value
            current = current.next
        return None

class TrieNode:
    def __init__(self, key=None, parent=None):
        self.key = key                   # Carácter
        self.parent = parent             # Nodo padre
        self.children = LinkedList()     # Lista de hijos (TrieNodes)
        self.isEndOfWord = False         # Marca de fin de palabra

class Trie:
    def __init__(self):
        self.root = TrieNode("*")  # raíz con símbolo especial


