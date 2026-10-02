def permutaciones(arr):
    resultado = []
    actual = []
    usado = [False] * len(arr)

    def backtrack():
        if len(actual) == len(arr):
            resultado.append(actual[:])
            return
        for i in range(len(arr)):
            if usado[i]:
                continue
            usado[i] = True          # elegir
            actual.append(arr[i])
            backtrack()              # explorar
            actual.pop()             # deshacer
            usado[i] = False

    backtrack()
    return resultado


def combinaciones(n, k):
    # subconjuntos de tamano k de {1..n}, en orden creciente
    resultado = []
    actual = []

    def backtrack(inicio):
        if len(actual) == k:
            resultado.append(actual[:])
            return
        for x in range(inicio, n + 1):
            actual.append(x)
            backtrack(x + 1)
            actual.pop()

    backtrack(1)
    return resultado


def parentesis_balanceados(n):
    resultado = []

    def backtrack(actual, abiertos, cerrados):
        if len(actual) == 2 * n:
            resultado.append(actual)
            return
        if abiertos < n:
            backtrack(actual + "(", abiertos + 1, cerrados)
        if cerrados < abiertos:   # poda: nunca cerrar de mas
            backtrack(actual + ")", abiertos, cerrados + 1)

    backtrack("", 0, 0)
    return resultado


if __name__ == "__main__":
    # --- ejemplo ---
    assert permutaciones([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert combinaciones(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert parentesis_balanceados(2) == ["(())", "()()"]
    # --- fin ejemplo ---
    from itertools import combinations as comb_it, permutations as perm_it
    from math import comb

    assert permutaciones([1, 2, 3]) == [list(p) for p in perm_it([1, 2, 3])]
    assert combinaciones(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert parentesis_balanceados(2) == ["(())", "()()"]
    assert len(parentesis_balanceados(3)) == 5

    for n in range(0, 7):
        assert permutaciones(list(range(n))) == [list(p) for p in perm_it(range(n))]
        for k in range(0, n + 1):
            assert combinaciones(n, k) == [list(c) for c in comb_it(range(1, n + 1), k)]
        assert len(parentesis_balanceados(n)) == comb(2 * n, n) // (n + 1)
        assert all(s.count("(") == s.count(")") == n for s in parentesis_balanceados(n))
    print("OK")
