# Colorear los nodos con a lo sumo m colores sin que dos vecinos
# compartan color (m-coloreo). grafo = {nodo: [vecinos]} no dirigido.
# Devuelve {nodo: color} con colores 0..m-1, o None si no se puede.
# Con m = 2 equivale a "es bipartito"; para m >= 3 el problema es
# NP-completo, por eso se usa backtracking (viable para pocos nodos).


def colorear_grafo(grafo, m):
    nodos = list(grafo)
    color = {}

    def asignar(i):
        if i == len(nodos):
            return True
        u = nodos[i]
        for c in range(m):
            if all(color.get(v) != c for v in grafo[u]):   # ningun vecino usa c
                color[u] = c
                if asignar(i + 1):
                    return True
                del color[u]                              # deshacer
        return False

    return dict(color) if asignar(0) else None


if __name__ == "__main__":
    # --- ejemplo ---
    triangulo = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert colorear_grafo(triangulo, 3) == {0: 0, 1: 1, 2: 2}
    assert colorear_grafo(triangulo, 2) is None   # un triangulo necesita 3 colores
    # --- fin ejemplo ---
    from itertools import product
    import random

    triangulo = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert colorear_grafo(triangulo, 2) is None
    assert colorear_grafo(triangulo, 3) is not None
    ciclo5 = {i: [(i - 1) % 5, (i + 1) % 5] for i in range(5)}   # ciclo impar: necesita 3
    assert colorear_grafo(ciclo5, 2) is None
    assert colorear_grafo(ciclo5, 3) is not None
    k4 = {i: [j for j in range(4) if j != i] for i in range(4)}
    assert colorear_grafo(k4, 3) is None
    assert colorear_grafo(k4, 4) is not None

    random.seed(3)
    for _ in range(200):
        n = random.randint(1, 6)
        aristas = {(a, b) for a in range(n) for b in range(a + 1, n) if random.random() < 0.5}
        grafo = {i: [] for i in range(n)}
        for a, b in aristas:
            grafo[a].append(b)
            grafo[b].append(a)
        for m in (1, 2, 3):
            esperado = any(all(col[a] != col[b] for a, b in aristas)
                           for col in product(range(m), repeat=n))
            res = colorear_grafo(grafo, m)
            assert (res is not None) == esperado, (grafo, m)
            if res is not None:
                assert all(res[a] != res[b] for a, b in aristas)
    print("OK")
