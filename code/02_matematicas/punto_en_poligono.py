# Punto dentro de un poligono (ray casting): "este punto esta adentro de
# esta region/terreno?". Traza un rayo horizontal desde p hacia la derecha
# y cuenta cuantas veces cruza el borde del poligono; si es impar, adentro.
# No detecta correctamente si p cae justo sobre el borde.


def punto_en_poligono(p, poligono):
    x, y = p
    n = len(poligono)
    dentro = False
    x1, y1 = poligono[0]
    for i in range(1, n + 1):
        x2, y2 = poligono[i % n]
        if y > min(y1, y2):
            if y <= max(y1, y2):
                if x <= max(x1, x2):
                    if y1 != y2:
                        xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if x1 == x2 or x <= xinters:
                        dentro = not dentro
        x1, y1 = x2, y2
    return dentro


if __name__ == "__main__":
    cuadrado = [(0, 0), (4, 0), (4, 4), (0, 4)]
    assert punto_en_poligono((2, 2), cuadrado) is True   # centro
    assert punto_en_poligono((10, 10), cuadrado) is False  # afuera
    assert punto_en_poligono((-1, 2), cuadrado) is False  # afuera a la izquierda
    print("OK")
