from trie import *

def insert(T: Trie, element: str):
    """Inserta una palabra en el Trie T"""
    current = T.root
    for char in element:
        # buscamos si ya existe un hijo con este char
        child = current.children.search(char)
        if child is None:
            # si no existe, lo creamos y lo insertamos en la lista de hijos
            new_node = TrieNode(key=char, parent=current)
            current.children.insert(new_node)
            child = new_node
        # avanzamos al hijo
        current = child
    # marcamos el fin de la palabra
    current.isEndOfWord = True


def search(T: Trie, element: str) -> bool:
    """Verifica si una palabra está en el Trie T"""
    current = T.root
    for char in element:
        child = current.children.search(char)
        if child is None:
            return False
        current = child
    return current.isEndOfWord

