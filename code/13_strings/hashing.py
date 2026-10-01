# Comparar substrings en O(1) tras un preprocesamiento O(n), util para
# buscar patrones, substrings repetidos, o comparar igualdad de
# rangos. Se recomienda DOBLE HASH (dos modulos/bases distintos) para
# evitar colisiones adversarias.


class HashCadena:
    def __init__(self, s, base=131, mod=10**9 + 7):
        self.n = len(s)
        self.mod = mod
        self.pot = [1] * (self.n + 1)
        self.pref = [0] * (self.n + 1)
        for i, c in enumerate(s):
            self.pot[i + 1] = (self.pot[i] * base) % mod
            self.pref[i + 1] = (self.pref[i] * base + ord(c)) % mod

    def hash_rango(self, l, r):  # hash de s[l:r] (r exclusivo), 0-index
        return (self.pref[r] - self.pref[l] * self.pot[r - l]) % self.mod


# Uso tipico: comparar si s[l1:r1] == s[l2:r2] en O(1) comparando
# hash_rango(l1, r1) == hash_rango(l2, r2) (idealmente con dos
# instancias de HashCadena con base/mod distintos)


def rabin_karp_buscar(texto, patron, base=131, mod=10**9 + 7):
    # busqueda de patron con hash rodante; compara directo como
    # respaldo ante colision
    n, m = len(texto), len(patron)
    if m > n:
        return []
    h_patron = 0
    h_texto = 0
    potencia = 1
    for i in range(m):
        h_patron = (h_patron * base + ord(patron[i])) % mod
        h_texto = (h_texto * base + ord(texto[i])) % mod
        if i < m - 1:
            potencia = (potencia * base) % mod

    ocurrencias = []
    for i in range(n - m + 1):
        if h_texto == h_patron and texto[i:i + m] == patron:  # verificacion evita falsos positivos
            ocurrencias.append(i)
        if i + m < n:
            h_texto = ((h_texto - ord(texto[i]) * potencia) * base + ord(texto[i + m])) % mod
    return ocurrencias


if __name__ == "__main__":
    s = "abracadabra"
    hc = HashCadena(s)
    # s[0:4]="abra", s[7:11]="abra" -> mismo hash
    assert hc.hash_rango(0, 4) == hc.hash_rango(7, 11)
    assert hc.hash_rango(0, 4) != hc.hash_rango(1, 5)  # "abra" != "brac"

    assert rabin_karp_buscar("ababcababc", "abc") == [2, 7]
    assert rabin_karp_buscar("aaaa", "aa") == [0, 1, 2]
    assert rabin_karp_buscar(s, "abra") == [0, 7]
    print("OK")
