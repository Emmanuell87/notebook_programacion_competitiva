# Divide el arreglo en dos mitades, ordena recursivamente, y luego
# fusiona.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])
    return merge(izq, der)


def merge(a, b):
    resultado = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    return resultado + a[i:] + b[j:]


if __name__ == "__main__":
    assert merge_sort([5, 2, 8, 1, 9, 3]) == [1, 2, 3, 5, 8, 9]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    print("OK")
