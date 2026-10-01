# Cubrir un intervalo objetivo con la menor cantidad de subintervalos.
# Estrategia: ordenar por inicio, luego extender lo mas posible con
# cada paso. Devuelve [] si es imposible cubrirlo.


def cubrir_intervalo(intervalos, objetivo):
    intervalos.sort()
    res = []
    i, n = 0, len(intervalos)
    actual = objetivo[0]
    while actual < objetivo[1]:
        mejor = None
        while i < n and intervalos[i][0] <= actual:
            if mejor is None or intervalos[i][1] > mejor[1]:
                mejor = intervalos[i]
            i += 1
        if mejor is None:
            return []  # no se puede cubrir
        res.append(mejor)
        actual = mejor[1]
    return res


if __name__ == "__main__":
    # (0,3) queda dominado por (0,5) (mismo inicio, llega mas lejos):
    # el greedy debe saltarselo y usar solo 3 intervalos, no 4
    intervalos = [(0, 3), (0, 5), (2, 7), (6, 9)]
    res = cubrir_intervalo(intervalos, (0, 9))
    assert res == [(0, 5), (2, 7), (6, 9)], res

    # imposible: hueco entre 2 y 3
    intervalos_con_hueco = [(0, 2), (3, 5)]
    assert cubrir_intervalo(intervalos_con_hueco, (0, 5)) == []
    print("OK")
