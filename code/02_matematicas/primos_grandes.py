# Miller-Rabin (primalidad) y Pollard's Rho (factorizacion) para enteros
# grandes. La criba de Eratostenes solo alcanza hasta ~10^7-10^8 (por
# memoria); trial division O(sqrt n) se vuelve lento pasado ~10^12 o con
# muchas consultas. es_primo es DETERMINISTA para todo n < 3.3 * 10^24
# con estos testigos fijos (no hace falta aleatoriedad para primalidad).

import random
from math import gcd


def es_primo(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n):
    if n % 2 == 0:
        return 2
    while True:
        x = y = random.randint(2, n - 1)
        c = random.randint(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n:  # si d == n, el ciclo fue "malo": reintentar con otro c
            return d


def factorizar(n):
    # devuelve la lista de factores primos de n (con repeticion)
    if n == 1:
        return []
    if es_primo(n):
        return [n]
    d = pollard_rho(n)
    return factorizar(d) + factorizar(n // d)


if __name__ == "__main__":
    for p in [2, 3, 5, 7, 11, 97, 7919, 104729, 999999937, 2**31 - 1]:
        assert es_primo(p), p
    for c in [1, 4, 6, 100, 999999999, (2**31 - 1) * 3, 910222067227]:
        assert not es_primo(c), c

    for n in [12, 97, 999999999, 2**31 - 1, (2**31 - 1) * 3]:
        factores = factorizar(n)
        prod = 1
        for f in factores:
            assert es_primo(f)
            prod *= f
        assert prod == n, (n, factores)

    print("OK")
