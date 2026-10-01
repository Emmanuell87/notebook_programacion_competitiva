# Estructura eficiente para consultas y actualizaciones en rangos.
# O(log n) para ambos procesos. arr = lista inicial (0-indexada).
# update(idx, value) asigna arr[idx] = value; query(l, r) responde la
# operacion agregada en el rango [l, r] INCLUSIVE, 0-indexado.
#
# Para adaptarlo a otra operacion (minimo, maximo, gcd, etc.) solo
# cambia neutral() (0 para suma, +inf para minimo, -inf para maximo,
# 0 para gcd) y oper(a,b) (la operacion en si, ej. min(a,b)).


class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 4 * self.n
        self.st = [self.neutral()] * self.size
        self._build(1, 0, self.n - 1, arr)

    def neutral(self):
        return 0

    def oper(self, a, b):
        return a + b

    def _build(self, node, l, r, arr):
        if l == r:
            self.st[node] = arr[l]
        else:
            m = (l + r) // 2
            self._build(2 * node, l, m, arr)
            self._build(2 * node + 1, m + 1, r, arr)
            self.st[node] = self.oper(self.st[2 * node], self.st[2 * node + 1])

    def _update(self, node, l, r, idx, value):
        if l == r:
            self.st[node] = value
        else:
            m = (l + r) // 2
            if idx <= m:
                self._update(2 * node, l, m, idx, value)
            else:
                self._update(2 * node + 1, m + 1, r, idx, value)
            self.st[node] = self.oper(self.st[2 * node], self.st[2 * node + 1])

    def _query(self, node, l, r, ql, qr):
        if qr < l or ql > r:
            return self.neutral()
        if ql <= l and r <= qr:
            return self.st[node]
        m = (l + r) // 2
        left = self._query(2 * node, l, m, ql, qr)
        right = self._query(2 * node + 1, m + 1, r, ql, qr)
        return self.oper(left, right)

    def update(self, idx, value):
        # asigna arr[idx] = value
        self._update(1, 0, self.n - 1, idx, value)

    def query(self, l, r):
        # suma en [l, r]
        return self._query(1, 0, self.n - 1, l, r)


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegTree(arr)
    assert st.query(0, 5) == sum(arr)
    assert st.query(1, 3) == 3 + 5 + 7
    st.update(1, 100)  # arr pasa a ser [1,100,5,7,9,11]
    assert st.query(0, 1) == 1 + 100
    assert st.query(2, 5) == 5 + 7 + 9 + 11
    print("OK")
