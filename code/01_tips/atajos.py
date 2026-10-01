from collections import defaultdict, deque
import heapq

# List comprehension rapida:
#   arr = list(map(int, input().split()))
#   matriz = [list(map(int, input().split())) for _ in range(n)]

# Diccionario con valor por defecto:
#   from collections import defaultdict
#   freq = defaultdict(int)

# Cola eficiente:
#   from collections import deque
#   cola = deque()
#   cola.append(x)
#   x = cola.popleft()

# Heap (minimo por defecto):
#   import heapq
#   heapq.heappush(heap, valor)
#   x = heapq.heappop(heap)


def ejemplo_defaultdict(arr):
    freq = defaultdict(int)
    for x in arr:
        freq[x] += 1
    return dict(freq)


def ejemplo_deque():
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


if __name__ == "__main__":
    assert ejemplo_defaultdict([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert ejemplo_deque() == (0, [1, 2])
    minimo, resto_heap = ejemplo_heap([5, 1, 8, 2])
    assert minimo == 1
    print("OK")
