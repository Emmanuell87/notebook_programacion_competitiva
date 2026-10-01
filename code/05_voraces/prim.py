# Encontrar el arbol de expansion minima (MST) en un grafo no dirigido
# y conexo. grafo = diccionario {nodo: [(vecino, peso), ...]}; inicio
# = nodo cualquiera (el resultado no depende de cual se elija).
# Devuelve la lista de aristas del MST como (padre, hijo, peso).
# Alternativa: kruskal (seccion DSU) -- Prim conviene en grafos densos.
# El MST contiene n-1 aristas si el grafo tiene n nodos.

import heapq


def prim(grafo, inicio):
    visitado = set()
    mst = []
    heap = [(0, inicio, None)]  # (peso, nodo, padre)

    while heap and len(visitado) < len(grafo):
        peso, u, padre = heapq.heappop(heap)
        if u not in visitado:
            visitado.add(u)
            if padre is not None:
                mst.append((padre, u, peso))
            for v, w in grafo[u]:
                if v not in visitado:
                    heapq.heappush(heap, (w, v, u))
    return mst


if __name__ == "__main__":
    grafo = {
        0: [(1, 4), (2, 1)],
        1: [(0, 4), (2, 2), (3, 5)],
        2: [(0, 1), (1, 2), (3, 8)],
        3: [(1, 5), (2, 8)],
    }
    mst = prim(grafo, 0)
    assert len(mst) == len(grafo) - 1
    peso_total = sum(w for _, _, w in mst)
    assert peso_total == 1 + 2 + 5  # 0-2(1), 2-1(2), 1-3(5)
    print("OK")
