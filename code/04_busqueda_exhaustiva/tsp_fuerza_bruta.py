# Problema del Agente Viajero (TSP): encuentra el camino minimo que
# visita cada ciudad una vez y regresa al inicio. dist = matriz de
# adyacencia n x n (lista de listas), dist[i][j] = costo de ir de i a j.
# Solo viable para n <~ 10-11 por el O(n!); para n mas grande se usa
# bitmask DP (O(n^2 2^n)) o Branch & Bound (ver "Ramificacion y Poda
# (Branch and Bound)" en esta misma seccion).

from itertools import permutations


def tsp(dist):
    n = len(dist)
    res = float("inf")
    for p in permutations(range(n)):
        cost = sum(dist[p[i]][p[(i + 1) % n]] for i in range(n))
        res = min(res, cost)
    return res


if __name__ == "__main__":
    # cuadrado de 4 ciudades: ir por el borde cuesta 4
    dist = [
        [0, 1, 2, 1],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [1, 2, 1, 0],
    ]
    assert tsp(dist) == 4

    # triangulo simple
    dist2 = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]
    assert tsp(dist2) == 3
    print("OK")
