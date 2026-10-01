# Encontrar la envolvente convexa de un conjunto de puntos en
# O(n log n) (Monotone Chain / Andrew). El poligono convexo mas
# pequeno que contiene a todos los puntos dados. points = lista de
# tuplas (x,y) (se eliminan duplicados internamente). Devuelve los
# vertices del hull en orden ANTIHORARIO, sin repetir el primer punto
# al final.


def convex_hull(points):
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


if __name__ == "__main__":
    # cuadrado con un punto interior que no debe quedar en el hull
    puntos = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]
    hull = convex_hull(puntos)
    assert set(hull) == {(0, 0), (4, 0), (4, 4), (0, 4)}
    assert (2, 2) not in hull
    assert len(hull) == 4
    print("OK")
