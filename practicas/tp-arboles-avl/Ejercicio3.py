from algo1 import*
from Ejercicio1 import*
from Ejercicio2 import*

def reBalance(T):
    """
    Rebalancea el árbol AVL aplicando rotaciones según el factor de balance.
    Entrada: T (AVLTree)
    Salida: T (balanceado)
    """
    # Paso 1: recalcular balance factors
    calculateBalance(T)

    def rebalance_node(node):
        if node is None:
            return None

        # Rebalancear primero los hijos (postorden)
        rebalance_node(node.leftnode)
        rebalance_node(node.rightnode)

        # Revisar balance del nodo actual
        if node.bf > 1:  # Desbalanceado a la izquierda
            if node.leftnode is not None and node.leftnode.bf < 0:
                # Rotación doble: izquierda + derecha
                rotateLeft(T, node.leftnode)
            rotateRight(T, node)

        elif node.bf < -1:  # Desbalanceado a la derecha
            if node.rightnode is not None and node.rightnode.bf > 0:
                # Rotación doble: derecha + izquierda
                rotateRight(T, node.rightnode)
            rotateLeft(T, node)

        return node

    rebalance_node(T.root)
    # recalcular balances luego de reestructurar
    calculateBalance(T)
    return T

T = AVLTree()

# Crear manualmente un árbol desbalanceado
n1 = AVLNode(); n1.key = 30; n1.value = "A"
n2 = AVLNode(); n2.key = 20; n2.value = "B"
n3 = AVLNode(); n3.key = 10; n3.value = "C"

T.root = n1
n1.leftnode = n2; n2.parent = n1
n2.leftnode = n3; n3.parent = n2

print("Antes del rebalanceo, raíz:", T.root.key)
reBalance(T)
print("Después del rebalanceo, raíz:", T.root.key)  # → debería ser 20
