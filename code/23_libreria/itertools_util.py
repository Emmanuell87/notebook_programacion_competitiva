from itertools import accumulate, chain, combinations, groupby, permutations, product


def sumas_prefijo(arr):
    # p[i] = suma de arr[:i]; la suma de arr[l:r] es p[r] - p[l]
    return [0] + list(accumulate(arr))


def maximo_acumulado(arr):
    # m[i] = max(arr[:i + 1])
    return list(accumulate(arr, max))


def rachas(s):
    # codificacion por longitud de racha: "aaabcc" -> [('a', 3), ('b', 1), ('c', 2)]
    return [(c, len(list(g))) for c, g in groupby(s)]


def aplanar(listas):
    return list(chain.from_iterable(listas))


def secuencias(simbolos, largo):
    # todas las secuencias de ese largo, con repeticion (n ** largo)
    return list(product(simbolos, repeat=largo))


def subconjuntos_de_tamano(arr, k):
    return list(combinations(arr, k))


def ordenamientos(arr):
    return list(permutations(arr))


if __name__ == "__main__":
    from math import factorial, comb

    # --- ejemplo ---
    assert sumas_prefijo([3, 1, 4, 1, 5]) == [0, 3, 4, 8, 9, 14]
    p = sumas_prefijo([3, 1, 4, 1, 5])
    assert p[4] - p[1] == 1 + 4 + 1          # suma de arr[1:4]
    assert maximo_acumulado([3, 1, 4, 1, 5]) == [3, 3, 4, 4, 5]
    assert rachas("aaabcc") == [("a", 3), ("b", 1), ("c", 2)]
    assert aplanar([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
    assert secuencias("ab", 2) == [("a", "a"), ("a", "b"), ("b", "a"), ("b", "b")]
    assert subconjuntos_de_tamano([1, 2, 3], 2) == [(1, 2), (1, 3), (2, 3)]
    # --- fin ejemplo ---
    assert ordenamientos([1, 2, 3])[:2] == [(1, 2, 3), (1, 3, 2)]
    assert sumas_prefijo([]) == [0]
    assert rachas("") == []

    assert len(secuencias(range(3), 4)) == 3 ** 4
    assert len(subconjuntos_de_tamano(range(6), 3)) == comb(6, 3)
    assert len(ordenamientos(range(5))) == factorial(5)
    print("OK")
