from algo1 import *

# Definición del árbol binario
class BinaryTree:
    root = None

# Definición de nodo del árbol binario
class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None

# Operación: search(B, element)
def search(B, element):
    def search_recursive(node):
        if node is None:
            return None
        if node.value == element:
            return node.key
        
        # Buscar en el subárbol izquierdo
        resultado = search_recursive(node.leftnode)
        if resultado is not None:
            return resultado

        # Buscar en el subárbol derecho
        return search_recursive(node.rightnode)

    return search_recursive(B.root)


def insert(B, element, key):
    # Crear el nuevo nodo con key y element
    nuevo = BinaryTreeNode()
    nuevo.key = key
    nuevo.value = element

    # Si el árbol está vacío
    if B.root is None:
        B.root = nuevo
        return key

    # Lógica auxiliar para inserción
    def insert_rec(node):
        if node is None:
            return None

        # Inserción a la izquierda si la key es menor
        if key < node.key:
            if node.leftnode is None:
                node.leftnode = nuevo
                nuevo.parent = node
                return key
            else:
                return insert_rec(node.leftnode)
        
        # Inserción a la derecha si la key es mayor
        elif key > node.key:
            if node.rightnode is None:
                node.rightnode = nuevo
                nuevo.parent = node
                return key
            else:
                return insert_rec(node.rightnode)

        # Si ya existe un nodo con la misma key, no se inserta
        else:
            return None

    return insert_rec(B.root)


def delete(B, element):
    # Buscar el nodo que contiene el elemento
    node_to_delete = _search_node(B.root, element)

    if node_to_delete is None:
        return None  # Elemento no encontrado

    deleted_key = node_to_delete.key

    # Caso 1: El nodo es una hoja
    if node_to_delete.leftnode is None and node_to_delete.rightnode is None:
        _replace_node_in_parent(B, node_to_delete, None)

    # Caso 2: El nodo tiene solo un hijo
    elif node_to_delete.leftnode is None:
        _replace_node_in_parent(B, node_to_delete, node_to_delete.rightnode)
    elif node_to_delete.rightnode is None:
        _replace_node_in_parent(B, node_to_delete, node_to_delete.leftnode)

    # Caso 3: El nodo tiene dos hijos
    else:
        # Buscar el sucesor (mínimo del subárbol derecho)
        successor = _find_min(node_to_delete.rightnode)

        # Copiar los datos del sucesor al nodo actual
        node_to_delete.key = successor.key
        node_to_delete.value = successor.value

        # Eliminar el sucesor recursivamente (caso simple porque el sucesor no puede tener dos hijos)
        _replace_node_in_parent(B, successor, successor.rightnode)

    return deleted_key


# Función auxiliar: busca el primer nodo con ese valor
def _search_node(node, element):
    if node is None:
        return None
    if node.value == element:
        return node
    # Buscar en subárbol izquierdo
    result = _search_node(node.leftnode, element)
    if result is not None:
        return result
    # Buscar en subárbol derecho
    return _search_node(node.rightnode, element)

# Función auxiliar: reemplaza el nodo en su padre
def _replace_node_in_parent(B, node, new_node):
    if node.parent is None:
        # El nodo es la raíz
        B.root = new_node
        if new_node is not None:
            new_node.parent = None
    else:
        if node == node.parent.leftnode:
            node.parent.leftnode = new_node
        else:
            node.parent.rightnode = new_node
        if new_node is not None:
            new_node.parent = node.parent

# Función auxiliar: mínimo del subárbol
def _find_min(node):
    while node.leftnode is not None:
        node = node.leftnode
    return node


def deleteKey(B, key):
    # Buscar nodo con la clave exacta
    node_to_delete = _search_node_by_key(B.root, key)

    if node_to_delete is None:
        return None  # No se encontró la clave

    deleted_key = node_to_delete.key

    # Caso 1: Nodo hoja
    if node_to_delete.leftnode is None and node_to_delete.rightnode is None:
        _replace_node_in_parent(B, node_to_delete, None)

    # Caso 2: Nodo con un solo hijo
    elif node_to_delete.leftnode is None:
        _replace_node_in_parent(B, node_to_delete, node_to_delete.rightnode)
    elif node_to_delete.rightnode is None:
        _replace_node_in_parent(B, node_to_delete, node_to_delete.leftnode)

    # Caso 3: Nodo con dos hijos
    else:
        successor = _find_min(node_to_delete.rightnode)
        node_to_delete.key = successor.key
        node_to_delete.value = successor.value
        _replace_node_in_parent(B, successor, successor.rightnode)

    return deleted_key


# Función auxiliar para buscar nodo por clave
def _search_node_by_key(node, key):
    if node is None:
        return None
    if node.key == key:
        return node
    # Buscar en subárbol izquierdo
    left_result = _search_node_by_key(node.leftnode, key)
    if left_result is not None:
        return left_result
    # Buscar en subárbol derecho
    return _search_node_by_key(node.rightnode, key)


def access(B, key):
    def access_recursive(node):
        if node is None:
            return None
        if node.key == key:
            return node.value
        # Buscar en subárbol izquierdo
        resultado = access_recursive(node.leftnode)
        if resultado is not None:
            return resultado
        # Buscar en subárbol derecho
        return access_recursive(node.rightnode)

    return access_recursive(B.root)


def update(L, element, key):
    def update_recursive(node):
        if node is None:
            return None
        if node.key == key:
            node.value = element
            return key
        # Buscar en subárbol izquierdo
        resultado = update_recursive(node.leftnode)
        if resultado is not None:
            return resultado
        # Buscar en subárbol derecho
        return update_recursive(node.rightnode)

    return update_recursive(L.root)


# Definición de nodo del árbol avl

class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None









