# Interseccion de dos segmentos (caso general + casos colineales/de borde).
# Preguntas del tipo "este cable/pared/trayectoria cruza a este otro?".
# p1,p2 extremos del primer segmento; p3,p4 del segundo. Devuelve True/False
# (no el punto de interseccion).
#
# NOTA: incluye copias locales de orientacion() y en_segmento() para que
# el archivo sea autocontenido (ver tambien orientacion.py, en_segmento.py).


def orientacion(o, a, b):
    val = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0


def en_segmento(p, a, b):
    return (min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def segmentos_se_intersectan(p1, p2, p3, p4):
    d1 = orientacion(p3, p4, p1)
    d2 = orientacion(p3, p4, p2)
    d3 = orientacion(p1, p2, p3)
    d4 = orientacion(p1, p2, p4)

    if d1 != d2 and d3 != d4:
        return True

    if d1 == 0 and en_segmento(p1, p3, p4):
        return True
    if d2 == 0 and en_segmento(p2, p3, p4):
        return True
    if d3 == 0 and en_segmento(p3, p1, p2):
        return True
    if d4 == 0 and en_segmento(p4, p1, p2):
        return True

    return False


if __name__ == "__main__":
    # cruz clasica: se intersectan en (1,1)
    assert segmentos_se_intersectan((0, 0), (2, 2), (0, 2), (2, 0)) is True
    # paralelos, no se tocan
    assert segmentos_se_intersectan((0, 0), (1, 0), (0, 1), (1, 1)) is False
    # colineales y se solapan
    assert segmentos_se_intersectan((0, 0), (2, 0), (1, 0), (3, 0)) is True
    # colineales pero sin tocarse
    assert segmentos_se_intersectan((0, 0), (1, 0), (2, 0), (3, 0)) is False
    print("OK")
