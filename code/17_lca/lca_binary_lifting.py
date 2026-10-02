# Idea: precalcular, para cada nodo, quien es su ancestro 2^k para
# k=0,1,2,... (up[k][v]). Para subir d niveles desde un nodo, se
# descompone d en binario y se dan esos "saltos". Para el LCA: primero
# se nivela el mas profundo de los dos al nivel del otro, y luego se
# suben ambos juntos a saltos decrecientes mientras sigan siendo
# distintos.
#
# Uso: LCABinaryLifting(n, grafo, raiz) preprocesa en O(n log n);
# luego .lca(u, v) responde en O(log n).

from collections import deque


class LCABinaryLifting:
    def __init__(self, n, grafo, raiz=0):
        self.n = n
        self.LOG = max(1, n.bit_length())
        self.up = [[-1] * n for _ in range(self.LOG)]
        self.depth = [0] * n
        self._bfs(grafo, raiz)
        for k in range(1, self.LOG):
            for v in range(n):
                if self.up[k - 1][v] != -1:
                    self.up[k][v] = self.up[k - 1][self.up[k - 1][v]]

    def _bfs(self, grafo, raiz):
        visitado = [False] * self.n
        visitado[raiz] = True
        self.up[0][raiz] = raiz  # la raiz es su propio padre (evita -1 en los saltos)
        q = deque([raiz])
        while q:
            u = q.popleft()
            for v in grafo[u]:
                if not visitado[v]:
                    visitado[v] = True
                    self.depth[v] = self.depth[u] + 1
                    self.up[0][v] = u
                    q.append(v)

    def kth_ancestor(self, v, k):
        # sube k niveles desde v (util tambien fuera del contexto de LCA)
        for i in range(self.LOG):
            if k & (1 << i):
                v = self.up[i][v]
        return v

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        u = self.kth_ancestor(u, self.depth[u] - self.depth[v])
        if u == v:
            return u
        for i in reversed(range(self.LOG)):
            if self.up[i][u] != self.up[i][v]:
                u = self.up[i][u]
                v = self.up[i][v]
        return self.up[0][u]


if __name__ == "__main__":
    # --- ejemplo ---
    # arbol de 7 nodos (0-indexado): 0 es raiz, hijos [1,2];
    # 1 tiene hijos [3,4]; 2 tiene hijos [5,6]
    n = 7
    grafo = [[] for _ in range(n)]
    aristas = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for u, v in aristas:
        grafo[u].append(v)
        grafo[v].append(u)

    bl = LCABinaryLifting(n, grafo, raiz=0)
    assert bl.lca(3, 4) == 1
    assert bl.lca(3, 5) == 0
    assert bl.lca(5, 6) == 2
    assert bl.lca(1, 3) == 1  # ancestro directo
    assert bl.kth_ancestor(3, 2) == 0  # 3 -> 1 -> 0
    # --- fin ejemplo ---
    print("OK")
