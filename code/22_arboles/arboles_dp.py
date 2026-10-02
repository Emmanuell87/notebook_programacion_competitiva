import sys

sys.setrecursionlimit(10 ** 6)   # el DFS es recursivo: necesario con muchos nodos

# Para un arbol no dirigido con n nodos (0..n-1), grafo = lista de
# adyacencia, en UN solo DFS desde la raiz calcula:
#   tam[u]  = cantidad de nodos del subarbol de u
#   alt[u]  = altura de u (aristas hasta su hoja mas lejana)
#   prof[u] = profundidad de u (aristas desde la raiz)
#   tin/tout = tiempos de entrada/salida: el subarbol de u son los
#              nodos v con tin[u] <= tin[v] <= tout[u] (un rango contiguo)
#   diametro = mayor distancia entre dos nodos, en aristas


def info_arbol(n, grafo, raiz=0):
    tam = [1] * n
    alt = [0] * n
    prof = [0] * n
    tin = [0] * n
    tout = [0] * n
    diametro = 0
    tiempo = 0

    def dfs(u, padre):
        nonlocal tiempo, diametro
        tin[u] = tiempo
        tiempo += 1
        mayor1 = mayor2 = 0          # las dos mayores alturas entre los hijos (+1)
        for v in grafo[u]:
            if v == padre:
                continue
            prof[v] = prof[u] + 1
            dfs(v, u)
            tam[u] += tam[v]
            h = alt[v] + 1
            if h > mayor1:
                mayor1, mayor2 = h, mayor1
            elif h > mayor2:
                mayor2 = h
        alt[u] = mayor1
        diametro = max(diametro, mayor1 + mayor2)   # el camino mas largo que pasa por u
        tout[u] = tiempo - 1

    dfs(raiz, -1)
    return {"tam": tam, "alt": alt, "prof": prof, "tin": tin, "tout": tout, "diametro": diametro}


if __name__ == "__main__":
    import random
    from collections import deque

    # --- ejemplo ---
    # arbol: 0 es raiz; hijos de 0: [1, 2]; hijos de 1: [3, 4]; hijo de 4: [5]
    grafo = [[1, 2], [0, 3, 4], [0], [1], [1, 5], [4]]
    info = info_arbol(6, grafo)
    assert info["tam"] == [6, 4, 1, 1, 2, 1]
    assert info["alt"] == [3, 2, 0, 0, 1, 0]
    assert info["diametro"] == 4          # 2 - 0 - 1 - 4 - 5
    # el subarbol de 1 son los nodos con tin en [tin[1], tout[1]]
    assert info["tout"][1] - info["tin"][1] + 1 == info["tam"][1]
    # --- fin ejemplo ---

    def distancias(n, grafo, s):
        d = [-1] * n
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in grafo[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    q.append(v)
        return d

    random.seed(5)
    for _ in range(300):
        n = random.randint(1, 14)
        grafo = [[] for _ in range(n)]
        for v in range(1, n):
            u = random.randrange(v)
            grafo[u].append(v)
            grafo[v].append(u)
        raiz = random.randrange(n)
        info = info_arbol(n, grafo, raiz)
        dist = [distancias(n, grafo, s) for s in range(n)]
        assert info["diametro"] == max(max(f) for f in dist)
        assert info["prof"] == dist[raiz]
        assert info["tam"][raiz] == n and info["tin"][raiz] == 0
        for u in range(n):
            # subarbol = nodos cuyo camino a la raiz pasa por u
            sub = [v for v in range(n) if dist[raiz][v] == dist[raiz][u] + dist[u][v]]
            assert info["tam"][u] == len(sub)
            assert info["alt"][u] == max(dist[u][v] for v in sub)
            en_rango = [v for v in range(n) if info["tin"][u] <= info["tin"][v] <= info["tout"][u]]
            assert sorted(en_rango) == sorted(sub)
    # cadena larga: no revienta el limite de recursion (con setrecursionlimit)
    n = 3000
    cadena = [[j for j in (i - 1, i + 1) if 0 <= j < n] for i in range(n)]
    assert info_arbol(n, cadena)["diametro"] == n - 1
    print("OK")
