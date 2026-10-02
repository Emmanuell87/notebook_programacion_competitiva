from math import comb


def combos_con_repeticion(n, k):
    return comb(n + k - 1, k)


def estrellas_y_barras(S, m):
    return comb(S + m - 1, m - 1)


def estrellas_y_barras_con_minimos(S, minimos):
    # x_1 + ... + x_m = S con x_i >= minimos[i]: se sustituye y_i = x_i - minimos[i]
    m = len(minimos)
    resto = S - sum(minimos)
    return comb(resto + m - 1, m - 1) if resto >= 0 else 0


def catalan(n):
    return comb(2 * n, n) // (n + 1)


if __name__ == "__main__":
    # 3 tipos de fruta, eligiendo 2 con repeticion: (3,3),(3,2),(3,1),(2,2),(2,1),(1,1) = 6
    assert combos_con_repeticion(3, 2) == 6
    assert estrellas_y_barras(5, 3) == comb(5 + 3 - 1, 3 - 1)
    # x1 + x2 + x3 = 6 con cada x_i >= 1: C(5, 2) = 10
    assert estrellas_y_barras_con_minimos(6, [1, 1, 1]) == 10
    # x1 >= 2, x2 >= 0, x3 >= 1 con suma 6: se reduce a suma 3 con 3 variables = C(5, 2)
    assert estrellas_y_barras_con_minimos(6, [2, 0, 1]) == 10
    assert estrellas_y_barras_con_minimos(2, [1, 1, 1]) == 0  # no alcanza
    assert catalan(0) == 1
    assert catalan(3) == 5  # 5 formas de triangular un poligono de 5 lados / parentesis
    assert catalan(4) == 14
    print("OK")
