# Encontrar el minimo (o maximo) de una funcion UNIMODAL continua o
# discreta. Precondicion: f debe ser unimodal en [l, r] (baja y luego
# sube, o viceversa -- una sola "joroba"; si tiene varios
# minimos/maximos locales el algoritmo puede fallar). f = funcion que
# recibe un numero y devuelve un numero; l, r = extremos del rango de
# busqueda; eps = precision deseada. Para f buscando el MAXIMO,
# invierte la comparacion (if f(m1) > f(m2)).


def ternary_search(f, l, r, eps=1e-6):
    while r - l > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return (l + r) / 2  # Posicion del minimo


if __name__ == "__main__":
    # parabola (x-3)^2 + 1, minimo en x=3
    f = lambda x: (x - 3) ** 2 + 1
    x_min = ternary_search(f, -10, 10)
    assert abs(x_min - 3) < 1e-4, x_min

    # funcion con minimo en x=0, buscando en rango asimetrico
    g = lambda x: x ** 2
    assert abs(ternary_search(g, -5, 2)) < 1e-4
    print("OK")
