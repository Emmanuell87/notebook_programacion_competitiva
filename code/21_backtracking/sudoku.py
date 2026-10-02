# tablero = matriz 9 x 9 con 0 en las celdas vacias. Se modifica en el
# lugar. Devuelve True si encontro solucion (y el tablero queda resuelto).


def resolver_sudoku(tablero):
    def es_valido(f, c, v):
        for i in range(9):
            if tablero[f][i] == v or tablero[i][c] == v:
                return False
        bf, bc = 3 * (f // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if tablero[bf + i][bc + j] == v:
                    return False
        return True

    def resolver():
        for f in range(9):
            for c in range(9):
                if tablero[f][c] == 0:
                    for v in range(1, 10):
                        if es_valido(f, c, v):
                            tablero[f][c] = v
                            if resolver():
                                return True
                            tablero[f][c] = 0   # deshacer
                    return False                # ningun valor sirve: retroceder
        return True                             # no quedan celdas vacias

    return resolver()


if __name__ == "__main__":
    puzzle = [
        "530070000", "600195000", "098000060",
        "800060003", "400803001", "700020006",
        "060000280", "000419005", "000080079",
    ]
    tablero = [[int(ch) for ch in fila] for fila in puzzle]
    original = [fila[:] for fila in tablero]
    assert resolver_sudoku(tablero) is True
    assert tablero[0] == [5, 3, 4, 6, 7, 8, 9, 1, 2]
    # solucion valida y respeta las pistas
    for i in range(9):
        assert sorted(tablero[i]) == list(range(1, 10))
        assert sorted(tablero[f][i] for f in range(9)) == list(range(1, 10))
    for bf in range(0, 9, 3):
        for bc in range(0, 9, 3):
            caja = [tablero[bf + i][bc + j] for i in range(3) for j in range(3)]
            assert sorted(caja) == list(range(1, 10))
    for f in range(9):
        for c in range(9):
            assert original[f][c] in (0, tablero[f][c])

    # sin solucion: la celda (0,8) no admite ningun valor
    imposible = [[0] * 9 for _ in range(9)]
    imposible[0] = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    imposible[1][8] = 9
    assert resolver_sudoku(imposible) is False
    print("OK")
