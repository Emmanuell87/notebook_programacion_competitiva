# Deteccion de ciclo en grafos NO dirigidos. g = lista de adyacencia
# 0-indexada. Aqui basta 1 color (vis) porque en no dirigido cualquier
# vecino ya visitado que NO sea el padre implica ciclo (por eso el
# parametro p, que evita confundir la arista de vuelta al padre con
# un ciclo).


def ciclo_nodirigido(g):
    n = len(g)
    vis = [False] * n

    def dfs(u, p):
        vis[u] = True
        for v in g[u]:
            if v == p:
                continue
            if vis[v] or dfs(v, u):
                return True
        return False

    return any(not vis[i] and dfs(i, -1) for i in range(n))


if __name__ == "__main__":
    # triangulo 0-1-2-0 (ciclo)
    g_con_ciclo = [[1, 2], [0, 2], [0, 1]]
    assert ciclo_nodirigido(g_con_ciclo) is True

    # arbol 0-1, 1-2 (sin ciclo)
    g_arbol = [[1], [0, 2], [1]]
    assert ciclo_nodirigido(g_arbol) is False
    print("OK")
