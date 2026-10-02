# Estadistico de Orden k (QuickSelect). Encontrar el k-esimo menor
# elemento en O(n) promedio. k es 0-indexado. Modifica arr en el
# lugar (particiona, como quicksort).

import random


def quickselect_inplace(arr, k):
    def partition(l, r):
        pivot_index = random.randint(l, r)  # pivote aleatorio evita el peor caso O(n^2)
        arr[l], arr[pivot_index] = arr[pivot_index], arr[l]
        pivot = arr[l]

        i = l
        for j in range(l + 1, r + 1):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[i] = arr[i], arr[l]
        return i  # nueva posicion del pivote

    l, r = 0, len(arr) - 1
    while l <= r:
        pivot_index = partition(l, r)
        if pivot_index == k:
            return arr[pivot_index]
        elif k < pivot_index:
            r = pivot_index - 1
        else:
            l = pivot_index + 1


if __name__ == "__main__":
    # --- ejemplo ---
    arr = [7, 10, 4, 3, 20, 15]
    assert quickselect_inplace(arr[:], 0) == 3    # el menor (k es 0-indexado)
    assert quickselect_inplace(arr[:], 2) == 7    # el 3er menor
    assert quickselect_inplace(arr[:], 5) == 20   # el mayor
    # --- fin ejemplo ---
    arr = [7, 10, 4, 3, 20, 15]
    ordenado = sorted(arr)
    for k in range(len(arr)):
        copia = arr[:]
        assert quickselect_inplace(copia, k) == ordenado[k], k
    print("OK")
