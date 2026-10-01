# Encontrar la distancia minima desde un nodo fuente a todos los demas
# en un grafo dirigido con pesos NO negativos. Usa una cola de
# prioridad para expandir siempre el nodo con menor distancia
# conocida. grafo = diccionario {u: [(v1,peso1), (v2,peso2), ...]}.

import heapq


def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0
    heap = [(0, inicio)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, peso in grafo[u]:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                heapq.heappush(heap, (dist[v], v))
    return dist


if __name__ == "__main__":
    grafo = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    dist = dijkstra(grafo, 0)
    assert dist[0] == 0
    assert dist[2] == 1
    assert dist[1] == 3   # 0->2->1 = 1+2=3, mejor que 0->1=4
    assert dist[3] == 4   # 0->2->1->3 = 1+2+1=4
    print("OK")
