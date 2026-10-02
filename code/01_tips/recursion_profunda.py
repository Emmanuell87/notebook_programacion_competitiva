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
    """Mismo orden de visita que dfs_recursivo, con una pila explicita.
    Se marca al SACAR de la pila (no al meter): si se marcara al meter,
    el orden podria diferir del recursivo."""
    visitado = set()
    orden = []
    pila = [inicio]
    while pila:
        u = pila.pop()
        if u in visitado:
            continue
        visitado.add(u)
        orden.append(u)
        for v in reversed(grafo[u]):   # reversed: .pop() saca el ultimo apilado
            if v not in visitado:
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

    # un grafo donde marcar al apilar daria otro orden: 0,1,3,2 en vez de 0,1,2,3
    g2 = {0: [1, 2], 1: [2, 3], 2: [], 3: []}
    assert dfs_recursivo(g2, 0) == dfs_iterativo(g2, 0) == [0, 1, 2, 3]

    import random
    random.seed(1)
    for _ in range(1000):
        n = random.randint(2, 8)
        g = {i: [] for i in range(n)}
        for _ in range(random.randint(1, 12)):
            a, b = random.randrange(n), random.randrange(n)
            if a != b and b not in g[a]:
                g[a].append(b)
                g[b].append(a)
        assert dfs_recursivo(g, 0) == dfs_iterativo(g, 0), g

    # grafo "en cadena" de 2000 nodos: con el limite de recursion por
    # defecto (~1000), dfs_recursivo tiraria RecursionError aqui.
    n = 2000
    cadena = {i: [i - 1, i + 1] for i in range(1, n - 1)}
    cadena[0] = [1]
    cadena[n - 1] = [n - 2]
    assert dfs_iterativo(cadena, 0) == list(range(n))

    print("OK")
