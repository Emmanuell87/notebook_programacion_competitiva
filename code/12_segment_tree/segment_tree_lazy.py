# Cuando necesitas actualizar RANGOS COMPLETOS (no solo una posicion)
# eficientemente -- ej. "suma 5 a todo el rango [3,8]" en vez de
# actualizar de a uno. Sin lazy propagation, actualizar un rango
# entero costaria O(n) en el peor caso; con ella sigue siendo
# O(log n). range_add(l,r,val) suma val a cada elemento en [l,r];
# range_set(l,r,val) asigna val a todo el rango (sobrescribe);
# point_add/point_set son casos particulares con l=r=idx; query(l,r)
# da la suma en el rango.


class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.st = [0] * (4 * self.n)
        self.lazy_add = [0] * (4 * self.n)     # incremento pendiente
        self.lazy_set = [None] * (4 * self.n)  # asignacion pendiente
        self._build(1, 0, self.n - 1, arr)

    def _build(self, node, l, r, arr):
        if l == r:
            self.st[node] = arr[l]
        else:
            m = (l + r) // 2
            self._build(node * 2, l, m, arr)
            self._build(node * 2 + 1, m + 1, r, arr)
            self.st[node] = self.st[node * 2] + self.st[node * 2 + 1]

    def _apply_add(self, node, l, r, val):
        self.st[node] += val * (r - l + 1)
        if self.lazy_set[node] is not None:
            self.lazy_set[node] += val
        else:
            self.lazy_add[node] += val

    def _apply_set(self, node, l, r, val):
        self.st[node] = val * (r - l + 1)
        self.lazy_set[node] = val
        self.lazy_add[node] = 0

    def _push(self, node, l, r):
        if l == r:
            return
        m = (l + r) // 2
        if self.lazy_set[node] is not None:
            v = self.lazy_set[node]
            self._apply_set(node * 2, l, m, v)
            self._apply_set(node * 2 + 1, m + 1, r, v)
            self.lazy_set[node] = None
        if self.lazy_add[node] != 0:
            v = self.lazy_add[node]
            self._apply_add(node * 2, l, m, v)
            self._apply_add(node * 2 + 1, m + 1, r, v)
            self.lazy_add[node] = 0

    def _update_add(self, node, l, r, ql, qr, val):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self._apply_add(node, l, r, val)
            return
        self._push(node, l, r)
        m = (l + r) // 2
        self._update_add(node * 2, l, m, ql, qr, val)
        self._update_add(node * 2 + 1, m + 1, r, ql, qr, val)
        self.st[node] = self.st[node * 2] + self.st[node * 2 + 1]

    def _update_set(self, node, l, r, ql, qr, val):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self._apply_set(node, l, r, val)
            return
        self._push(node, l, r)
        m = (l + r) // 2
        self._update_set(node * 2, l, m, ql, qr, val)
        self._update_set(node * 2 + 1, m + 1, r, ql, qr, val)
        self.st[node] = self.st[node * 2] + self.st[node * 2 + 1]

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.st[node]
        self._push(node, l, r)
        m = (l + r) // 2
        return self._query(node * 2, l, m, ql, qr) + self._query(node * 2 + 1, m + 1, r, ql, qr)

    def range_add(self, l, r, val):
        # suma val a todos en [l, r]
        self._update_add(1, 0, self.n - 1, l, r, val)

    def range_set(self, l, r, val):
        # asigna val a todos en [l, r]
        self._update_set(1, 0, self.n - 1, l, r, val)

    def point_add(self, idx, val):
        self.range_add(idx, idx, val)

    def point_set(self, idx, value):
        self.range_set(idx, idx, value)

    def query(self, l, r):
        # suma en [l, r]
        return self._query(1, 0, self.n - 1, l, r)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    st = SegTree(arr)
    assert st.query(0, 4) == 15

    st.range_add(1, 3, 10)  # arr logico: [1,12,13,14,5]
    assert st.query(0, 4) == 15 + 30  # se sumo 10 a 3 elementos
    assert st.query(1, 1) == 12

    st.range_set(0, 4, 7)  # todo el arreglo pasa a valer 7
    assert st.query(0, 4) == 35
    assert st.query(2, 2) == 7

    st.point_add(0, 3)  # arr[0] = 7+3 = 10
    assert st.query(0, 0) == 10
    print("OK")
