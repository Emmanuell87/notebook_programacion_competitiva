# TSP con DP sobre bitmask (Held-Karp). dist = matriz n x n con
# dist[i][j] = costo de ir de i a j. dp[mask][u] = costo minimo de un
# camino que parte de la ciudad 0, visita exactamente las ciudades de
# mask y termina en u. Viable hasta n ~ 20 (memoria 2^n * n).


def tsp_bitmask(dist):
    n = len(dist)
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0                                  # solo la ciudad 0 visitada
    for mask in range(1, 1 << n):
        if not mask & 1:
            continue                              # todo camino incluye la ciudad 0
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if mask >> v & 1:
                    continue                      # v ya fue visitada
                nueva = mask | (1 << v)
                costo = dp[mask][u] + dist[u][v]
                if costo < dp[nueva][v]:
                    dp[nueva][v] = costo
    completo = (1 << n) - 1
    return min(dp[completo][u] + dist[u][0] for u in range(n))   # volver a 0


if __name__ == "__main__":
    # --- ejemplo ---
    # cuadrado de 4 ciudades: ir por el borde cuesta 4
    dist = [
        [0, 1, 2, 1],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [1, 2, 1, 0],
    ]
    assert tsp_bitmask(dist) == 4
    # --- fin ejemplo ---
    from itertools import permutations
    import random

    cuadrado = [
        [0, 1, 2, 1],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [1, 2, 1, 0],
    ]
    assert tsp_bitmask(cuadrado) == 4
    assert tsp_bitmask([[0]]) == 0

    def fuerza_bruta(dist):
        n = len(dist)
        return min(sum(dist[p[i]][p[(i + 1) % n]] for i in range(n))
                   for p in ([0] + list(q) for q in permutations(range(1, n))))

    random.seed(8)
    for _ in range(60):
        n = random.randint(1, 7)
        dist = [[0 if i == j else random.randint(1, 20) for j in range(n)] for i in range(n)]
        assert tsp_bitmask(dist) == fuerza_bruta(dist)
    print("OK")
