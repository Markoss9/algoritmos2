def hash_codigo_postal(codigo, m):
    """
    Función de hash para códigos postales argentinos.
    codigo: string de la forma cddddccc
    m: tamaño de la tabla hash
    """
    a = 37  # base polinómica (puede ser 31, 37 o un número primo cercano)
    h = 0

    for char in codigo:
        if char.isalpha():
            valor = ord(char) - ord('A')  # Convierte letras A-Z en 0-25
        elif char.isdigit():
            valor = int(char)  # Convierte dígitos 0-9 en su valor numérico
        else:
            valor = 0  # Seguridad ante otros caracteres (no esperados)

        # Calcula el hash acumulativo usando una función polinómica
        h = (h * a + valor) % m

    return h


# Ejemplo de uso:
codigo = "C1024CWN"
m = 101  # tamaño de la tabla hash (idealmente primo)
print(f"Hash de {codigo} = {hash_codigo_postal(codigo, m)}")
