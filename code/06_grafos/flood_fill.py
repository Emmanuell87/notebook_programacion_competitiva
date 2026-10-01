# Cuando el "grafo" es en realidad una matriz/grilla 2D (mapa, imagen)
# y necesitas expandirte desde una celda a sus 4 vecinas mientras
# cumplan una condicion (ej.: mismo color/valor). grid = matriz
# (lista de listas); sx,sy = fila/columna donde empieza el relleno;
# marca = valor con el que se sobrescriben las celdas visitadas.
# Devuelve cuantas celdas se rellenaron. OJO: modifica grid en el
# lugar (efecto secundario).

from collections import deque


def flood_fill(grid, sx, sy, marca=1):
    n, m = len(grid), len(grid[0])
    if not (0 <= sx < n and 0 <= sy < m):
        return 0
    objetivo = grid[sx][sy]
    q = deque([(sx, sy)])
    vis = {(sx, sy)}
    cnt = 0
    forx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y = q.popleft()
        cnt += 1
        grid[x][y] = marca
        for dx, dy in forx:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vis and grid[nx][ny] == objetivo:
                vis.add((nx, ny))
                q.append((nx, ny))
    return cnt


if __name__ == "__main__":
    grid = [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1],
    ]
    cnt = flood_fill(grid, 0, 0, marca=9)
    assert cnt == 4  # las 4 celdas con 0
    assert grid[0][0] == 9 and grid[1][1] == 9
    assert grid[0][2] == 1  # no tocado (era un 1, no un 0)
    print("OK")
