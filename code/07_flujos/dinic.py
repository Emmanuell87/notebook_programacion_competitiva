# Maximo Flujo, mas rapido que Edmonds-Karp. edmonds_karp es O(V E^2)
# -- con grafos grandes (V~10^4, E~10^5) puede dar TLE. Dinic es
# O(V^2 E) en el peor caso pero muchisimo mas rapido en la practica, y
# O(E sqrt(V)) en grafos de capacidad unitaria/bipartitos (por eso
# Hopcroft-Karp es esencialmente un caso particular de Dinic para
# matching). Idea: en vez de buscar un solo camino aumentante por BFS
# (como Edmonds-Karp), construye un "grafo de niveles" con BFS y
# satura TODOS los caminos aumentantes de ese grafo con un DFS
# (blocking flow) antes de rehacer el BFS.
#
# Dinic(n) crea el grafo (n nodos, 0-indexados); agregar_arista(u,v,cap)
# agrega arista dirigida u->v con capacidad cap (mas su residual
# inversa con capacidad 0); max_flow(s,t) devuelve el flujo maximo.
# Truco: las aristas se guardan en pares consecutivos (directa en
# indice par, residual en el impar), asi eid^1 da la arista opuesta.

from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]  # adj[u] = indices de aristas que salen de u
        self.to = []    # destino de cada arista (por indice)
        self.cap = []   # capacidad restante de cada arista (por indice)

    def agregar_arista(self, u, v, cap):
        self.adj[u].append(len(self.to)); self.to.append(v); self.cap.append(cap)
        self.adj[v].append(len(self.to)); self.to.append(u); self.cap.append(0)  # residual inversa

    def _bfs(self, s, t):
        self.nivel = [-1] * self.n
        self.nivel[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for eid in self.adj[u]:
                v = self.to[eid]
                if self.cap[eid] > 0 and self.nivel[v] == -1:
                    self.nivel[v] = self.nivel[u] + 1
                    q.append(v)
        return self.nivel[t] != -1

    def _dfs(self, u, t, f):
        if u == t or f == 0:
            return f
        while self.it[u] < len(self.adj[u]):
            eid = self.adj[u][self.it[u]]
            v = self.to[eid]
            if self.cap[eid] > 0 and self.nivel[v] == self.nivel[u] + 1:
                d = self._dfs(v, t, min(f, self.cap[eid]))
                if d > 0:
                    self.cap[eid] -= d
                    self.cap[eid ^ 1] += d  # actualiza la arista residual inversa
                    return d
            self.it[u] += 1  # esta arista ya no sirve mas en este blocking flow
        return 0

    def max_flow(self, s, t):
        flujo = 0
        while self._bfs(s, t):
            self.it = [0] * self.n
            f = self._dfs(s, t, float('inf'))
            while f > 0:
                flujo += f
                f = self._dfs(s, t, float('inf'))
        return flujo


if __name__ == "__main__":
    din = Dinic(4)
    din.agregar_arista(0, 1, 3)
    din.agregar_arista(0, 2, 2)
    din.agregar_arista(1, 2, 1)
    din.agregar_arista(1, 3, 2)
    din.agregar_arista(2, 3, 3)
    assert din.max_flow(0, 3) == 5  # mismo grafo que edmonds_karp.py, mismo resultado
    print("OK")
