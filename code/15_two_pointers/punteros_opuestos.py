# Punteros opuestos: uno empieza al inicio, otro al final, y se
# acercan. Cuando usar: arreglo ORDENADO donde se busca un par (o
# particion) que cumpla una condicion con la suma/comparacion de los
# extremos -- el orden permite descartar la mitad del espacio de
# busqueda en cada paso, similar en espiritu a binary search.
#
# Otros usos tipicos: verificar si un string es palindromo, particion
# estilo "dutch flag", fusionar dos arreglos ordenados (la misma idea
# que usa merge de Merge Sort).


def two_sum_ordenado(arr, objetivo):
    izq, der = 0, len(arr) - 1
    while izq < der:
        s = arr[izq] + arr[der]
        if s == objetivo:
            return (izq, der)
        elif s < objetivo:
            izq += 1   # la suma es chica, hay que agrandarla
        else:
            der -= 1   # la suma es grande, hay que achicarla
    return None


if __name__ == "__main__":
    # --- ejemplo ---
    # arreglo ordenado: buscar un par con suma 15
    assert two_sum_ordenado([1, 2, 4, 7, 11, 15], 15) == (2, 4)   # 4 + 11
    assert two_sum_ordenado([1, 2, 3], 100) is None
    # --- fin ejemplo ---
    import random
    random.seed(3)
    for _ in range(100):
        n = random.randint(2, 15)
        arr = sorted(random.randint(1, 20) for _ in range(n))
        i, j = random.sample(range(n), 2)
        objetivo = arr[i] + arr[j]
        res = two_sum_ordenado(arr, objetivo)
        assert res is not None
        assert arr[res[0]] + arr[res[1]] == objetivo

    assert two_sum_ordenado([1, 2, 3, 100], 1000) is None
    print("OK")
