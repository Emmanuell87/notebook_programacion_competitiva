# Trucos de un solo bit (i = posicion del bit, desde 0 = el menos
# significativo):
#   obtener_bit  = (n >> i) & 1
#   encender_bit = n | (1 << i)
#   apagar_bit   = n & ~(1 << i)
#   alternar_bit = n ^ (1 << i)          # togglea el bit i
#
# n & (n-1) apaga el bit menos significativo que esta encendido (ej.
# 1100 -> 1000). Es la idea detras del recorrido de Fenwick.
# n & -n aisla ese mismo bit menos significativo encendido (ej. n=12
# (1100) da 4 (0100)). Tambien se usa en Fenwick, para saber cuanto
# "saltar".
# n.bit_length() da la posicion del bit mas significativo +1 (se usa
# en Sparse Table y Binary Lifting para calcular log2(n)).


def es_potencia_de_2(n):
    return n > 0 and (n & (n - 1)) == 0


def contar_bits(n):
    return bin(n).count('1')  # o n.bit_count() desde Python 3.10


if __name__ == "__main__":
    # trucos de un solo bit
    n, i = 0b1010, 1
    assert (n >> i) & 1 == 1          # obtener_bit
    assert n | (1 << 2) == 0b1110     # encender_bit
    assert n & ~(1 << 1) == 0b1000    # apagar_bit
    assert n ^ (1 << 1) == 0b1000     # alternar_bit

    for valor in [1, 2, 3, 4, 8, 15, 16, 1024, 1023]:
        assert es_potencia_de_2(valor) == (valor > 0 and (valor & (valor - 1)) == 0)
    assert contar_bits(7) == 3   # 111
    assert contar_bits(8) == 1   # 1000

    assert (12 & -12) == 4    # 1100 -> aisla 0100
    assert (12 & (12 - 1)) == 8  # 1100 -> apaga el menos significativo -> 1000
    print("OK")
