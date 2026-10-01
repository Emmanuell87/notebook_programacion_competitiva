# Buscar todas las ocurrencias de un patron p en un texto s en
# O(|s|+|p|), usando una tabla de fallos (failure function) que evita
# retroceder en el texto. lps[i] es el corazon del algoritmo --
# precalcula cuanto se puede "saltar" sin volver a comparar desde cero
# cuando hay un mismatch.


def construir_lps(p):
    # lps[i] = longitud del prefijo propio mas largo de p[0..i]
    # que tambien es sufijo de p[0..i]
    n = len(p)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_buscar(texto, patron):
    n, m = len(texto), len(patron)
    if m == 0:
        return []
    lps = construir_lps(patron)
    ocurrencias = []
    i = j = 0  # i: texto, j: patron
    while i < n:
        if texto[i] == patron[j]:
            i += 1
            j += 1
            if j == m:
                ocurrencias.append(i - j)  # posicion 0-index del match
                j = lps[j - 1]
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
    return ocurrencias


if __name__ == "__main__":
    assert kmp_buscar("ababcababc", "abc") == [2, 7]
    assert kmp_buscar("aaaa", "aa") == [0, 1, 2]
    assert kmp_buscar("abc", "xyz") == []
    assert construir_lps("aabaaab") == [0, 1, 0, 1, 2, 2, 3]
    print("OK")
