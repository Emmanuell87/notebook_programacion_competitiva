# Python tiene un limite de profundidad de recursion relativamente
# bajo (por defecto ~1000). Para recursion profunda (ej. DFS en un
# grafo/arbol desbalanceado con muchos nodos en cadena), hay que subir
# el limite al inicio del programa:
#
#   import sys
#   sys.setrecursionlimit(10**6)
#
# Esto NO siempre alcanza: por debajo tambien existe el limite real
# del stack de llamadas en C que usa el interprete, y una recursion
# MUY profunda puede terminar en un crash silencioso (segfault) en vez
# de un RecursionError, incluso con el limite ya subido. Para esos
# casos conviene pasar el algoritmo a forma iterativa con una pila
# explicita: nunca hay riesgo de desbordar nada, sin importar que tan
# profundo sea el grafo/arbol.


def dfs_recursivo(grafo, inicio):
    visitado = {inicio}
    orden = []

    def dfs(u):
        orden.append(u)
        for v in grafo[u]:
            if v not in visitado:
                visitado.add(v)
                dfs(v)

    dfs(inicio)
    return orden


def dfs_iterativo(grafo, inicio):
    """Mismo recorrido que dfs_recursivo, pero con una pila explicita
    en vez de recursion real."""
    visitado = {inicio}
    orden = []
    pila = [inicio]
    while pila:
        u = pila.pop()
        orden.append(u)
        for v in reversed(grafo[u]):
            if v not in visitado:
                visitado.add(v)
                pila.append(v)
    return orden


if __name__ == "__main__":
    grafo = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1],
    }
    assert dfs_recursivo(grafo, 0) == dfs_iterativo(grafo, 0)

    # grafo "en cadena" de 2000 nodos: con el limite de recursion por
    # defecto (~1000), dfs_recursivo tiraria RecursionError aqui.
    n = 2000
    cadena = {i: [i - 1, i + 1] for i in range(1, n - 1)}
    cadena[0] = [1]
    cadena[n - 1] = [n - 2]
    assert dfs_iterativo(cadena, 0) == list(range(n))

    print("OK")
