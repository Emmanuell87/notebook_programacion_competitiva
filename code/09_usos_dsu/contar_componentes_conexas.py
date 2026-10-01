# Determinar cuantas componentes conexas hay en un grafo no dirigido
# usando DSU. aristas = lista de (u, v); n = numero de nodos (los
# aislados, sin aristas, cuentan como su propia componente).


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


def contar_componentes_conexas(aristas, n):
    dsu = DSU(n)
    for u, v in aristas:
        dsu.union(u, v)

    componentes = set()
    for i in range(n):
        componentes.add(dsu.find(i))

    return len(componentes)


if __name__ == "__main__":
    # {0,1,2}, {3,4}, {5} aislado
    aristas = [(0, 1), (1, 2), (3, 4)]
    assert contar_componentes_conexas(aristas, 6) == 3
    assert contar_componentes_conexas([], 4) == 4  # todos aislados
    print("OK")
