# Cuadrados Magicos: matriz n x n con filas, columnas y diagonales que
# suman igual. Verificacion.


def es_magico(grid):
    n = len(grid)
    suma = sum(grid[0])
    return (
        all(sum(fila) == suma for fila in grid) and
        all(sum(grid[i][j] for i in range(n)) == suma for j in range(n)) and
        sum(grid[i][i] for i in range(n)) == suma and
        sum(grid[i][n - 1 - i] for i in range(n)) == suma
    )


if __name__ == "__main__":
    magico = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8],
    ]
    assert es_magico(magico) is True

    no_magico = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert es_magico(no_magico) is False
    print("OK")
