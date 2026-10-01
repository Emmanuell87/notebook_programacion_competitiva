# Puntos de articulacion y puentes (Tarjan). En grafos NO dirigidos y
# conexos: un PUNTO DE ARTICULACION es un nodo que, al quitarlo,
# desconecta el grafo; un PUENTE es una arista con la misma propiedad.
# Tipico en problemas de "puntos criticos de una red". g = lista de
# adyacencia 0-indexada. Devuelve (is_art, bridges).

import sys
sys.setrecursionlimit(10000)


def articulaciones_y_puentes(g):
    n = len(g)
    time = 0
    tin = [-1] * n
    low = [0] * n
    is_art = [False] * n
    bridges = []

    def dfs(u, p=-1):
        nonlocal time
        time += 1
        tin[u] = low[u] = time
        hijos = 0
        for v in g[u]:
            if v == p:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] >= tin[u] and p != -1:
                    is_art[u] = True
                if low[v] > tin[u]:
                    bridges.append((u, v))
                hijos += 1
        if p == -1 and hijos > 1:
            is_art[u] = True

    for i in range(n):
        if tin[i] == -1:
            dfs(i)
    return is_art, bridges


if __name__ == "__main__":
    # 0-1-2 triangulo, mas 2-3 colgando: 3 conecta solo por 2 (puente),
    # y 2 es punto de articulacion (quitarlo desconecta a 3)
    g = [[1, 2], [0, 2], [0, 1, 3], [2]]
    is_art, bridges = articulaciones_y_puentes(g)
    assert is_art[2] is True
    assert is_art[0] is False and is_art[1] is False and is_art[3] is False
    assert (2, 3) in bridges or (3, 2) in bridges
    assert len(bridges) == 1
    print("OK")
