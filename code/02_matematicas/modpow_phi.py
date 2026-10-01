# modpow(a,e,m): a^e mod m en O(log e).
# modinv_prime(a,p): inverso de a modulo p, SOLO si p es primo (usa Fermat).
#   Si el modulo no es primo, usar modinv (egcd_modinv.py).
# phi(n): calcula la funcion totiente de Euler en O(sqrt(n)) factorizando n.


def modpow(a, e, m):
    r = 1 % m
    a %= m
    while e > 0:
        if e & 1:
            r = (r * a) % m
        a = (a * a) % m
        e >>= 1
    return r


def modinv_prime(a, p):  # p primo
    return modpow(a, p - 2, p)


def phi(n):
    r = n
    x = n
    f = 2
    while f * f <= x:
        if x % f == 0:
            while x % f == 0:
                x //= f
            r -= r // f
        f += 1
    if x > 1:
        r -= r // x
    return r


if __name__ == "__main__":
    assert modpow(2, 10, 1000) == 24
    assert modpow(3, 0, 5) == 1
    assert modinv_prime(3, 7) == 5  # 3*5=15 = 2*7+1
    assert (3 * modinv_prime(3, 7)) % 7 == 1
    assert phi(1) == 1
    assert phi(9) == 6   # 1,2,4,5,7,8
    assert phi(36) == 12
    assert phi(13) == 12  # primo
    print("OK")
