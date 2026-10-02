from math import comb, gcd, isqrt, lcm, perm, prod

# isqrt, comb, perm: Python 3.8+. lcm (y gcd con varios argumentos): 3.9+.


def raiz_entera(n):
    # floor(sqrt(n)) exacto. int(n ** 0.5) falla con numeros grandes
    # por el error de los float.
    return isqrt(n)


def es_cuadrado_perfecto(n):
    r = isqrt(n)
    return r * r == n


def techo_division(a, b):
    # ceil(a / b) solo con enteros (b > 0), sin pasar por float
    return -(-a // b)


def combinaciones(n, k):
    # C(n, k) exacto, con enteros arbitrariamente grandes
    return comb(n, k)


def arreglos_ordenados(n, k):
    # P(n, k) = n! / (n - k)!
    return perm(n, k)


def mcm_y_mcd(numeros):
    return lcm(*numeros), gcd(*numeros)


def producto(numeros):
    return prod(numeros)   # prod([]) == 1


if __name__ == "__main__":
    from fractions import Fraction
    from math import ceil, factorial

    # --- ejemplo ---
    assert raiz_entera(99) == 9 and raiz_entera(100) == 10
    # con float falla: (10**18 - 1) ** 0.5 se redondea a 10**9
    assert raiz_entera(10 ** 18 - 1) == 10 ** 9 - 1
    assert int((10 ** 18 - 1) ** 0.5) == 10 ** 9
    assert es_cuadrado_perfecto(144) is True and es_cuadrado_perfecto(145) is False
    assert techo_division(7, 2) == 4 and techo_division(8, 2) == 4
    assert combinaciones(5, 2) == 10 and arreglos_ordenados(5, 2) == 20
    assert mcm_y_mcd([4, 6, 10]) == (60, 2)
    assert producto([2, 3, 4]) == 24 and producto([]) == 1
    # --- fin ejemplo ---

    for n in range(0, 20000):
        r = raiz_entera(n)
        assert r * r <= n < (r + 1) * (r + 1)
        assert es_cuadrado_perfecto(n) == (int(n ** 0.5) ** 2 == n)   # exacto con numeros chicos
    for a in range(-30, 31):
        for b in range(1, 12):
            assert techo_division(a, b) == ceil(Fraction(a, b))
    for n in range(0, 15):
        for k in range(0, n + 1):
            assert combinaciones(n, k) == factorial(n) // (factorial(k) * factorial(n - k))
            assert arreglos_ordenados(n, k) == factorial(n) // factorial(n - k)
    big = 10 ** 40 + 12345
    assert raiz_entera(big * big) == big
    print("OK")
