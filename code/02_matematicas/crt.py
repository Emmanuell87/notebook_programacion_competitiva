# Teorema Chino del Resto: resuelve x = r1 (mod m1), x = r2 (mod m2),
# con m1, m2 NO necesariamente coprimos. Cuando el problema da varias
# restricciones de "resto al dividir por" y pide el menor x que las
# cumple todas a la vez (ciclos/calendarios con distinto periodo).
# Para combinar mas de 2 congruencias, aplicar crt repetidamente de a pares.
#
# NOTA: incluye su propia copia de egcd para que el archivo sea
# autocontenido (ver tambien egcd_modinv.py).


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def crt(r1, m1, r2, m2):
    g, p, q = egcd(m1, m2)
    if (r2 - r1) % g != 0:
        return None  # sin solucion
    lcm = m1 // g * m2
    x = (r1 + m1 * ((r2 - r1) // g * p % (m2 // g))) % lcm
    return x, lcm  # solucion x (mod lcm)


if __name__ == "__main__":
    # Dos satelites: A pasa cada 6h (primera vez en la hora 2),
    # B pasa cada 14h (primera vez en la hora 4). Primera coincidencia?
    x, lcm = crt(2, 6, 4, 14)
    assert (x, lcm) == (32, 42), (x, lcm)

    # caso sin solucion: x=0 mod 4 y x=1 mod 2 es imposible (paridad distinta)
    assert crt(0, 4, 1, 2) is None

    # caso coprimos simple: x=2 mod 3, x=3 mod 5 -> x=8 mod 15
    assert crt(2, 3, 3, 5) == (8, 15)
    print("OK")
