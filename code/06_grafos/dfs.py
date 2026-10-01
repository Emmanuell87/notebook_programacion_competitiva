# Recorrer un grafo en profundidad, util para exploracion completa y
# problemas como deteccion de ciclos o componentes conexas. grafo =
# diccionario {nodo: [vecinos]}; inicio = nodo de partida; visitado
# normalmente se deja en None (se crea solo) salvo que quieras
# acumular visitados entre varias llamadas, como hace
# componentes_conexas.py. Devuelve el conjunto de nodos visitados.


def dfs(grafo, inicio, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(inicio)
    for v in grafo[inicio]:
        if v not in visitado:
            dfs(grafo, v, visitado)
    return visitado


if __name__ == "__main__":
    grafo = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
    assert dfs(grafo, 0) == {0, 1, 2, 3, 4}
    assert dfs(grafo, 4) == {0, 1, 2, 3, 4}  # conexo, llega a todos
    print("OK")
