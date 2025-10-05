def es_permutacion(s, p):
    # Si las longitudes difieren, ya no son permutaciones
    if len(s) != len(p):
        return False

    # Contar caracteres en s
    conteo = {}
    for c in s:
        conteo[c] = conteo.get(c, 0) + 1

    # Restar conteos según p
    for c in p:
        if c not in conteo:
            return False
        conteo[c] -= 1
        if conteo[c] < 0:
            return False

    # Si todos los conteos quedaron en 0, son permutaciones
    return True

#   es_permutacion("hola", "ahlo") → True
#   es_permutacion("hola", "ahdo") → False
