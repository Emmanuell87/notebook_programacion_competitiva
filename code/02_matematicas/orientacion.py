# Orientacion de 3 puntos (signo del producto cruz ab x ac):
# positivo = giro antihorario (izquierda), negativo = horario (derecha),
# cero = colineales. Es la pieza base de casi toda la geometria discreta.


def orientacion(o, a, b):
    val = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    if val > 0:
        return 1   # antihorario (izquierda)
    if val < 0:
        return -1  # horario (derecha)
    return 0        # colineales


if __name__ == "__main__":
    assert orientacion((0, 0), (1, 0), (1, 1)) == 1   # giro izquierda
    assert orientacion((0, 0), (1, 0), (1, -1)) == -1  # giro derecha
    assert orientacion((0, 0), (1, 0), (2, 0)) == 0   # colineales
    print("OK")
