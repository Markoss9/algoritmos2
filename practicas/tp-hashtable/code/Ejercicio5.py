def todos_unicos(L):
    tabla = {}  # diccionario vacío, nuestra tabla hash

    for elemento in L:
        if elemento in tabla:   # búsqueda en O(1) promedio
            return False        # repetido
        tabla[elemento] = True  # lo marcamos como visto

    return True  # no se repitió ninguno

L = [1, 5, 12, 1, 2]
print(todos_unicos(L)) 

S = [3, 7, 2, 5]
print(todos_unicos(S))
