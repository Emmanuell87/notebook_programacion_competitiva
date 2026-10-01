# Z[i] = longitud del prefijo comun entre S y S[i:]. Busqueda de
# patrones (alternativa a KMP): para buscar 'patron' en 'texto', arma
# s = patron + '#' + texto (separador que no aparezca en ninguno) y
# calcula z_function(s); toda posicion i con z[i] == len(patron) es
# una ocurrencia.


def z_function(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def buscar_patron_con_z(texto, patron):
    s = patron + "#" + texto
    z = z_function(s)
    m = len(patron)
    ocurrencias = []
    for i in range(m + 1, len(s)):
        if z[i] == m:
            ocurrencias.append(i - m - 1)  # posicion 0-index en 'texto'
    return ocurrencias


if __name__ == "__main__":
    assert z_function("aaaa") == [0, 3, 2, 1]
    assert z_function("aabxaab") == [0, 1, 0, 0, 3, 1, 0]

    assert buscar_patron_con_z("ababcababc", "abc") == [2, 7]
    assert buscar_patron_con_z("aaaa", "aa") == [0, 1, 2]
    print("OK")
