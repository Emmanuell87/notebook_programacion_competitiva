# Caminos con Pesos Negativos - Bellman-Ford. Encontrar distancias
# minimas desde un nodo fuente s en grafos dirigidos con pesos
# negativos, detectando ciclos negativos que afectan a otros nodos.
# En vez de Dijkstra cuando el grafo puede tener pesos negativos
# (Dijkstra falla en ese caso). n = numero de nodos (0-indexados),
# edges = lista de (u, v, w), s = nodo fuente. Devuelve
# (dist, in_neg_cycle): distancias minimas y que nodos son
# alcanzables desde un ciclo negativo (ahi la "distancia minima" no
# esta bien definida, tiende a -infinito).

from collections import deque


def bellman_ford(n, edges, s):
    dist = [float('inf')] * n
    dist[s] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Paso extra: detectar nodos afectados por ciclos negativos
    in_neg_cycle = [False] * n
    for _ in range(1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                in_neg_cycle[v] = True

    # Propagacion con BFS
    graph = [[] for _ in range(n)]
    for u, v, _ in edges:
        graph[u].append(v)

    queue = deque([i for i in range(n) if in_neg_cycle[i]])
    visited = [False] * n
    for i in queue:
        visited[i] = True

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                in_neg_cycle[v] = True
                queue.append(v)

    return dist, in_neg_cycle


if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, -2), (1, 3, 1)]
    dist, in_neg_cycle = bellman_ford(4, edges, 0)
    assert dist[1] == -1  # 0->2->1 = 1-2=-1, mejor que 0->1=4
    assert dist[3] == 0   # 0->2->1->3 = 1-2+1=0
    assert not any(in_neg_cycle)

    # con ciclo negativo: 0->1->2->0 con suma negativa
    edges_ciclo = [(0, 1, 1), (1, 2, -3), (2, 0, 1), (2, 3, 1)]
    dist2, in_neg = bellman_ford(4, edges_ciclo, 0)
    assert in_neg[0] and in_neg[1] and in_neg[2] and in_neg[3]
    print("OK")
