# Busca UN subconjunto de arr (enteros positivos) cuya suma sea objetivo.
# Ordenar de mayor a menor y podar cuando lo que queda ya no alcanza
# acelera mucho el backtracking. Devuelve la lista elegida o None.


def subconjunto_con_suma(arr, objetivo):
    arr = sorted(arr, reverse=True)
    resto = [0] * (len(arr) + 1)   # resto[i] = suma de arr[i:]
    for i in range(len(arr) - 1, -1, -1):
        resto[i] = resto[i + 1] + arr[i]
    elegido = []

    def buscar(i, falta):
        if falta == 0:
            return True
        if i == len(arr) or resto[i] < falta:   # poda: aunque se tomen todos, no alcanza
            return False
        if arr[i] <= falta:
            elegido.append(arr[i])
            if buscar(i + 1, falta - arr[i]):
                return True
            elegido.pop()
        return buscar(i + 1, falta)

    return list(elegido) if buscar(0, objetivo) else None


if __name__ == "__main__":
    # --- ejemplo ---
    assert subconjunto_con_suma([3, 34, 4, 12, 5, 2], 9) == [5, 4]
    assert subconjunto_con_suma([3, 34, 4, 12, 5, 2], 30) is None   # no hay
    # --- fin ejemplo ---
    from itertools import combinations
    import random

    res = subconjunto_con_suma([3, 34, 4, 12, 5, 2], 9)
    assert res is not None and sum(res) == 9
    assert subconjunto_con_suma([3, 34, 4, 12, 5, 2], 30) is None
    assert subconjunto_con_suma([1, 2, 3], 0) == []

    random.seed(1)
    for _ in range(300):
        arr = [random.randint(1, 12) for _ in range(random.randint(0, 9))]
        objetivo = random.randint(0, 40)
        existe = any(sum(c) == objetivo for r in range(len(arr) + 1) for c in combinations(arr, r))
        res = subconjunto_con_suma(arr, objetivo)
        assert (res is not None) == existe, (arr, objetivo)
        if res is not None:
            assert sum(res) == objetivo
            resto = arr[:]
            for x in res:
                resto.remove(x)   # res debe ser sub-multiconjunto de arr
    print("OK")
