# Matching bipartito. Emparejar dos conjuntos disjuntos (ej.
# trabajadores-tareas, alumnos-proyectos) maximizando la cantidad de
# parejas, cuando NO hay costos/pesos de por medio. Si hay costos, usa
# Hungarian (hungarian.py). G = lista de adyacencia 0-indexada SOLO
# del lado U (G[u] = indices en V a los que u puede conectarse); U,V
# = tamanos de cada lado. Devuelve (match, pairU, pairV).

from collections import deque

INF = 10 ** 18


def hopcroft_karp(G, U, V):
    pairU = [-1] * U
    pairV = [-1] * V
    dist = [0] * U

    def bfs():
        q = deque()
        for u in range(U):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in G[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                if pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in G[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = INF
        return False

    match = 0
    while bfs():
        for u in range(U):
            if pairU[u] == -1 and dfs(u):
                match += 1
    return match, pairU, pairV


if __name__ == "__main__":
    # 3 trabajadores (U), 3 tareas (V)
    # trabajador 0 puede hacer tareas 0,1; trabajador 1 solo tarea 0;
    # trabajador 2 puede hacer tareas 1,2
    G = [[0, 1], [0], [1, 2]]
    match, pairU, pairV = hopcroft_karp(G, 3, 3)
    assert match == 3, match
    # verificar consistencia entre pairU y pairV
    for u in range(3):
        assert pairV[pairU[u]] == u

    # caso con matching maximo imperfecto: dos trabajadores quieren la misma unica tarea
    G2 = [[0], [0]]
    match2, pairU2, _ = hopcroft_karp(G2, 2, 1)
    assert match2 == 1
    print("OK")
