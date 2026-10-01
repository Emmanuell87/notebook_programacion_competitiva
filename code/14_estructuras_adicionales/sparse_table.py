# Igual que prefix sums: el arreglo NO CAMBIA (estatico), pero aqui la
# operacion es min (o max/gcd -- cualquier operacion IDEMPOTENTE,
# donde repetir un elemento no afecta el resultado, a diferencia de la
# suma). Preprocesamiento O(n log n), consulta O(1) -- mas rapido que
# Segment Tree, pero NO admite actualizaciones.
#
# SparseTableMin(arr) recibe la lista; query(l, r) da el minimo en
# [l,r] inclusive, 0-indexado.


class SparseTableMin:
    def __init__(self, arr):
        self.n = len(arr)
        self.K = self.n.bit_length()
        self.st = [arr[:]]
        j = 1
        while (1 << j) <= self.n:
            prev = self.st[-1]
            cur = [min(prev[i], prev[i + (1 << (j - 1))])
                   for i in range(self.n - (1 << j) + 1)]
            self.st.append(cur)
            j += 1

    def query(self, l, r):  # inclusive
        k = (r - l + 1).bit_length() - 1
        return min(self.st[k][l], self.st[k][r - (1 << k) + 1])


if __name__ == "__main__":
    arr = [5, 2, 4, 7, 1, 3, 6]
    st = SparseTableMin(arr)
    assert st.query(1, 4) == 1   # min(2,4,7,1)
    assert st.query(0, 2) == 2   # min(5,2,4)
    assert st.query(0, 6) == 1   # min de todo el arreglo
    assert st.query(3, 3) == 7   # un solo elemento
    print("OK")
