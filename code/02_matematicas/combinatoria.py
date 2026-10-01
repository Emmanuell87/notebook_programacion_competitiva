from math import comb


def combos_con_repeticion(n, k):
    return comb(n + k - 1, k)


def estrellas_y_barras(S, m):
    return comb(S + m - 1, m - 1)


def catalan(n):
    return comb(2 * n, n) // (n + 1)


if __name__ == "__main__":
    # 3 frutas de tipos, eligiendo 2 con repeticion: (3,3),(3,2),(3,1),(2,2),(2,1),(1,1) = 6
    assert combos_con_repeticion(3, 2) == 6
    assert estrellas_y_barras(5, 3) == comb(5 + 3 - 1, 3 - 1)
    assert catalan(0) == 1
    assert catalan(3) == 5  # 5 formas de triangular un poligono de 5 lados / parentesis
    assert catalan(4) == 14
    print("OK")
