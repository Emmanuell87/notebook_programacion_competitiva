# i = posicion del bit, desde 0 = el menos significativo.


def obtener_bit(n, i):
    # devuelve el bit i de n (0 o 1)
    return (n >> i) & 1


def encender_bit(n, i):
    # pone el bit i en 1
    return n | (1 << i)


def apagar_bit(n, i):
    # pone el bit i en 0
    return n & ~(1 << i)


def alternar_bit(n, i):
    # invierte el bit i (0 -> 1, 1 -> 0)
    return n ^ (1 << i)


def apagar_bit_mas_bajo(n):
    # 1100 -> 1000. Es la idea detras del recorrido de Fenwick.
    return n & (n - 1)


def aislar_bit_mas_bajo(n):
    # 1100 -> 0100. En Fenwick indica cuanto "saltar".
    return n & -n


def es_potencia_de_2(n):
    # una potencia de 2 tiene un solo bit en 1
    return n > 0 and (n & (n - 1)) == 0


def contar_bits(n):
    # cantidad de bits en 1 (popcount); n.bit_count() desde Python 3.10
    return bin(n).count('1')


def posicion_bit_mas_alto(n):
    # n.bit_length() = esa posicion + 1; se usa en Sparse Table y
    # Binary Lifting para calcular log2(n).
    return n.bit_length() - 1


if __name__ == "__main__":
    n = 0b1010
    assert obtener_bit(n, 1) == 1
    assert obtener_bit(n, 0) == 0
    assert encender_bit(n, 2) == 0b1110
    assert apagar_bit(n, 1) == 0b1000
    assert alternar_bit(n, 1) == 0b1000
    assert alternar_bit(n, 0) == 0b1011

    assert apagar_bit_mas_bajo(0b1100) == 0b1000
    assert aislar_bit_mas_bajo(0b1100) == 0b0100
    assert aislar_bit_mas_bajo(12) == 4

    for valor in [1, 2, 3, 4, 8, 15, 16, 1024, 1023]:
        assert es_potencia_de_2(valor) == (valor > 0 and (valor & (valor - 1)) == 0)
    assert not es_potencia_de_2(0)
    assert contar_bits(7) == 3   # 111
    assert contar_bits(8) == 1   # 1000

    assert posicion_bit_mas_alto(1) == 0
    assert posicion_bit_mas_alto(8) == 3
    assert posicion_bit_mas_alto(1000) == 9

    # contra una implementacion directa
    for x in range(1, 2000):
        assert aislar_bit_mas_bajo(x) == min(1 << b for b in range(12) if x >> b & 1)
        assert apagar_bit_mas_bajo(x) == x - aislar_bit_mas_bajo(x)
        assert posicion_bit_mas_alto(x) == max(b for b in range(12) if x >> b & 1)
        for i in range(11):
            assert obtener_bit(encender_bit(x, i), i) == 1
            assert obtener_bit(apagar_bit(x, i), i) == 0
            assert alternar_bit(alternar_bit(x, i), i) == x
    print("OK")
