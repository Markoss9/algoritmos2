# --- Crear Diccionario ---
def create_dictionary(m):
    """
    Crea un diccionario vacío con m posiciones.
    Cada posición se inicializa como una lista vacía (para encadenamiento).
    """
    return [[] for _ in range(m)]
