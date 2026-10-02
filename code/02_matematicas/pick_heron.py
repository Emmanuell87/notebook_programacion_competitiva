from math import gcd


def pick_area(I, B):
    return I + B / 2 - 1


def puntos_en_borde(poligono):
    # B = suma de gcd(|dx|, |dy|) sobre cada arista (vertices enteros)
    n = len(poligono)
    total = 0
    for i in range(n):
        x1, y1 = poligono[i]
        x2, y2 = poligono[(i + 1) % n]
        total += gcd(abs(x2 - x1), abs(y2 - y1))
    return total


def puntos_interiores(poligono):
    # despeja I en Pick: I = A - B/2 + 1, con 2A por la formula del cordon
    n = len(poligono)
    doble_area = 0
    for i in range(n):
        x1, y1 = poligono[i]
        x2, y2 = poligono[(i + 1) % n]
        doble_area += x1 * y2 - x2 * y1
    return (abs(doble_area) - puntos_en_borde(poligono) + 2) // 2


def heron(a, b, c):
    s = (a + b + c) / 2
    if a + b <= c or a + c <= b or b + c <= a:
        return 0.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def es_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a


if __name__ == "__main__":
    assert pick_area(4, 4) == 4 + 2 - 1
    # rectangulo 4 x 3: borde 14, interior 3 * 2 = 6
    rect = [(0, 0), (4, 0), (4, 3), (0, 3)]
    assert puntos_en_borde(rect) == 14
    assert puntos_interiores(rect) == 6
    # triangulo (0,0), (4,0), (0,4): borde 12, interior 3
    tri = [(0, 0), (4, 0), (0, 4)]
    assert puntos_en_borde(tri) == 12
    assert puntos_interiores(tri) == 3
    assert pick_area(puntos_interiores(tri), puntos_en_borde(tri)) == 8
    # triangulo 3-4-5 (rectangulo): area = 6
    assert abs(heron(3, 4, 5) - 6.0) < 1e-9
    assert heron(1, 1, 10) == 0.0  # no forma triangulo
    assert es_triangulo(3, 4, 5) is True
    assert es_triangulo(1, 1, 10) is False
    print("OK")
