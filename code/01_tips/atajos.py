from collections import defaultdict, deque
import heapq


def leer_enteros_de_linea(linea):
    return list(map(int, linea.split()))


def ejemplo_defaultdict(arr):
    freq = defaultdict(int)
    for x in arr:
        freq[x] += 1
    return dict(freq)


def ejemplo_deque():
    # deque es O(1) tanto al principio como al final; una lista normal
    # es O(n) para insertar/sacar del principio.
    cola = deque()
    cola.append(1)
    cola.append(2)
    cola.appendleft(0)
    primero = cola.popleft()
    return primero, list(cola)


def ejemplo_heap(valores):
    heap = []
    for x in valores:
        heapq.heappush(heap, x)
    minimo = heapq.heappop(heap)
    return minimo, heap


def ejemplo_pow_mod(a, b, mod):
    return pow(a, b, mod)


def ejemplo_inverso_modular(a, mod):
    # funciona con cualquier mod (no solo primos) mientras gcd(a, mod) == 1
    return pow(a, -1, mod)


if __name__ == "__main__":
    assert leer_enteros_de_linea("1 2 3 4") == [1, 2, 3, 4]
    assert ejemplo_defaultdict([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert ejemplo_deque() == (0, [1, 2])
    minimo, resto_heap = ejemplo_heap([5, 1, 8, 2])
    assert minimo == 1

    assert ejemplo_pow_mod(2, 10, 1000) == 24
    inv = ejemplo_inverso_modular(3, 7)
    assert (3 * inv) % 7 == 1, inv

    print("OK")
