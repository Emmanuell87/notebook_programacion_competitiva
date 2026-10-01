def pick_area(I, B):
    return I + B / 2 - 1


def heron(a, b, c):
    s = (a + b + c) / 2
    if a + b <= c or a + c <= b or b + c <= a:
        return 0.0
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def es_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a


if __name__ == "__main__":
    assert pick_area(4, 4) == 4 + 2 - 1
    # triangulo 3-4-5 (rectangulo): area = 6
    assert abs(heron(3, 4, 5) - 6.0) < 1e-9
    assert heron(1, 1, 10) == 0.0  # no forma triangulo
    assert es_triangulo(3, 4, 5) is True
    assert es_triangulo(1, 1, 10) is False
    print("OK")
