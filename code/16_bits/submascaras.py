# Problemas de DP sobre subconjuntos / bitmask donde necesitas
# recorrer todos los subconjuntos de un conjunto de n elementos,
# representados como bits de un entero (mascara). Recorrer TODAS las
# submascaras de TODAS las mascaras es O(3^n) en total (no O(4^n)
# como pareceria) -- cada elemento esta en uno de tres estados: fuera
# de la mascara, dentro de la mascara pero fuera de la submascara, o
# dentro de ambas.


def submascaras(mask):
    sub = mask
    while True:
        yield sub          # procesar sub aqui
        if sub == 0:
            break
        sub = (sub - 1) & mask


if __name__ == "__main__":
    # --- ejemplo ---
    assert list(submascaras(0b101)) == [0b101, 0b100, 0b001, 0b000]
    # --- fin ejemplo ---
    for mask in [0, 1, 5, 6, 7, 13, 255]:
        subs = list(submascaras(mask))
        esperado = [s for s in range(mask, -1, -1) if (s & mask) == s]
        assert set(subs) == set(esperado), (mask, subs, esperado)
        assert len(subs) == len(set(subs))  # sin duplicados
        assert len(subs) == (1 << bin(mask).count('1'))
    print("OK")
