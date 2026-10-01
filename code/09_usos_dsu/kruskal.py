# Arbol de Expansion Minima (MST) - Kruskal. Construir un arbol que
# conecte todos los nodos con el costo minimo. n = numero de nodos
# (0-indexados); aristas = lista de (u, v, peso). Devuelve
# (mst_peso, mst_aristas). Conviene sobre Prim cuando el grafo es
# disperso (pocas aristas), porque el costo dominante es ordenar las
# aristas: O(E log E).
#
# NOTA: incluye su propia copia de DSU para que el archivo sea
# autocontenido (ver tambien 08_dsu/dsu.py).


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]


def kruskal(n, aristas):
    dsu = DSU(n)
    aristas.sort(key=lambda x: x[2])  # Ordenar por peso
    mst_peso = 0
    mst_aristas = []

    for u, v, peso in aristas:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst_peso += peso
            mst_aristas.append((u, v))

    return mst_peso, mst_aristas


if __name__ == "__main__":
    # mismo grafo que prim.py: MST esperado 0-2(1), 1-2(2), 1-3(5) = peso 8
    aristas = [(0, 1, 4), (0, 2, 1), (1, 2, 2), (1, 3, 5), (2, 3, 8)]
    peso, mst = kruskal(4, aristas)
    assert peso == 8, peso
    assert len(mst) == 3
    print("OK")
