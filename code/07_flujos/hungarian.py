# Asignacion de tareas, O(n^3). Emparejamiento bipartito CON COSTOS: n
# trabajadores y n tareas, cada par (i,j) tiene un costo, y quieres el
# emparejamiento 1-a-1 completo que MINIMIZA el costo total. cost =
# matriz n x n, cost[i][j] = costo de asignar el trabajador i a la
# tarea j. Devuelve (total, asig): costo minimo total y asig[i] =
# tarea asignada al trabajador i. Para MAXIMIZAR, negar la matriz de
# costos antes de llamarla.


def hungarian(cost):
    n = len(cost)
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [float('inf')] * (n + 1)
        used = [False] * (n + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = float('inf')
            j1 = 0
            for j in range(1, n + 1):
                if not used[j]:
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    asig = [0] * n
    for j in range(1, n + 1):
        if p[j]:
            asig[p[j] - 1] = j - 1
    total = sum(cost[i][asig[i]] for i in range(n))
    return total, asig


def fuerza_bruta(cost):
    from itertools import permutations
    n = len(cost)
    mejor = float('inf')
    for perm in permutations(range(n)):
        total = sum(cost[i][perm[i]] for i in range(n))
        mejor = min(mejor, total)
    return mejor


if __name__ == "__main__":
    import random
    random.seed(0)
    for _ in range(20):
        n = random.randint(1, 5)
        cost = [[random.randint(1, 20) for _ in range(n)] for _ in range(n)]
        total, asig = hungarian(cost)
        assert len(set(asig)) == n  # asignacion valida (biyeccion)
        assert total == fuerza_bruta(cost), (cost, total, fuerza_bruta(cost))
    print("OK")
