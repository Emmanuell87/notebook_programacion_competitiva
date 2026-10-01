class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]


if __name__ == "__main__":
    dsu = DSU(5)
    assert dsu.find(0) != dsu.find(1)
    dsu.union(0, 1)
    dsu.union(1, 2)
    assert dsu.find(0) == dsu.find(2)
    assert dsu.find(3) != dsu.find(0)
    dsu.union(3, 4)
    assert dsu.find(3) == dsu.find(4)
    assert dsu.find(0) != dsu.find(3)
    print("OK")
