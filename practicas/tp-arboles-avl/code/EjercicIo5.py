from Ejercicio3 import reBalance

def delete(T, element):
    """
    Elimina el nodo cuyo value == element del árbol AVL T y rebalancea.
    Retorna la clave eliminada o None si no existe.
    """
    # Buscar el nodo a eliminar
    node_to_delete = _search_node(T.root, element)
    if node_to_delete is None:
        return None

    deleted_key = node_to_delete.key

    # Caso 1: hoja
    if node_to_delete.leftnode is None and node_to_delete.rightnode is None:
        _replace_node_in_parent(T, node_to_delete, None)
    # Caso 2: un solo hijo
    elif node_to_delete.leftnode is None:
        _replace_node_in_parent(T, node_to_delete, node_to_delete.rightnode)
    elif node_to_delete.rightnode is None:
        _replace_node_in_parent(T, node_to_delete, node_to_delete.leftnode)
    # Caso 3: dos hijos
    else:
        successor = _find_min(node_to_delete.rightnode)
        node_to_delete.key = successor.key
        node_to_delete.value = successor.value
        _replace_node_in_parent(T, successor, successor.rightnode)

    # Rebalancear el árbol AVL
    reBalance(T)
    return deleted_key