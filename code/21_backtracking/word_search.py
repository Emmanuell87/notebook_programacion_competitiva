# Buscar una palabra en una matriz de caracteres, moviendose a celdas
# vecinas (arriba/abajo/izquierda/derecha) sin reusar una celda en la
# misma palabra. tablero = lista de listas de caracteres; palabra = str.
# Se marca la celda al entrar y se restaura al salir (backtracking).


def existe_palabra(tablero, palabra):
    n, m = len(tablero), len(tablero[0])

    def buscar(f, c, k):
        if k == len(palabra):
            return True
        if not (0 <= f < n and 0 <= c < m) or tablero[f][c] != palabra[k]:
            return False
        original = tablero[f][c]
        tablero[f][c] = "#"              # marcar como usada
        encontrado = any(buscar(f + df, c + dc, k + 1)
                         for df, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        tablero[f][c] = original         # deshacer
        return encontrado

    return any(buscar(f, c, 0) for f in range(n) for c in range(m))


if __name__ == "__main__":
    tablero = [list("ABCE"), list("SFCS"), list("ADEE")]
    copia = [fila[:] for fila in tablero]
    assert existe_palabra(tablero, "ABCCED") is True
    assert existe_palabra(tablero, "SEE") is True
    assert existe_palabra(tablero, "ABCB") is False   # no se puede reusar la B
    assert tablero == copia                             # el tablero queda intacto
    assert existe_palabra([list("A")], "A") is True
    assert existe_palabra([list("AB")], "ABA") is False
    print("OK")
