from avltree import*

def rotateLeft(T, x):
    """
    Rotación a la izquierda sobre el nodo x.
    T: AVLTree
    x: AVLNode
    Retorna la nueva raíz de ese subárbol
    """
    y = x.rightnode
    if y is None:
        return x  # No se puede rotar si no hay hijo derecho

    # Hacer el cambio de punteros
    x.rightnode = y.leftnode
    if y.leftnode is not None:
        y.leftnode.parent = x

    y.parent = x.parent
    if x.parent is None:
        T.root = y
    else:
        if x == x.parent.leftnode:
            x.parent.leftnode = y
        else:
            x.parent.rightnode = y

    y.leftnode = x
    x.parent = y

    return y  # Nueva raíz del subárbol


def rotateRight(T, x):
    """
    Rotación a la derecha sobre el nodo x.
    T: AVLTree
    x: AVLNode
    Retorna la nueva raíz de ese subárbol
    """
    y = x.leftnode
    if y is None:
        return x  # No se puede rotar si no hay hijo izquierdo

    # Hacer el cambio de punteros
    x.leftnode = y.rightnode
    if y.rightnode is not None:
        y.rightnode.parent = x

    y.parent = x.parent
    if x.parent is None:
        T.root = y
    else:
        if x == x.parent.leftnode:
            x.par

# Crear un árbol AVL vacío
T = AVLTree()

# Crear nodos manualmente
n1 = AVLNode(); n1.key = 10; n1.value = "A"
n2 = AVLNode(); n2.key = 20; n2.value = "B"
n3 = AVLNode(); n3.key = 30; n3.value = "C"

# Construimos un árbol desbalanceado (desbalance a la derecha)
T.root = n1
n1.rightnode = n2; n2.parent = n1
n2.rightnode = n3; n3.parent = n2

print("Raíz antes de rotar:", T.root.key)  # → 10

# Aplicar rotación izquierda en la raíz
rotateLeft(T, n1)

print("Raíz después de rotar:", T.root.key)  # → 20
print("Hijo izquierdo de la raíz:", T.root.leftnode.key)  # → 10
print("Hijo derecho de la raíz:", T.root.rightnode.key)  # → 30