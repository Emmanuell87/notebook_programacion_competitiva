# Ramificacion y Poda (Branch & Bound): optimizacion de busqueda usando
# limites para evitar caminos peores. Ejemplo aplicado a TSP: mismos
# parametros que tsp() (matriz dist), pero path/visited empiezan como
# [0]/[True]+[False]*(n-1) y cost=0, best=float('inf'). En la practica
# conviene ademas PODAR cuando cost ya supera best (no incluido aqui
# para mantenerlo simple, pero es la mejora tipica que se agrega en
# competencia).


def tsp_bb(dist, path, cost, visited, best):
    if len(path) == len(dist):
        total = cost + dist[path[-1]][path[0]]
        return min(best, total)
    for i in range(len(dist)):
        if not visited[i]:
            visited[i] = True
            best = min(best, tsp_bb(dist, path + [i], cost + dist[path[-1]][i], visited, best))
            visited[i] = False
    return best


if __name__ == "__main__":
    dist = [
        [0, 1, 2, 1],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [1, 2, 1, 0],
    ]
    n = len(dist)
    resultado = tsp_bb(dist, [0], 0, [True] + [False] * (n - 1), float("inf"))
    assert resultado == 4, resultado
    print("OK")
