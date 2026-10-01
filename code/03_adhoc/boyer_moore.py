# Encuentra el candidato a mayoria. Cuando el problema garantiza que
# existe un elemento que aparece mas de n/2 veces en arr, en O(n) y
# O(1) memoria. OJO: el resultado es solo un CANDIDATO -- si el
# problema no garantiza mayoria estricta, hay que verificar contando
# de nuevo cuantas veces aparece.


def boyer_moore(arr):
    count, candidate = 0, None
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate


if __name__ == "__main__":
    assert boyer_moore([2, 2, 1, 1, 1, 2, 2]) == 2
    assert boyer_moore([3, 3, 4, 2, 3, 3, 3]) == 3
    assert boyer_moore([5]) == 5
    print("OK")
