# Caminos Mas Cortos - Floyd-Warshall. Encontrar las distancias
# minimas entre TODOS los pares de nodos en un grafo con pesos (puede
# haber pesos negativos, pero no ciclos negativos). Cuando necesitas
# distancias entre todos los pares (no solo desde una fuente) y n es
# pequeno (O(n^3), n <~ 400-500); para una sola fuente es mas barato
# Dijkstra o Bellman-Ford. grafo = matriz n x n, grafo[i][j] = peso de
# i->j (usa float('inf') si no hay arista directa, 0 en la diagonal).


def floyd_warshall(grafo):
    n = len(grafo)
    dist = [fila[:] for fila in grafo]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


if __name__ == "__main__":
    INF = float('inf')
    grafo = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0],
    ]
    dist = floyd_warshall(grafo)
    assert dist[0][2] == 5   # 0->1->2 = 3+2=5
    assert dist[0][3] == 6   # 0->1->2->3 = 3+2+1=6
    assert dist[2][1] == 6   # 2->3->0->1 = 1+2+3=6
    print("OK")
