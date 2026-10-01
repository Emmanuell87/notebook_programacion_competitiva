# Ordenar tareas/eventos con dependencias (DAG) de modo que cada nodo
# aparezca despues de todos sus prerequisitos; tambien sirve para
# DETECTAR CICLOS en un grafo dirigido (si orden no incluye todos los
# nodos, hay ciclo). A diferencia de BFS/DFS/Dijkstra (diccionario),
# aqui el grafo es lista de adyacencia 0-indexada: n = numero de
# nodos (0..n-1), edges = lista de (u, v) (arista dirigida u->v).
# Devuelve la lista de nodos en orden topologico, o None si hay ciclo.

from collections import deque


def topo_sort(n, edges):
    g = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    orden = []
    while q:
        u = q.popleft()
        orden.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return orden if len(orden) == n else None


if __name__ == "__main__":
    # 0 -> 1 -> 2, 0 -> 2
    orden = topo_sort(3, [(0, 1), (1, 2), (0, 2)])
    assert orden.index(0) < orden.index(1) < orden.index(2)

    # ciclo: 0->1->2->0
    assert topo_sort(3, [(0, 1), (1, 2), (2, 0)]) is None
    print("OK")
