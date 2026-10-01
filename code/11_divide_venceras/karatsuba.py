# Multiplicar dos numeros grandes en menos de O(n^2).


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a, b = divmod(x, 10 ** m)
    c, d = divmod(y, 10 ** m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * 10 ** (2 * m) + ad_plus_bc * 10 ** m + bd


if __name__ == "__main__":
    assert karatsuba(1234, 5678) == 1234 * 5678
    assert karatsuba(123456789, 987654321) == 123456789 * 987654321
    assert karatsuba(5, 7) == 35
    print("OK")
