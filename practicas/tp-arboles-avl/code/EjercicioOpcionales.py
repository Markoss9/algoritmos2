def height(self):
    """
    Retorna la altura del AVL.
    O(log n) porque la altura de un AVL con n nodos es O(log n),
    y el recorrido desde la raíz a la hoja más profunda sigue un solo camino.
    """
    node = self.root
    h = 0
    while node is not None:
        # Decidimos bajar hacia el hijo de mayor altura
        if node.leftnode and (not node.rightnode or node.leftnode.height >= node.rightnode.height):
            node = node.leftnode
        else:
            node = node.rightnode
        h += 1
    return h

def rank(node, x):
    """
    Retorna cuántos keys ≤ x hay en el subárbol cuya raíz es 'node'.
    O(log n) porque bajamos desde la raíz a una hoja.
    """
    if node is None:
        return 0
    
    if x < node.key:
        # Todo lo que esté a la derecha es mayor, no sirve
        return rank(node.leftnode, x)
    else:
        # El nodo actual cuenta + todo lo que esté a la izquierda
        left_count = node.leftnode.count if node.leftnode else 0
        return left_count + 1 + rank(node.rightnode, x)


def count_in_interval(T, a, b):
    """
    Retorna cuántos nodos tienen key en [a, b].
    O(log n).
    """
    return rank(T.root, b) - rank(T.root, a - 1)
