# Pares mas cercanos (Closest Pair of Points). Encontrar la distancia
# minima entre dos puntos en un plano, en O(n log^2 n) (mejor que el
# O(n^2) de probar todos los pares; se reduce a O(n log n) si la franja
# se mantiene ordenada por y al hacer merge). points = lista de puntos (x,y);
# n >= 2. Devuelve la distancia minima ENTERA (usa int(...); quitar el
# int() final si necesitas precision decimal).

from math import inf


def closest_pair(points):
    def dist2(p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return dx * dx + dy * dy

    def closest_rec(Px, l, r):
        if r - l <= 2:
            min_d = inf
            for i in range(l, r + 1):
                for j in range(i + 1, r + 1):
                    min_d = min(min_d, dist2(Px[i], Px[j]))
            return min_d

        mid = (l + r) // 2
        mid_x = Px[mid][0]

        d_left = closest_rec(Px, l, mid)
        d_right = closest_rec(Px, mid + 1, r)
        d = min(d_left, d_right)

        strip = []
        for i in range(l, r + 1):
            if (Px[i][0] - mid_x) ** 2 < d:
                strip.append(Px[i])

        strip.sort(key=lambda x: x[1])

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1]) ** 2 >= d:
                    break
                d = min(d, dist2(strip[i], strip[j]))

        return d

    points.sort()  # Ordenar por coordenada x
    return int(closest_rec(points, 0, len(points) - 1) ** 0.5)


def fuerza_bruta(points):
    n = len(points)
    mejor = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            d = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            mejor = min(mejor, d)
    return int(mejor)


if __name__ == "__main__":
    # --- ejemplo ---
    pts = [(0, 0), (10, 10), (3, 4), (20, 20)]
    assert closest_pair(pts) == 5   # (0,0) y (3,4)
    # --- fin ejemplo ---
    import random
    random.seed(0)
    for _ in range(30):
        n = random.randint(2, 20)
        pts = [(random.randint(0, 50), random.randint(0, 50)) for _ in range(n)]
        assert closest_pair(pts[:]) == fuerza_bruta(pts), pts
    print("OK")
