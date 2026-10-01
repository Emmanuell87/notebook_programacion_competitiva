# Idea: un DFS registra CADA VISITA a un nodo (no solo la primera) en
# euler, junto con su profundidad en ese momento en profundidad. El
# LCA de u,v resulta ser el nodo con MENOR PROFUNDIDAD entre la
# primera aparicion de u y la primera de v en ese recorrido -- es
# decir, un RMQ (minimo en rango) sobre el arreglo profundidad,
# resuelto con Sparse Table. Diferencia con el SparseTableMin de
# Estructuras Adicionales: aqui la tabla guarda INDICES (para poder
# recuperar el nodo con euler[idx]), no solo el valor minimo.
#
# Uso: LCAEulerTour(n, grafo, raiz) preprocesa en O(n log n); luego
# .lca(u, v) responde en O(1).

import sys
sys.setrecursionlimit(10**6)  # el DFS puede ser profundo en arboles muy desbalanceados


class LCAEulerTour:
    def __init__(self, n, grafo, raiz=0):
        self.euler = []          # secuencia de nodos visitados (se repiten)
        self.profundidad = []    # profundidad de cada visita
        self.primera = [-1] * n  # primera posicion de cada nodo en 'euler'
        self._dfs(grafo, raiz, -1, 0)
        self._construir_sparse()

    def _dfs(self, grafo, u, padre, d):
        self.primera[u] = len(self.euler)
        self.euler.append(u)
        self.profundidad.append(d)
        for v in grafo[u]:
            if v != padre:
                self._dfs(grafo, v, u, d + 1)
                self.euler.append(u)
                self.profundidad.append(d)

    def _construir_sparse(self):
        m = len(self.profundidad)
        self.st = [list(range(m))]  # st[0][i] = i (indice del "minimo" de largo 1)
        j = 1
        while (1 << j) <= m:
            prev = self.st[-1]
            half = 1 << (j - 1)
            cur = []
            for i in range(m - (1 << j) + 1):
                a, b = prev[i], prev[i + half]
                cur.append(a if self.profundidad[a] <= self.profundidad[b] else b)
            self.st.append(cur)
            j += 1

    def _query_idx(self, l, r):  # indice del minimo en profundidad[l..r]
        k = (r - l + 1).bit_length() - 1
        a, b = self.st[k][l], self.st[k][r - (1 << k) + 1]
        return a if self.profundidad[a] <= self.profundidad[b] else b

    def lca(self, u, v):
        l, r = self.primera[u], self.primera[v]
        if l > r:
            l, r = r, l
        return self.euler[self._query_idx(l, r)]


if __name__ == "__main__":
    n = 7
    grafo = [[] for _ in range(n)]
    aristas = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for u, v in aristas:
        grafo[u].append(v)
        grafo[v].append(u)

    et = LCAEulerTour(n, grafo, raiz=0)
    assert et.lca(3, 4) == 1
    assert et.lca(3, 5) == 0
    assert et.lca(5, 6) == 2
    assert et.lca(1, 3) == 1
    print("OK")
