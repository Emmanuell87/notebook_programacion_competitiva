from collections import Counter


def factorizacion(n):
    factores = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factores.append(d)
            n //= d
        d += 1
    if n > 1:
        factores.append(n)
    return factores


def factorizacion_con_exponentes(n):
    return dict(Counter(factorizacion(n)))


if __name__ == "__main__":
    assert factorizacion(1) == []
    assert factorizacion(2) == [2]
    assert factorizacion(360) == [2, 2, 2, 3, 3, 5]
    assert factorizacion(97) == [97]
    assert factorizacion_con_exponentes(360) == {2: 3, 3: 2, 5: 1}

    def es_primo(x):
        return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))

    for n in range(1, 3000):
        fs = factorizacion(n)
        prod = 1
        for f in fs:
            assert es_primo(f)
            prod *= f
        assert prod == n
        assert fs == sorted(fs)
    print("OK")
