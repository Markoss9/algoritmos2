from trie import *

def delete(T, element):
    current = T.root
    
    # 1. Buscar palabra
    for char in element:
        child = current.children.search(char)
        if child is None:
            return False  # palabra no existe
        current = child
    
    # 2. Marcar nodo final como no fin de palabra
    if not current.isEndOfWord:
        return False  # la palabra no estaba marcada como existente
    
    current.isEndOfWord = False
    
    # 3. Eliminar nodos innecesarios hacia atrás
    while current.parent is not None:
        if current.children.head is None and not current.isEndOfWord:
            # eliminar este nodo de la lista de hijos de su padre
            parent = current.parent
            remove_from_linkedlist(parent.children, current.key)
            current = parent
        else:
            break
    
    return True


def remove_from_linkedlist(ll, key):
    current = ll.head
    prev = None
    while current:
        if current.value.key == key:
            if prev:
                prev.next = current.next
            else:
                ll.head = current.next
            return
        prev = current
        current = current.next
