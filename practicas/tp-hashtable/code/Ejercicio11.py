class Slot:
    def __init__(self):
        self.flag = "free"     # indica si está libre o usado
        self.key = None
        self.value = None
        self.next = None       # para la lista de libres o colisiones


class HashTable:
    def __init__(self, m):
        self.m = m
        self.table = [Slot() for _ in range(m)]

        # Construcción de la lista de libres (simplemente enlazada)
        for i in range(m - 1):
            self.table[i].next = self.table[i + 1]
        self.free_head = self.table[0]

        # Tabla principal de punteros (una por posición hash)
        self.buckets = [None for _ in range(m)]

    def hash(self, key):
        """Función de hash simple"""
        return hash(key) % self.m

    def insert(self, key, value):
        """Inserta (key, value) en O(1) usando la lista de libres"""
        if not self.free_head:
            raise Exception("No hay espacio libre en la tabla")

        # Tomar nodo libre
        slot = self.free_head
        self.free_head = slot.next

        # Asignar datos
        slot.key = key
        slot.value = value
        slot.flag = "used"

        # Insertar en el bucket (al frente de la lista de colisiones)
        index = self.hash(key)
        slot.next = self.buckets[index]
        self.buckets[index] = slot

    def search(self, key):
        """Busca una clave en O(1) promedio"""
        index = self.hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key and current.flag == "used":
                return current.value
            current = current.next
        return None

    def delete(self, key):
        """Elimina un elemento y lo devuelve a la lista libre en O(1)"""
        index = self.hash(key)
        prev = None
        current = self.buckets[index]

        # Buscar el elemento en la lista del bucket
        while current:
            if current.key == key and current.flag == "used":
                # Eliminar de la lista de colisiones
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next

                # Resetear slot y devolverlo a la lista libre
                current.key = None
                current.value = None
                current.flag = "free"

                current.next = self.free_head
                self.free_head = current
                return
            prev = current
            current = current.next

        raise KeyError("Clave no encontrada")

    def __repr__(self):
        """Representación del estado de la tabla (para depuración)"""
        lines = []
        for i, head in enumerate(self.buckets):
            s = f"Bucket {i}:"
            current = head
            while current:
                s += f" -> ({current.key}, {current.value})"
                current = current.next
            lines.append(s)
        return "\n".join(lines)


# Crear una tabla de tamaño 5
ht = HashTable(5)

# Insertar valores
ht.insert("a", 1)
ht.insert("b", 2)
ht.insert("c", 3)

print(ht)
# Buscar
print(ht.search("b"))  # 2

# Eliminar
ht.delete("b")
print(ht.search("b"))  # None

# Insertar otro elemento (reutiliza slot libre)
ht.insert("d", 4)
print(ht)
