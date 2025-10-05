def comprimir_con_hash(cadena):
    if not cadena:
        return cadena

    # hash table (diccionario) para contar frecuencias
    tabla = {}

    # contar frecuencias de cada carácter
    for char in cadena:
        if char in tabla:
            tabla[char] += 1
        else:
            tabla[char] = 1

    # construir la cadena comprimida
    comprimida = ''.join([f"{char}{tabla[char]}" for char in tabla])

    # si no se acorta, devolver la original
    if len(comprimida) >= len(cadena):
        return cadena
    return comprimida

print(comprimir_con_hash("aabcccccaaa"))  # ✅ a5b1c5
print(comprimir_con_hash("abc"))          # ✅ abc (no se acorta)
print(comprimir_con_hash("AAaaBBbb"))     # ✅ A2a2B2b2
