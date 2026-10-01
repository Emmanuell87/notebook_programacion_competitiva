# Complejidad promedio O(n log n), peor caso O(n^2).


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menores = [x for x in arr[1:] if x <= pivot]
    mayores = [x for x in arr[1:] if x > pivot]
    return quicksort(menores) + [pivot] + quicksort(mayores)


if __name__ == "__main__":
    assert quicksort([5, 2, 8, 1, 9, 3]) == [1, 2, 3, 5, 8, 9]
    assert quicksort([]) == []
    assert quicksort([3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3]
    print("OK")
