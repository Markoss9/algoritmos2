def rabin_karp(S, P):
    L, K = len(S), len(P)
    if K > L:
        return -1

    base = 256
    mod = 10**9 + 7  # número primo grande

    # precomputar base^(K-1)
    high_order = pow(base, K - 1, mod)

    # calcular hash del patrón y primera ventana
    hash_p = 0
    hash_s = 0
    for i in range(K):
        hash_p = (hash_p * base + ord(P[i])) % mod
        hash_s = (hash_s * base + ord(S[i])) % mod

    # recorrer texto
    for i in range(L - K + 1):
        if hash_p == hash_s:
            # verificar coincidencia real (por colisiones)
            if S[i:i + K] == P:
                return i  # primera ocurrencia

        if i < L - K:
            # actualizar hash (rolling)
            hash_s = (hash_s - ord(S[i]) * high_order) % mod
            hash_s = (hash_s * base + ord(S[i + K])) % mod
            hash_s = (hash_s + mod) % mod  # evitar negativos

    return -1

S = "abracadabra"
P = "cada"
print(rabin_karp(S, P))  # salida: 4
