# Encontrar todas las componentes conexas en un grafo no dirigido.
# grafo = diccionario {nodo: [vecino1, vecino2, ...]}. dfs() recibe un
# set() compartido para ir acumulando visitados entre varias llamadas.


def dfs(grafo, inicio, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(inicio)
    for v in grafo[inicio]:
        if v not in visitado:
            dfs(grafo, v, visitado)
    return visitado


def componentes_conexas(grafo):
    visitado = set()
    componentes = []

    for nodo in grafo:
        if nodo not in visitado:
            comp = set()
            dfs(grafo, nodo, comp)
            componentes.append(comp)
            visitado |= comp
    return componentes


if __name__ == "__main__":
    # dos componentes: {0,1,2} y {3,4}
    grafo = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}
    comps = componentes_conexas(grafo)
    assert len(comps) == 2
    assert {0, 1, 2} in comps
    assert {3, 4} in comps
    print("OK")
