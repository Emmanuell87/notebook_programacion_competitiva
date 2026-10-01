# Componentes Fuertemente Conectadas (Kosaraju). En grafos DIRIGIDOS
# para agrupar nodos que son mutuamente alcanzables (u->v y v->u);
# util como paso previo para "condensar" el grafo en un DAG de
# componentes. g = lista de adyacencia 0-indexada dirigida. Devuelve
# (comp, cid): comp[i] = id de la SCC del nodo i, cid = cantidad total
# de SCCs.


def scc_kosaraju(g):
    n = len(g)
    gr = [[] for _ in range(n)]
    for u in range(n):
        for v in g[u]:
            gr[v].append(u)
    vis = [False] * n
    order = []

    def dfs1(u):
        vis[u] = True
        for v in g[u]:
            if not vis[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not vis[i]:
            dfs1(i)

    comp = [-1] * n
    cid = 0

    def dfs2(u):
        comp[u] = cid
        for v in gr[u]:
            if comp[v] == -1:
                dfs2(v)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u)
            cid += 1
    return comp, cid


if __name__ == "__main__":
    # dos ciclos separados: 0<->1<->2<->0, y 3<->4, sin conexion entre grupos
    g = [[1], [2], [0], [4], [3]]
    comp, cid = scc_kosaraju(g)
    assert cid == 2, cid
    assert comp[0] == comp[1] == comp[2]
    assert comp[3] == comp[4]
    assert comp[0] != comp[3]
    print("OK")
