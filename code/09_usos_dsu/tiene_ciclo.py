# Usar DSU para determinar si un grafo (no dirigido) contiene ciclos.
# aristas = lista de (u, v) (sin peso); n = numero de nodos.
# Alternativa a ciclo_nodirigido (DFS, seccion de Recorridos) -- usa
# esta cuando ya tienes las aristas sueltas y no armaste una lista de
# adyacencia.


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


def tiene_ciclo(aristas, n):
    dsu = DSU(n)
    for u, v in aristas:
        if dsu.find(u) == dsu.find(v):
            return True  # Hay ciclo
        dsu.union(u, v)
    return False  # No hay ciclo


if __name__ == "__main__":
    # triangulo 0-1-2-0: tiene ciclo
    assert tiene_ciclo([(0, 1), (1, 2), (2, 0)], 3) is True
    # arbol 0-1, 1-2: sin ciclo
    assert tiene_ciclo([(0, 1), (1, 2)], 3) is False
    print("OK")
