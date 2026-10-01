# Seleccionar el maximo numero de actividades no solapadas segun su
# tiempo de inicio y fin. Estrategia: ordenar por hora de finalizacion
# y seleccionar actividades compatibles.


def seleccionar_actividades(inicio, fin):
    actividades = sorted(zip(inicio, fin), key=lambda x: x[1])
    res = []
    fin_actual = 0
    for i, f in actividades:
        if i >= fin_actual:
            res.append((i, f))
            fin_actual = f
    return res


if __name__ == "__main__":
    inicio = [1, 3, 0, 5, 8, 5]
    fin = [2, 4, 6, 7, 9, 9]
    res = seleccionar_actividades(inicio, fin)
    # orden por fin: (1,2),(3,4),(5,7),(0,6),(8,9),(5,9)
    # greedy: toma (1,2), (3,4), (5,7) [0,6) se descarta por solapar con (3,4), (8,9)
    assert res == [(1, 2), (3, 4), (5, 7), (8, 9)], res
    print("OK")
