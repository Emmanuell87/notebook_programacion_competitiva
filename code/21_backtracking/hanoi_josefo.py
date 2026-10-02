def hanoi(n, origen="A", destino="C", auxiliar="B"):
    # lista de movimientos (desde, hacia) para pasar n discos de origen a destino
    if n == 0:
        return []
    return (hanoi(n - 1, origen, auxiliar, destino)
            + [(origen, destino)]
            + hanoi(n - 1, auxiliar, destino, origen))


def josefo(n, k):
    # n personas en circulo (0..n-1), se elimina cada k-esima.
    # Devuelve la posicion (0-indexada) de la que sobrevive.
    # Recurrencia: J(1) = 0, J(n) = (J(n-1) + k) mod n
    pos = 0
    for i in range(2, n + 1):
        pos = (pos + k) % i
    return pos


if __name__ == "__main__":
    assert hanoi(1) == [("A", "C")]
    assert hanoi(2) == [("A", "B"), ("A", "C"), ("B", "C")]
    assert josefo(7, 3) == 3
    assert josefo(1, 5) == 0

    for n in range(0, 9):
        movs = hanoi(n)
        assert len(movs) == 2 ** n - 1
        pilas = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        for desde, hacia in movs:
            disco = pilas[desde].pop()
            assert not pilas[hacia] or pilas[hacia][-1] > disco   # nunca grande sobre chico
            pilas[hacia].append(disco)
        assert pilas["C"] == list(range(n, 0, -1)) and not pilas["A"] and not pilas["B"]

    for n in range(1, 30):
        for k in range(1, 8):
            vivos = list(range(n))
            i = 0
            while len(vivos) > 1:
                i = (i + k - 1) % len(vivos)
                vivos.pop(i)
            assert josefo(n, k) == vivos[0], (n, k)
    print("OK")
