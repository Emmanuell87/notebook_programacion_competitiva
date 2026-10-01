# Cuando necesitas un multiconjunto dinamico (insertar/eliminar
# elementos) y preguntar rapidamente "cuantos elementos son <= x?" o
# "cual es el k-esimo elemento mas chico?" -- como el
# order_of_key/find_by_order de un ordered set en C++, pero en Python.
#
# OrderStatMultiset(universe) recibe universe = lista con TODOS los
# valores que podrian insertarse (se usa para comprimir coordenadas);
# add(x)/remove(x) insertan/quitan x (debe estar en universe),
# rank_le(x) cuenta cuantos elementos actualmente insertados son <=x,
# y kth_value(k) da el valor en la posicion k (0-indexado) si se
# ordenaran los insertados.


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.ft = [0] * (n + 1)

    def add(self, i, v=1):
        i += 1
        while i <= self.n:
            self.ft[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.ft[i]
            i -= i & -i
        return s

    def kth(self, k):  # devuelve indice 0-based con prefijo > k
        i = 0
        bit = 1 << (self.n.bit_length())
        while bit:
            t = i + bit
            if t <= self.n and self.ft[t] <= k:
                k -= self.ft[t]
                i = t
            bit >>= 1
        return i


class OrderStatMultiset:
    def __init__(self, universe):
        self.coords = sorted(set(universe))
        self.pos = {v: i for i, v in enumerate(self.coords)}
        self.ft = Fenwick(len(self.coords) + 2)

    def add(self, x):
        self.ft.add(self.pos[x], 1)

    def remove(self, x):
        self.ft.add(self.pos[x], -1)

    def rank_le(self, x):
        return self.ft.sum(self.pos[x])  # #<=x

    def kth_value(self, k):
        return self.coords[self.ft.kth(k)]  # k: 0-based


if __name__ == "__main__":
    universo = [5, 1, 9, 3, 7]
    oss = OrderStatMultiset(universo)
    oss.add(5)
    oss.add(1)
    oss.add(9)
    assert oss.rank_le(5) == 2  # 1 y 5
    assert oss.kth_value(0) == 1   # el menor insertado
    assert oss.kth_value(2) == 9   # el tercer menor (1,5,9)
    oss.remove(5)
    assert oss.rank_le(5) == 1
    assert oss.kth_value(1) == 9   # ahora solo quedan 1,9
    print("OK")
