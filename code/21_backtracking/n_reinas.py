def soluciones_n_reinas(n):
    # genera cada solucion como una lista cols, donde cols[f] = columna
    # de la reina de la fila f
    cols = []
    ocupa_col = set()
    ocupa_d1 = set()   # diagonales f - c
    ocupa_d2 = set()   # diagonales f + c

    def colocar(f):
        if f == n:
            yield cols[:]
            return
        for c in range(n):
            if c in ocupa_col or (f - c) in ocupa_d1 or (f + c) in ocupa_d2:
                continue   # poda: la casilla esta atacada
            cols.append(c)
            ocupa_col.add(c)
            ocupa_d1.add(f - c)
            ocupa_d2.add(f + c)
            yield from colocar(f + 1)
            cols.pop()
            ocupa_col.remove(c)
            ocupa_d1.remove(f - c)
            ocupa_d2.remove(f + c)

    return colocar(0)


def contar_n_reinas(n):
    return sum(1 for _ in soluciones_n_reinas(n))


if __name__ == "__main__":
    assert [contar_n_reinas(n) for n in range(1, 9)] == [1, 0, 0, 2, 10, 4, 40, 92]
    assert next(soluciones_n_reinas(4)) == [1, 3, 0, 2]
    assert next(soluciones_n_reinas(1)) == [0]
    assert next(soluciones_n_reinas(3), None) is None   # sin solucion

    for n in range(1, 8):
        for sol in soluciones_n_reinas(n):
            assert sorted(sol) == list(range(n))
            for f1 in range(n):
                for f2 in range(f1 + 1, n):
                    assert abs(sol[f1] - sol[f2]) != f2 - f1   # no comparten diagonal
    print("OK")
