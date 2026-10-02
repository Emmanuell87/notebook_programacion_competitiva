from bisect import bisect_left, bisect_right, insort

# arr debe estar ORDENADO (no decreciente). Cada consulta es O(log n).


def lower_bound(arr, x):
    # primer indice i con arr[i] >= x (len(arr) si no hay)
    return bisect_left(arr, x)


def upper_bound(arr, x):
    # primer indice i con arr[i] > x (len(arr) si no hay)
    return bisect_right(arr, x)


def contar_en_rango(arr, lo, hi):
    # cantidad de elementos v con lo <= v <= hi
    return bisect_right(arr, hi) - bisect_left(arr, lo)


def contiene(arr, x):
    i = bisect_left(arr, x)
    return i < len(arr) and arr[i] == x


def mayor_menor_o_igual(arr, x):
    # el mayor elemento <= x, o None si no hay
    i = bisect_right(arr, x)
    return arr[i - 1] if i else None


def menor_mayor_o_igual(arr, x):
    # el menor elemento >= x, o None si no hay
    i = bisect_left(arr, x)
    return arr[i] if i < len(arr) else None


def insertar_ordenado(arr, x):
    # inserta x dejando arr ordenado (la busqueda es O(log n), pero
    # desplazar elementos de la lista cuesta O(n))
    insort(arr, x)


if __name__ == "__main__":
    import random

    # --- ejemplo ---
    arr = [1, 3, 3, 5, 8]
    assert lower_bound(arr, 3) == 1
    assert upper_bound(arr, 3) == 3
    assert contar_en_rango(arr, 3, 5) == 3
    assert contiene(arr, 8) is True and contiene(arr, 4) is False
    assert mayor_menor_o_igual(arr, 4) == 3
    assert menor_mayor_o_igual(arr, 4) == 5
    assert mayor_menor_o_igual(arr, 0) is None
    # --- fin ejemplo ---

    random.seed(2)
    for _ in range(500):
        a = sorted(random.randint(0, 12) for _ in range(random.randint(0, 10)))
        x = random.randint(-1, 13)
        lo, hi = sorted((random.randint(-1, 13), random.randint(-1, 13)))
        assert lower_bound(a, x) == sum(1 for v in a if v < x)
        assert upper_bound(a, x) == sum(1 for v in a if v <= x)
        assert contar_en_rango(a, lo, hi) == sum(1 for v in a if lo <= v <= hi)
        assert contiene(a, x) == (x in a)
        menores = [v for v in a if v <= x]
        mayores = [v for v in a if v >= x]
        assert mayor_menor_o_igual(a, x) == (max(menores) if menores else None)
        assert menor_mayor_o_igual(a, x) == (min(mayores) if mayores else None)
        b = a[:]
        insertar_ordenado(b, x)
        assert b == sorted(a + [x])
    print("OK")
