from avltree import*
from Ejercicio1 import *
from Ejercicio2 import *
from Ejercicio3 import *

def insertAVL(T, element, key):
    """
    Inserta un nodo en el árbol AVL y lo rebalancea.
    Entrada:
        T: AVLTree
        element: valor
        key: clave entera
    Salida:
        key si se inserta, None si la clave ya existe
    """
    # Crear el nuevo nodo
    nuevo = AVLNode()
    nuevo.key = key
    nuevo.value = element
    nuevo.bf = 0

    # Si el árbol está vacío
    if T.root is None:
        T.root = nuevo
        return key

    # Inserción binaria normal
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
            return None  # no permitir duplicados

    res = insert_rec(T.root)

    # Paso extra: rebalancear todo el árbol
    reBalance(T)

    return res

T = AVLTree()

insertAVL(T, "A", 30)
insertAVL(T, "B", 20)
insertAVL(T, "C", 10)  # ← aquí debería reordenar

print("Raíz después de 3 inserts:", T.root.key)        # → 20
print("Hijo izquierdo:", T.root.leftnode.key)          # → 10
print("Hijo derecho:", T.root.rightnode.key)           # → 30
