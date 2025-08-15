from avltree import*
from Ejercicio3 import*

def insertAVL(T, element, key):
    """
    Inserta un nodo en un árbol AVL y mantiene el balance.
    T: AVLTreegit push
    element: valor del nodo
    key: clave del nodo
    """
    # 1️Crear nodo nuevo
    nuevo = AVLNode()
    nuevo.key = key
    nuevo.value = element
    nuevo.bf = 0

    # 2️ Insertar como en un BST normal
    if T.root is None:
        T.root = nuevo
        return key

    def insert_rec(node):
        if key < node.key:
            if node.leftnode is None:
                node.leftnode = nuevo
                nuevo.parent = node
                return key
            else:
                return insert_rec(node.leftnode)
        elif key > node.key:
            if node.rightnode is None:
                node.rightnode = nuevo
                nuevo.parent = node
                return key
            else:
                return insert_rec(node.rightnode)
        else:
            # Ya existe la clave
            return None

    insert_rec(T.root)

    # 3️ Rebalancear todo el árbol
    reBalance(T)

    return key
# Crear un AVL vacío
T = AVLTree()

# Insertar elementos
insertAVL(T, "A", 30)
insertAVL(T, "B", 20)
insertAVL(T, "C", 10)  # Esto provoca un desbalance a la izquierda

# Imprimir raíz antes y después del rebalance
print("Raíz después de inserciones y rebalanceo:", T.root.key)  # → 20
print("Hijo izquierdo de la raíz:", T.root.leftnode.key)  # → 10
print("Hijo derecho de la raíz:", T.root.rightnode.key)  # → 30
