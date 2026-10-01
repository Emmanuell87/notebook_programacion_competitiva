# Inverso modular general (funciona aunque m no sea primo, siempre que
# gcd(a,m)=1), usando Euclides extendido. egcd(a,b) resuelve a*x+b*y=gcd(a,b)
# y tambien se reutiliza en crt.py.


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)  # (gcd, x, y) t.q. a*x + b*y = gcd
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def modinv(a, m):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        return None  # no existe inverso (a y m no son coprimos)
    return x % m


if __name__ == "__main__":
    g, x, y = egcd(6, 14)
    assert 6 * x + 14 * y == g

    assert modinv(3, 11) == 4  # 3*4=12 = 1 mod 11
    assert (3 * modinv(3, 11)) % 11 == 1
    assert modinv(4, 8) is None  # gcd(4,8)=4 != 1, no existe inverso

    # modulo no primo: modinv_prime fallaria aqui, modinv si funciona
    assert modinv(3, 10) == 7  # 3*7=21 = 1 mod 10
    print("OK")
