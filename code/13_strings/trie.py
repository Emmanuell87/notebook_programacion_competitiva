# Insertar y buscar palabras/prefijos en O(L), donde L es la longitud
# de la palabra. Util para autocompletado, conteo de prefijos,
# diccionarios. palabra/prefijo son strings; se usa como
# t = Trie(); t.insertar("casa"), etc. (el propio objeto raiz hace de
# nodo).
#
# Adaptable a: Trie binario de bits (para XOR maximo entre pares, ver
# la seccion de Manejo de Bits), reemplazando el diccionario hijos por
# dos entradas [0] y [1] y recorriendo el numero bit a bit.


class Trie:
    def __init__(self):
        self.hijos = {}        # letra -> Trie
        self.fin_palabra = False
        self.cont_prefijo = 0  # cuantas palabras pasan por este nodo

    def insertar(self, palabra):
        nodo = self
        nodo.cont_prefijo += 1
        for c in palabra:
            if c not in nodo.hijos:
                nodo.hijos[c] = Trie()
            nodo = nodo.hijos[c]
            nodo.cont_prefijo += 1
        nodo.fin_palabra = True

    def buscar(self, palabra):
        nodo = self
        for c in palabra:
            if c not in nodo.hijos:
                return False
            nodo = nodo.hijos[c]
        return nodo.fin_palabra

    def contar_con_prefijo(self, prefijo):
        nodo = self
        for c in prefijo:
            if c not in nodo.hijos:
                return 0
            nodo = nodo.hijos[c]
        return nodo.cont_prefijo


if __name__ == "__main__":
    t = Trie()
    for palabra in ["casa", "cama", "carro", "caballo"]:
        t.insertar(palabra)

    assert t.buscar("casa") is True
    assert t.buscar("cas") is False     # es prefijo, no palabra completa
    assert t.buscar("perro") is False
    assert t.contar_con_prefijo("ca") == 4
    assert t.contar_con_prefijo("cas") == 1
    assert t.contar_con_prefijo("z") == 0
    print("OK")
