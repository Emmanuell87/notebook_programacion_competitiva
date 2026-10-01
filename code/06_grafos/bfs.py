# Recorrer un grafo nivel por nivel, util para encontrar la distancia
# minima en grafos no ponderados. grafo = diccionario
# {nodo: [vecino1, vecino2, ...]} (sin pesos); inicio = nodo de
# partida. Devuelve {nodo: distancia} (en numero de aristas).

from collections import deque


def bfs(grafo, inicio):
    visitado = set()
    distancia = {inicio: 0}
    cola = deque([inicio])
    visitado.add(inicio)

    while cola:
        u = cola.popleft()
        for v in grafo[u]:
            if v not in visitado:
                visitado.add(v)
                distancia[v] = distancia[u] + 1
                cola.append(v)
    return distancia


if __name__ == "__main__":
    grafo = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
    dist = bfs(grafo, 0)
    assert dist == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}, dist
    print("OK")
