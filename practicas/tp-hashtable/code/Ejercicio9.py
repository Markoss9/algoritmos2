def es_subconjunto(S, T):
    # Crear la tabla hash con los elementos de T
    tabla_T = set(T)  # en Python, set usa hashing internamente

    # Verificar cada elemento de S
    for s in S:
        if s not in tabla_T:
            return False  # si falta alguno, no es subconjunto
    return True

S = {1, 2, 3}
T = {0, 1, 2, 3, 4, 5}
print(es_subconjunto(S, T))  # ✅ True

S = {1, 2, 6}
print(es_subconjunto(S, T))  # ❌ False
