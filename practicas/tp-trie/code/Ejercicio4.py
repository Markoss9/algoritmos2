from trie import *

def find_node(self, prefix):
        """Devuelve el nodo final del prefijo, o None si no existe"""
        node = self.root
        for char in prefix:
            node = node.children.search(char)
            if not node:
                return None
        return node

def dfs(self, node, path, n, result):
        """Recorrido en profundidad para buscar palabras de longitud n"""
        if len(path) == n:
            if node.isEndOfWord:
                result.append("".join(path))
            return
        
        current = node.children.head
        while current:
            child = current.value
            self._dfs(child, path + [child.key], n, result)
            current = current.next

def palabras_con_prefijo_y_longitud(self, prefijo, n):
        """Devuelve todas las palabras que comienzan con prefijo y tienen longitud n"""
        start_node = self._find_node(prefijo)
        if not start_node:
            return []  # prefijo no encontrado

        result = []
        self._dfs(start_node, list(prefijo), n, result)
        return result

# Crear Trie
t = Trie()
t.insert("hola")
t.insert("hondo")
t.insert("honor")
t.insert("hora")
t.insert("hoja")
t.insert("hogar")

# Buscar
print(t.palabras_con_prefijo_y_longitud("ho", 4))  # ['hora', 'hoja']
print(t.palabras_con_prefijo_y_longitud("hon", 5)) # ['hondo', 'honor']
print(t.palabras_con_prefijo_y_longitud("ho", 5))  # ['hogar']
