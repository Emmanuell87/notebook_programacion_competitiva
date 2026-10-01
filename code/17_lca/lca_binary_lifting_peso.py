# Extender Binary Lifting con informacion extra en el camino. Cada
# salto up[k][v] representa un "bloque" de 2^k aristas consecutivas.
# Si ademas guardas, para ese mismo bloque, un dato agregado (peso
# maximo, suma, xor, gcd, ...), puedes responder consultas sobre el
# CAMINO COMPLETO entre u y v usando la misma descomposicion en saltos
# que ya usa lca. A diferencia de la Sparse Table (que solo sirve para
# operaciones idempotentes como min/max/gcd, porque sus rangos se
# solapan a proposito), aqui los bloques son DISJUNTOS -- por eso esto
# funciona tambien con suma o xor, no solo con min/max.
#
# Ejemplo: peso maximo de arista en el camino u->v. grafo[u] es una
# lista de (vecino, peso). Para adaptarlo a otra cosa: cambia
# max_peso por lo que necesites (suma_peso, xor_peso, min_peso, ...) y
# reemplaza cada max(...) por la operacion correspondiente (+, ^, min,
# ...) tanto en la construccion como en query.

from collections import deque


class LCABinaryLiftingConPeso:
    def __init__(self, n, grafo, raiz=0):
        # grafo[u] = lista de (v, peso) -- arbol ponderado
        self.n = n
        self.LOG = max(1, n.bit_length())
        self.up = [[-1] * n for _ in range(self.LOG)]
        self.max_peso = [[0] * n for _ in range(self.LOG)]
        self.depth = [0] * n
        self._bfs(grafo, raiz)
        for k in range(1, self.LOG):
            for v in range(n):
                mid = self.up[k - 1][v]
                if mid != -1:
                    self.up[k][v] = self.up[k - 1][mid]
                    self.max_peso[k][v] = max(self.max_peso[k - 1][v], self.max_peso[k - 1][mid])

    def _bfs(self, grafo, raiz):
        visitado = [False] * self.n
        visitado[raiz] = True
        self.up[0][raiz] = raiz
        q = deque([raiz])
        while q:
            u = q.popleft()
            for v, w in grafo[u]:
                if not visitado[v]:
                    visitado[v] = True
                    self.depth[v] = self.depth[u] + 1
                    self.up[0][v] = u
                    self.max_peso[0][v] = w
                    q.append(v)

    def query(self, u, v):
        # devuelve (lca, peso_maximo_en_el_camino_u_v)
        peso_max = 0
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                peso_max = max(peso_max, self.max_peso[i][u])
                u = self.up[i][u]
        if u == v:
            return u, peso_max
        for i in reversed(range(self.LOG)):
            if self.up[i][u] != self.up[i][v]:
                peso_max = max(peso_max, self.max_peso[i][u], self.max_peso[i][v])
                u = self.up[i][u]
                v = self.up[i][v]
        peso_max = max(peso_max, self.max_peso[0][u], self.max_peso[0][v])
        return self.up[0][u], peso_max


if __name__ == "__main__":
    # Arbol: 0 raiz; hijos [1,2]; 1->[3,4]; 2->[5,6]
    n = 7
    grafo = [[] for _ in range(n)]
    aristas = [(0, 1, 5), (0, 2, 3), (1, 3, 2), (1, 4, 7), (2, 5, 4), (2, 6, 6)]
    for u, v, w in aristas:
        grafo[u].append((v, w))
        grafo[v].append((u, w))

    st = LCABinaryLiftingConPeso(n, grafo, raiz=0)

    lca, mx = st.query(3, 4)  # 3->1(2)->4(7): max=7, lca=1
    assert (lca, mx) == (1, 7), (lca, mx)

    lca, mx = st.query(3, 5)  # 3->1(2)->0(5)->2(3)->5(4): max=5, lca=0
    assert (lca, mx) == (0, 5), (lca, mx)

    lca, mx = st.query(1, 6)  # 1->0(5)->2(3)->6(6): max=6, lca=0
    assert (lca, mx) == (0, 6), (lca, mx)

    lca, mx = st.query(4, 4)  # nodo consigo mismo
    assert (lca, mx) == (4, 0), (lca, mx)
    print("OK")
