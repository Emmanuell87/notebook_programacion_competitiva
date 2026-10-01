# Diferencia clave con el DSU base: ese usa compresion de camino en
# find, lo cual "aplana" el arbol y DESTRUYE la informacion de como
# estaba antes, asi que no se puede deshacer una union barato. Esta
# version NO comprime camino (solo usa union por tamano, sigue siendo
# O(log n)) y guarda un historial explicito de que cambio en cada
# union, para poder revertirlo con rollback() en O(1).
#
# Cuando usar: conectividad dinamica OFFLINE -- aristas que solo
# "existen" durante un rango de tiempo/consultas (segment tree sobre
# el tiempo + DFS que hace union al entrar y rollback al salir).


class DSURollback:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.historial = []  # guarda que revertir en cada rollback()

    def find(self, x):
        while self.parent[x] != x:  # SIN compresion de camino (a proposito)
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            self.historial.append(None)  # no hubo cambio real, pero se registra
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.historial.append((b, a, self.size[a]))  # b se colgo de a; guarda tamano viejo de a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def rollback(self):
        # deshace la ultima union() realizada
        cambio = self.historial.pop()
        if cambio is None:
            return
        b, a, tam_viejo_a = cambio
        self.parent[b] = b
        self.size[a] = tam_viejo_a


if __name__ == "__main__":
    d = DSURollback(5)
    assert d.find(0) != d.find(1)
    d.union(0, 1)
    d.union(2, 3)
    assert d.find(0) == d.find(1)
    assert d.find(2) == d.find(3)
    d.union(1, 2)
    assert d.find(0) == d.find(3)  # todos conectados 0-1-2-3
    d.rollback()  # deshace union(1,2)
    assert d.find(0) == d.find(1)
    assert d.find(2) == d.find(3)
    assert d.find(0) != d.find(2)  # separados otra vez
    d.rollback()  # deshace union(2,3)
    assert d.find(2) != d.find(3)
    d.rollback()  # deshace union(0,1)
    assert d.find(0) != d.find(1)
    print("OK")
