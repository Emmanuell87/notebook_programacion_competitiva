# Verifica si un punto p, YA SABIENDO que es colineal con la recta a-b
# (ej. porque orientacion(a,b,p)==0), cae dentro del segmento [a,b] y no
# fuera de sus extremos. Funcion auxiliar, no se usa sola normalmente
# (la usa segmentos_intersectan.py para los casos colineales).


def en_segmento(p, a, b):
    return (min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


if __name__ == "__main__":
    assert en_segmento((1, 0), (0, 0), (2, 0)) is True
    assert en_segmento((3, 0), (0, 0), (2, 0)) is False  # fuera del rango
    assert en_segmento((0, 0), (0, 0), (2, 0)) is True   # en el extremo
    print("OK")
