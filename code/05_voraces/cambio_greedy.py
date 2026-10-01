# Dar cambio usando la menor cantidad de monedas. Estrategia voraz:
# tomar siempre la moneda mas grande posible. SOLO funciona
# correctamente si el sistema de monedas es "canonico" (ej: 1,5,10,25).


def cambio_greedy(monedas, valor):
    monedas.sort(reverse=True)
    resultado = []
    for m in monedas:
        while valor >= m:
            valor -= m
            resultado.append(m)
    return resultado


if __name__ == "__main__":
    res = cambio_greedy([1, 5, 10, 25], 41)
    assert sum(res) == 41
    assert res == [25, 10, 5, 1], res
    assert len(cambio_greedy([1, 5, 10, 25], 0)) == 0
    print("OK")
