# Cuando n es demasiado grande para probar todos los 2^n subconjuntos
# de una vez (fuerza bruta) pero demasiado pequeno para DP normal --
# tipicamente 20 < n <= 40. Se divide el arreglo a la mitad (2^(n/2)
# cada una, manejable) y se combinan resultados.

import bisect


def contar_subsets_suma(arr, target):
    n = len(arr)
    A = arr[:n // 2]
    B = arr[n // 2:]
    SA = [0]
    for x in A:
        SA += [s + x for s in SA]
    SB = [0]
    for x in B:
        SB += [s + x for s in SB]
    SB.sort()
    cnt = 0
    for s in SA:
        t = target - s
        cnt += bisect.bisect_right(SB, t) - bisect.bisect_left(SB, t)
    return cnt


def fuerza_bruta(arr, target):
    n = len(arr)
    cnt = 0
    for mask in range(1 << n):
        s = sum(arr[i] for i in range(n) if mask & (1 << i))
        if s == target:
            cnt += 1
    return cnt


if __name__ == "__main__":
    # --- ejemplo ---
    # subconjuntos de [1..6] con suma 7: {1,6}, {2,5}, {3,4}, {1,2,4}
    assert contar_subsets_suma([1, 2, 3, 4, 5, 6], 7) == 4
    # --- fin ejemplo ---
    arr = [1, 2, 3, 4, 5]
    for target in range(0, 16):
        assert contar_subsets_suma(arr, target) == fuerza_bruta(arr, target), target
    print("OK")
