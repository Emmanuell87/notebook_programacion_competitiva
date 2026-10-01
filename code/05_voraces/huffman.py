# Construir un arbol binario para obtener codigos optimos de
# compresion segun la frecuencia de cada caracter. entrada = lista de
# tuplas (caracter, frecuencia). Cuando piden asignar codigos binarios
# de largo variable a simbolos segun su frecuencia, minimizando el
# largo total codificado (los mas frecuentes obtienen codigos mas
# cortos). construir_arbol_huffman devuelve la raiz;
# imprimir_rutas_a_hojas recorre el arbol y da el codigo ('0'/'1') de
# cada caracter.

import heapq


class Nodo:
    def __init__(self):
        self.left = None
        self.right = None
        self.freq = None
        self.char = None


def construir_arbol_huffman(entrada):
    heap = []
    heapq.heapify(heap)
    for char, freq in entrada:
        nodo = Nodo()
        nodo.char = char
        nodo.freq = freq
        heapq.heappush(heap, (nodo.freq, nodo.char, nodo))

    while len(heap) > 1:
        nodo = Nodo()
        left = heapq.heappop(heap)[2]
        right = heapq.heappop(heap)[2]
        nodo.left = left
        nodo.right = right
        nodo.freq = left.freq + right.freq
        nodo.char = left.char + right.char
        heapq.heappush(heap, (nodo.freq, nodo.char, nodo))

    return heap[0][2]  # Raiz del arbol


def codigos_por_caracter(nodo, camino='', codigos=None):
    if codigos is None:
        codigos = {}
    if nodo is None:
        return codigos
    if nodo.left is None and nodo.right is None:
        codigos[nodo.char] = camino or '0'
        return codigos
    codigos_por_caracter(nodo.left, camino + '0', codigos)
    codigos_por_caracter(nodo.right, camino + '1', codigos)
    return codigos


if __name__ == "__main__":
    entrada = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
    raiz = construir_arbol_huffman(entrada)
    codigos = codigos_por_caracter(raiz)

    # el caracter mas frecuente ('f') debe tener el codigo mas corto
    assert len(codigos['f']) <= min(len(codigos[c]) for c in 'abcde')
    # todos los codigos deben ser distintos (prefijo libre)
    assert len(set(codigos.values())) == 6
    print("OK")
