from trie import *

def insert(T, word):
    """
    Inserta una palabra en el Trie T.
    """
    node = T.root
    for char in word:
        # Buscar si el caracter ya existe entre los hijos
        found_in_children = False
        for child in node.children:
            if child.key == char:
                node = child
                found_in_children = True
                break
        # Si no existe, crear nuevo nodo
        if not found_in_children:
            new_node = TrieNode(key=char, parent=node)
            node.children.append(new_node)
            node = new_node
    node.isEndOfWord = True  # Marca el fin de la palabra

def search(T, word):
    """
    Busca una palabra en el Trie T.
    Devuelve True si existe, False en caso contrario.
    """
    node = T.root
    for char in word:
        char_not_found = True
        for child in node.children:
            if child.key == char:
                node = child
                char_not_found = False
                break
        if char_not_found:
            return False
        
T = Trie()
insert(T, "MARKO")

def buscar_palabra(T, palabra):
    if search(T, palabra):
        print(f"La palabra '{palabra}' fue encontrada en el Trie.")
    else:
        print(f"La palabra '{palabra}' NO fue encontrada en el Trie.")

buscar_palabra(T, "MARK")    # NO fue encontrada
buscar_palabra(T, "MARKO")   # fue encontrada


T = Trie()
buscar_palabra(T,"MARKO")

buscar_palabra(T,"MARK")
buscar_palabra(T,"MARKO")
