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
    
    # ---------------------------- Ejercicio 4 ----------------------------
    def insert(self, word):
        """Inserta una palabra en el Trie"""
        node = self.root
        for char in word:
            child = node.children.search(char)
            if not child:  # si no existe, lo creo
                child = TrieNode(char, parent=node)
                node.children.insert(child)
            node = child
        node.isEndOfWord = True

    def _find_node(self, prefix):
        """Devuelve el nodo final del prefijo, o None si no existe"""
        node = self.root
        for char in prefix:
            node = node.children.search(char)
            if not node:
                return None
        return node

    def _dfs(self, node, path, n, result):
        """Recorrido en profundidad para buscar palabras de longitud n"""
        if len(path) == n:
            if node.isEndOfWord:
                result.append("".join(path))
            return
        
        current = node.children.head
        while current:
            child = current.value
            self._dfs(child, path + [child.key], n, result)
            current = current.next

    def palabras_con_prefijo_y_longitud(self, prefijo, n):
        """Devuelve todas las palabras que comienzan con prefijo y tienen longitud n"""
        start_node = self._find_node(prefijo)
        if not start_node:
            return []  # prefijo no encontrado

        result = []
        self._dfs(start_node, list(prefijo), n, result)
        return result
    
    # ---------------------------- Ejercicio 7 ---------------------------- 
    
    def autoCompletar(self, prefijo):
        """Devuelve la continuación única de prefijo, o "" si hay varias o ninguna"""
        node = self._find_node(prefijo)
        if not node:
            return ""   # prefijo no existe
    
        sufijo = []
        while True:
            # contar hijos
            current = node.children.head
            if not current:  # sin hijos → no hay nada que completar
                return ""  

            # ver si hay más de un hijo
            if current.next:  
                return ""  # varias ramas → ambigüedad → no autocompleta

            # si llegamos acá → exactamente 1 hijo
            child = current.value
            sufijo.append(child.key)
            node = child

            # si la palabra terminó y ya no hay más ramas, devolvemos el sufijo
            if node.isEndOfWord and not node.children.head:
                return "".join(sufijo)


