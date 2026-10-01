# Ecuaciones Diofanticas Lineales ax+by=c. Cuando piden enteros x,y que
# cumplan ax+by=c (ej.: "se puede pagar exactamente c con monedas de a
# y b, permitiendo cantidades negativas/prestadas?"). resolver_diofantica
# devuelve (x0, y0, g): UNA solucion particular y g=gcd(a,b); si
# c % g != 0 no hay solucion entera. La familia completa de soluciones
# es x = x0 + (b/g)*t, y = y0 - (a/g)*t para cualquier entero t.


def egcd(a, b):
    if b == 0:
        return (abs(a), 1 if a > 0 else -1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


def resolver_diofantica(a, b, c):
    g, x0, y0 = egcd(a, b)
    if c % g != 0:
        return None  # sin solucion
    k = c // g
    return (x0 * k, y0 * k, g)


if __name__ == "__main__":
    # 6x + 14y = 10 -> gcd(6,14)=2, 10%2==0, hay solucion
    res = resolver_diofantica(6, 14, 10)
    assert res is not None
    x0, y0, g = res
    assert 6 * x0 + 14 * y0 == 10, (x0, y0, g)

    # 4x + 6y = 5 -> gcd(4,6)=2, 5%2 != 0, sin solucion
    assert resolver_diofantica(4, 6, 5) is None

    # caso trivial
    res2 = resolver_diofantica(3, 5, 1)
    x0, y0, g = res2
    assert 3 * x0 + 5 * y0 == 1
    print("OK")
