# Circuito/camino euleriano (recorre cada arista exactamente una vez) en
# un grafo NO dirigido. aristas = lista de (u, v); se admiten aristas
# repetidas. Devuelve la lista de vertices del recorrido, o None si no
# existe. Existe si las aristas estan conectadas y hay 0 o 2 vertices de
# grado impar (con 2, el camino empieza en uno de ellos). Es iterativo.


def circuito_euleriano(n, aristas):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(aristas):
        adj[u].append((v, i))
        adj[v].append((u, i))
    impares = [v for v in range(n) if len(adj[v]) % 2]
    if len(impares) not in (0, 2):
        return None
    inicio = impares[0] if impares else next((v for v in range(n) if adj[v]), 0)

    usada = [False] * len(aristas)
    ptr = [0] * n
    pila = [inicio]
    camino = []
    while pila:
        u = pila[-1]
        while ptr[u] < len(adj[u]) and usada[adj[u][ptr[u]][1]]:
            ptr[u] += 1
        if ptr[u] == len(adj[u]):
            camino.append(pila.pop())      # sin aristas libres: va al camino final
        else:
            v, i = adj[u][ptr[u]]
            usada[i] = True
            pila.append(v)
    if len(camino) != len(aristas) + 1:
        return None                        # las aristas no estan todas conectadas
    return camino[::-1]


if __name__ == "__main__":
    # --- ejemplo ---
    # triangulo: circuito (empieza y termina en el mismo vertice)
    assert circuito_euleriano(3, [(0, 1), (1, 2), (2, 0)]) == [0, 1, 2, 0]
    # camino de 2 aristas: empieza en un vertice de grado impar
    assert circuito_euleriano(3, [(0, 1), (1, 2)]) == [0, 1, 2]
    # tres vertices de grado impar: no existe
    assert circuito_euleriano(4, [(0, 1), (0, 2), (0, 3)]) is None
    # --- fin ejemplo ---
    import random

    assert circuito_euleriano(3, [(0, 1), (1, 2), (2, 0)]) is not None   # triangulo: circuito
    camino = circuito_euleriano(3, [(0, 1), (1, 2)])
    assert camino in ([0, 1, 2], [2, 1, 0])                               # camino de 2 aristas
    assert circuito_euleriano(4, [(0, 1), (0, 2), (0, 3)]) is None        # 3 vertices impares

    def usa_cada_arista(camino, aristas):
        pares = sorted(tuple(sorted(p)) for p in zip(camino, camino[1:]))
        return pares == sorted(tuple(sorted(a)) for a in aristas)

    def existe(n, aristas):
        grado = [0] * n
        padre = list(range(n))

        def f(x):
            while padre[x] != x:
                padre[x] = padre[padre[x]]
                x = padre[x]
            return x
        for u, v in aristas:
            grado[u] += 1
            grado[v] += 1
            padre[f(u)] = f(v)
        con_aristas = {f(v) for v in range(n) if grado[v]}
        return len(con_aristas) <= 1 and sum(g % 2 for g in grado) in (0, 2)

    random.seed(4)
    for _ in range(600):
        n = random.randint(1, 6)
        aristas = [(random.randrange(n), random.randrange(n)) for _ in range(random.randint(0, 9))]
        res = circuito_euleriano(n, aristas)
        assert (res is not None) == existe(n, aristas), (n, aristas)
        if res is not None:
            assert usa_cada_arista(res, aristas), (aristas, res)
            assert len(res) == len(aristas) + 1
    print("OK")
