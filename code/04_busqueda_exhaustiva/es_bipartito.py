# Backtracking para 2-coloreo. grafo = diccionario {nodo: [vecinos]}.
# Para saber si un grafo es bipartito (2-coloreable); si dfs devuelve
# False en algun punto, el grafo NO es bipartito.


def es_bipartito(grafo):
    color = {}

    def dfs(v, c):
        if v in color:
            return color[v] == c
        color[v] = c
        return all(dfs(u, 1 - c) for u in grafo[v])

    return all(dfs(v, 0) for v in grafo if v not in color)


if __name__ == "__main__":
    # ciclo de 4 (bipartito)
    grafo_par = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
    assert es_bipartito(grafo_par) is True

    # triangulo (ciclo impar, NO bipartito)
    grafo_impar = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert es_bipartito(grafo_impar) is False

    # grafo desconectado, ambas componentes bipartitas
    grafo_desconectado = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert es_bipartito(grafo_desconectado) is True
    print("OK")
