# Area de un poligono simple (formula del Shoelace):
#   Area = 1/2 * |sum(x_i * y_{i+1} - x_{i+1} * y_i)|
# Sirve siempre que te den los vertices de un poligono (no autointersectado)
# y pidan su area. puntos = lista de vertices (x,y) en orden, O(n).


def area_poligono(puntos):
    n = len(puntos)
    s = 0
    for i in range(n):
        x1, y1 = puntos[i]
        x2, y2 = puntos[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


if __name__ == "__main__":
    cuadrado = [(0, 0), (4, 0), (4, 4), (0, 4)]
    assert area_poligono(cuadrado) == 16

    triangulo = [(0, 0), (4, 0), (0, 3)]
    assert area_poligono(triangulo) == 6.0

    # el orden (horario vs antihorario) no debe afectar el resultado (usa abs)
    assert area_poligono(list(reversed(cuadrado))) == 16
    print("OK")
