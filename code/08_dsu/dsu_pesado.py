# DSU con Pesos (Potenciado / Weighted DSU). Cuando las uniones no son
# solo "estan conectados si/no" sino que cargan una RELACION
# CUANTITATIVA entre nodos: diferencias (a-b=c), paridad, o distancia
# relativa. Ejemplos: "Food Chain" (3 especies ciclicas), o "dado un
# conjunto de restricciones a_i-a_j=c, decir si son consistentes y
# responder a_i-a_j=? para pares conectados".
#
# Idea: cada nodo guarda peso[x] = valor(x) - valor(raiz de su
# componente). Al unir imponiendo valor(x)-valor(y)=w, se resuelve
# algebraicamente el offset de la raiz que se cuelga. Si x e y ya
# estaban en el mismo componente, en vez de unir se VERIFICA
# CONSISTENCIA con lo que ya se sabia.


class DSUPesado:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.peso = [0] * n  # peso[x] = valor(x) - valor(raiz de x)

    def find(self, x):
        if self.parent[x] != x:
            padre = self.parent[x]
            raiz = self.find(padre)
            self.peso[x] += self.peso[padre]  # acumula el offset de todo el camino
            self.parent[x] = raiz
        return self.parent[x]

    def diff(self, x, y):
        # valor(x) - valor(y), asumiendo que x e y ya estan en el mismo componente
        self.find(x)
        self.find(y)
        return self.peso[x] - self.peso[y]

    def union(self, x, y, w):
        # impone valor(x) - valor(y) = w; devuelve False si w es inconsistente
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return (self.peso[x] - self.peso[y]) == w
        if self.rank[rx] < self.rank[ry]:
            rx, ry, x, y, w = ry, rx, y, x, -w
        self.parent[ry] = rx
        self.peso[ry] = self.peso[x] - self.peso[y] - w
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


if __name__ == "__main__":
    dp = DSUPesado(3)  # A=0, B=1, C=2
    assert dp.union(0, 1, 3)   # valor(A) - valor(B) = 3
    assert dp.union(1, 2, 2)   # valor(B) - valor(C) = 2
    assert dp.diff(0, 2) == 5  # valor(A) - valor(C) deberia ser 5
    assert dp.union(0, 2, 5) is True   # consistente
    assert dp.union(0, 2, 6) is False  # inconsistente

    dp2 = DSUPesado(4)
    assert dp2.union(0, 1, -2)  # A - B = -2
    assert dp2.union(2, 3, 4)   # C - D = 4
    assert dp2.union(1, 2, 1)   # B - C = 1
    # A - D = (A-B)+(B-C)+(C-D) = -2+1+4 = 3
    assert dp2.diff(0, 3) == 3
    print("OK")
