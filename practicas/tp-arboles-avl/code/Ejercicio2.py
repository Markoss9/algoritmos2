from avltree import*
def calculateBalance(T):
    """
    Calcula de forma recursiva el balance factor (bf) de cada nodo del árbol.
    Entrada: AVLTree
    Salida: El mismo árbol T pero con los bf actualizados
    """

    def altura(node):
        if node is None:
            return -1  # Árbol vacío tiene altura -1
        return 1 + max(altura(node.leftnode), altura(node.rightnode))   # Altura del nodo de forma recursiva

    def calcular(node):
        if node is None:
            return
        # calcular primero en hijos
        calcular(node.leftnode)
        calcular(node.rightnode)
        # asignar balance factor
        node.bf = altura(node.leftnode) - altura(node.rightnode)

    calcular(T.root)
    return T


T = AVLTree()
n1 = AVLNode(); n1.key = 10; n1.value = "A"
n2 = AVLNode(); n2.key = 5;  n2.value = "B"
n3 = AVLNode(); n3.key = 15; n3.value = "C"

T.root = n1
n1.leftnode = n2; n2.parent = n1
n1.rightnode = n3; n3.parent = n1

calculateBalance(T)

print(n1.bf, n2.bf, n3.bf)  # → 0, 0, 0 (porque es perfectamente balanceado)
