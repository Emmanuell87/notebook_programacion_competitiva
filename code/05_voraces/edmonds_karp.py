# Calcular el flujo maximo desde un nodo fuente a uno destino en un
# grafo dirigido con capacidades. Variante de Ford-Fulkerson que usa
# BFS para encontrar caminos aumentantes con la menor cantidad de
# aristas. grafo = diccionario {nodo: [(vecino, capacidad), ...]}
# (dirigido); s,t = nodo fuente y destino. Devuelve el valor del flujo
# maximo (numero), no las rutas usadas.
#
# Para grafos grandes (V~10^4, E~10^5) esto puede dar TLE por ser
# O(V E^2); ver Dinic (seccion de Flujos) para una version mas rapida.

from collections import deque, defaultdict


def bfs(capacidad, grafo, s, t, padre):
    visitado = set()
    q = deque([s])
    while q:
        u = q.popleft()
        for v, _ in grafo[u]:  # OJO: desempaquetar (vecino, peso), no comparar la tupla completa
            if v not in visitado and capacidad[u][v] > 0:
                padre[v] = u
                visitado.add(v)
                if v == t:
                    return True
                q.append(v)
    return False


def edmonds_karp(grafo, s, t):
    capacidad = defaultdict(lambda: defaultdict(int))
    for u in grafo:
        for v, c in grafo[u]:
            capacidad[u][v] += c
            capacidad[v][u] += 0  # residual inverso

    flujo = 0
    padre = {}
    while bfs(capacidad, grafo, s, t, padre):
        f = float('inf')
        v = t
        while v != s:
            u = padre[v]
            f = min(f, capacidad[u][v])
            v = u
        v = t
        while v != s:
            u = padre[v]
            capacidad[u][v] -= f
            capacidad[v][u] += f
            v = u
        flujo += f
    return flujo


if __name__ == "__main__":
    grafo = {
        0: [(1, 3), (2, 2)],
        1: [(2, 1), (3, 2)],
        2: [(3, 3)],
        3: [],
    }
    assert edmonds_karp(grafo, 0, 3) == 5  # 0->1->3(2) + 0->2->3(2) + 0->1->2->3(1) = 5
    print("OK")
