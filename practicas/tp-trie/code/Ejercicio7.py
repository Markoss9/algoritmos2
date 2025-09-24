from trie import *

def autoCompletar(self, prefijo):
    """Devuelve la continuación única de prefijo, o "" si hay varias o ninguna"""
    node = self._find_node(prefijo)
    if not node:
        return ""   # prefijo no existe
    
    sufijo = []
    while True:
        # contar hijos
        current = node.children.head
        if not current:  # sin hijos → no hay nada que completar
            return ""  

        # ver si hay más de un hijo
        if current.next:  
            return ""  # varias ramas → ambigüedad → no autocompleta

        # si llegamos acá → exactamente 1 hijo
        child = current.value
        sufijo.append(child.key)
        node = child

        # si la palabra terminó y ya no hay más ramas, devolvemos el sufijo
        if node.isEndOfWord and not node.children.head:
            return "".join(sufijo)

# Supongamos que ya tenés Trie, TrieNode, LinkedList y Node definidos
t = Trie()

# Insertamos algunas palabras
t.insert("hola")
t.insert("holanda")
t.insert("hombre")
t.insert("helicoptero")
t.insert("helado")

# Caso 1: prefijo con autocompletado único
print(t.autoCompletar("homb"))  # Output: "re"
# Explicación: sólo hay una palabra que continúa "homb" → "hombre"

# Caso 2: prefijo con varias posibilidades → devuelve ""
print(t.autoCompletar("ho"))    # Output: ""
# Explicación: "ho" puede continuar con "la", "landa" o "mbre" → varias ramas

# Caso 3: prefijo que no existe → devuelve ""
print(t.autoCompletar("x"))     # Output: ""
# Explicación: no hay palabras que comiencen con "x"

# Caso 4: prefijo con autocompletado único parcial
print(t.autoCompletar("heli"))  # Output: "coptero"
# Explicación: sólo hay una palabra que continúa "heli" → "helicoptero"
