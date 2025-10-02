# dictionary.py

# --- Función de hash básica ---
def hash_function(key, m):
    """Calcula la posición en la tabla usando el valor hash del key."""
    return hash(key) % m

# --- Crear Diccionario ---
def create_dictionary(m):
    """
    Crea un diccionario vacío con m posiciones.
    Cada posición se inicializa como una lista vacía (para encadenamiento).
    """
    return [[] for _ in range(m)]

# --- Insertar elemento ---
def insert(D, key, value):
    """
    Inserta un par (key, value) en el diccionario D usando encadenamiento.
    
    Entrada:
        D: diccionario (lista de listas)
        key: clave del elemento a insertar
        value: valor asociado a la clave
    
    Salida:
        Devuelve el diccionario D actualizado
    """
    m = len(D)
    index = hash_function(key, m)

    # Revisar si la clave ya existe en la lista (para actualizar el valor)
    for i, (k, v) in enumerate(D[index]):
        if k == key:
            D[index][i] = (key, value)  # actualizar valor
            return D
    
    # Si no existe, insertar nuevo par
    D[index].append((key, value))
    return D

# --- Buscar elemento ---
def search(D, key):
    """
    Busca un key en el diccionario D.
    
    Entrada:
        D: diccionario (lista de listas)
        key: clave a buscar
    
    Salida:
        Devuelve el value asociado a la key si existe.
        Devuelve None si la key no se encuentra.
    """
    m = len(D)
    index = hash_function(key, m)

    # Recorrer lista en esa posición
    for k, v in D[index]:
        if k == key:
            return v
    
    return None

# --- Eliminar elemento ---
def delete(D, key):
    """
    Elimina un key en el diccionario D.
    
    Descripción:
        Busca la posición determinada por la función de hash y 
        marca la key eliminada como None.
    
    Entrada:
        D: diccionario (lista de listas)
        key: clave a eliminar
    
    Salida:
        Devuelve el diccionario D actualizado
    """
    m = len(D)
    index = hash_function(key, m)

    for i, (k, v) in enumerate(D[index]):
        if k == key:
            # marcar como None según la especificación
            D[index][i] = (None, None)
            return D
    
    return D