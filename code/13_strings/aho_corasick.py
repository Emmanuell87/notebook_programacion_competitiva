# Busqueda de multiples patrones a la vez. Cuando tienes MUCHOS
# patrones (no uno solo) y quieres encontrar todas sus ocurrencias en
# un texto en una sola pasada. Con KMP tendrias que correrlo una vez
# por patron (O(M*|texto|) para M patrones); Aho-Corasick construye un
# Trie de todos los patrones y le agrega ENLACES DE FALLO (la misma
# idea del lps de KMP, pero generalizada sobre el arbol), respondiendo
# todo en O(|texto| + suma(|patrones|) + ocurrencias). Ejemplo tipico:
# filtro de palabras prohibidas, deteccion de firmas/virus.
#
# patrones = lista de strings. buscar(texto) devuelve una lista de
# (posicion_final, indice_del_patron) por cada coincidencia
# (posicion_final es 0-indexada, el indice del ultimo caracter).

from collections import deque


class AhoCorasick:
    def __init__(self, patrones):
        self.hijos = [{}]   # hijos[nodo][caracter] = nodo (aristas del trie)
        self.fail = [0]     # enlace de fallo de cada nodo
        self.salida = [[]]  # indices de patrones que terminan aqui (heredando de los fallos)
        for idx, p in enumerate(patrones):
            self._insertar(p, idx)
        self._construir_fallos()

    def _insertar(self, palabra, idx):
        nodo = 0
        for c in palabra:
            if c not in self.hijos[nodo]:
                self.hijos.append({})
                self.fail.append(0)
                self.salida.append([])
                self.hijos[nodo][c] = len(self.hijos) - 1
            nodo = self.hijos[nodo][c]
        self.salida[nodo].append(idx)

    def _ir(self, nodo, c):
        # transicion "on the fly": sigue enlaces de fallo si hace falta (como en KMP)
        while nodo != 0 and c not in self.hijos[nodo]:
            nodo = self.fail[nodo]
        return self.hijos[nodo][c] if c in self.hijos[nodo] else 0

    def _construir_fallos(self):
        q = deque()
        for hijo in self.hijos[0].values():
            self.fail[hijo] = 0
            q.append(hijo)
        while q:
            u = q.popleft()
            for c, v in self.hijos[u].items():
                self.fail[v] = self._ir(self.fail[u], c)
                self.salida[v] = self.salida[v] + self.salida[self.fail[v]]  # hereda coincidencias del fallo
                q.append(v)

    def buscar(self, texto):
        nodo = 0
        resultados = []
        for i, c in enumerate(texto):
            nodo = self._ir(nodo, c)
            for idx in self.salida[nodo]:
                resultados.append((i, idx))
        return resultados


if __name__ == "__main__":
    patrones = ["he", "she", "his", "hers"]
    ac = AhoCorasick(patrones)
    resultados = set(ac.buscar("ushers"))
    # ushers: u(0)s(1)h(2)e(3)r(4)s(5)
    assert (3, 0) in resultados  # "he"
    assert (3, 1) in resultados  # "she"
    assert (5, 3) in resultados  # "hers"
    assert len(resultados) == 3
    print("OK")
