import heapq
from collections import Counter
from functools import cmp_to_key


def frecuencias(arr):
    return Counter(arr)            # valor -> cantidad (0 si no aparece)


def mas_frecuentes(arr, k):
    # [(valor, cantidad)] de mayor a menor; los empates quedan por primera aparicion
    return Counter(arr).most_common(k)


def son_anagramas(a, b):
    return Counter(a) == Counter(b)


def sobrantes(a, b):
    # elementos de a que no se pueden emparejar con los de b (multiconjuntos)
    return Counter(a) - Counter(b)


def k_mayores(arr, k):
    return heapq.nlargest(k, arr)     # O(n log k), sin ordenar todo


def k_menores(arr, k):
    return heapq.nsmallest(k, arr)


def ordenar_desc_x_asc_y(pares):
    # mayor x primero; a igual x, menor y primero (se niega el valor a invertir)
    return sorted(pares, key=lambda p: (-p[0], p[1]))


def ordenar_con_comparador(arr, cmp):
    # cmp(a, b) < 0 si a va antes que b; > 0 si va despues; 0 si es igual
    return sorted(arr, key=cmp_to_key(cmp))


if __name__ == "__main__":
    import random

    # --- ejemplo ---
    assert frecuencias("abracadabra")["a"] == 5
    assert frecuencias("abracadabra")["z"] == 0
    assert mas_frecuentes("abracadabra", 2) == [("a", 5), ("b", 2)]
    assert son_anagramas("listen", "silent") is True
    assert son_anagramas("aab", "abb") is False
    assert sobrantes("aabbb", "ab") == Counter({"a": 1, "b": 2})
    assert k_mayores([5, 1, 9, 3, 7], 2) == [9, 7]
    assert k_menores([5, 1, 9, 3, 7], 2) == [1, 3]
    assert ordenar_desc_x_asc_y([(1, 5), (3, 2), (3, 1), (2, 9)]) == [(3, 1), (3, 2), (2, 9), (1, 5)]
    # --- fin ejemplo ---
    # ordenar para que al concatenar salga el numero mas grande posible
    mayor = ordenar_con_comparador(["3", "30", "34", "5", "9"], lambda a, b: -1 if a + b > b + a else 1)
    assert "".join(mayor) == "9534330"

    random.seed(6)
    for _ in range(300):
        arr = [random.randint(0, 6) for _ in range(random.randint(0, 12))]
        k = random.randint(0, 5)
        assert k_mayores(arr, k) == sorted(arr, reverse=True)[:k]
        assert k_menores(arr, k) == sorted(arr)[:k]
        cuenta = {v: arr.count(v) for v in set(arr)}
        assert dict(frecuencias(arr)) == cuenta
        top = mas_frecuentes(arr, k)
        assert [c for _, c in top] == sorted(cuenta.values(), reverse=True)[:k]
    print("OK")
