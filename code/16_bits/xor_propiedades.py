from functools import reduce


def encontrar_unico(arr):
    # Ejemplo clasico: encontrar el unico numero que no se repite
    # (todos los demas aparecen exactamente 2 veces). Como x^x=0, al
    # hacer XOR de todo el arreglo, los pares se cancelan entre si y
    # queda solo el que no tiene pareja.
    return reduce(lambda a, b: a ^ b, arr, 0)


def pref_xor(a):
    # igual que prefix sum, pero con XOR: util para responder "cual es
    # el XOR del rango [l,r]?" en O(1) tras un preprocesamiento O(n).
    p = [0] * (len(a) + 1)
    for i, x in enumerate(a, 1):
        p[i] = p[i - 1] ^ x
    return p  # xor[l..r] = p[r+1] ^ p[l]


if __name__ == "__main__":
    # --- ejemplo ---
    assert encontrar_unico([4, 1, 2, 1, 2]) == 4
    p = pref_xor([3, 5, 7, 9])
    assert p[3] ^ p[1] == 5 ^ 7   # XOR del rango [1, 2]
    # --- fin ejemplo ---
    import random
    random.seed(0)
    for _ in range(100):
        n = random.randint(1, 10)
        pares = [random.randint(1, 50) for _ in range(n)]
        unico = random.randint(1, 50)
        arr = pares + pares + [unico]
        random.shuffle(arr)
        assert encontrar_unico(arr) == unico

    for _ in range(100):
        n = random.randint(1, 15)
        arr = [random.randint(0, 100) for _ in range(n)]
        p = pref_xor(arr)
        l = random.randint(0, n - 1)
        r = random.randint(l, n - 1)
        esperado = 0
        for i in range(l, r + 1):
            esperado ^= arr[i]
        assert (p[r + 1] ^ p[l]) == esperado
    print("OK")
