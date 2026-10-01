# Contar pares (i, j) tal que i < j y A[i] > A[j]. Se resuelve junto
# con MergeSort: cada vez que se toma un elemento de 'right' antes que
# uno de 'left' que quedaba pendiente, todos los pendientes de left
# forman una inversion con el.


def merge_count(arr):
    def merge_sort(arr):
        n = len(arr)
        if n <= 1:
            return arr, 0

        mid = n // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_merge = merge(left, right)

        return merged, inv_left + inv_right + inv_merge

    def merge(left, right):
        merged = [0] * (len(left) + len(right))
        i = j = k = inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged[k] = left[i]
                i += 1
            else:
                merged[k] = right[j]
                inv_count += len(left) - i  # Inversiones: todos los que faltan en left
                j += 1
            k += 1

        while i < len(left):
            merged[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            merged[k] = right[j]
            j += 1
            k += 1

        return merged, inv_count

    z, total_inversions = merge_sort(arr)
    return z, total_inversions


if __name__ == "__main__":
    ordenado, inv = merge_count([2, 4, 1, 3, 5])
    assert ordenado == [1, 2, 3, 4, 5]
    assert inv == 3, inv  # (2,1),(4,1),(4,3)

    _, inv2 = merge_count([5, 4, 3, 2, 1])
    assert inv2 == 10  # orden totalmente invertido: C(5,2)=10

    _, inv3 = merge_count([1, 2, 3])
    assert inv3 == 0
    print("OK")
