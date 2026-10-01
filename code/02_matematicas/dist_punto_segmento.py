# Distancia de un punto a un segmento (no a una recta infinita).
# p = punto; a,b = extremos del segmento. Proyecta p sobre la recta y
# recorta (clamp) la proyeccion al rango [a,b].


def dist_punto_segmento(p, a, b):
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:  # a y b son el mismo punto
        return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))  # clamp al segmento
    cx, cy = ax + t * dx, ay + t * dy
    return ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5


if __name__ == "__main__":
    # punto justo encima del segmento horizontal
    assert dist_punto_segmento((1, 1), (0, 0), (2, 0)) == 1.0
    # punto mas alla del extremo derecho: distancia al extremo, no a la recta
    assert dist_punto_segmento((5, 0), (0, 0), (2, 0)) == 3.0
    # punto sobre el segmento
    assert dist_punto_segmento((1, 0), (0, 0), (2, 0)) == 0.0
    # a y b son el mismo punto
    assert dist_punto_segmento((3, 4), (0, 0), (0, 0)) == 5.0
    print("OK")
