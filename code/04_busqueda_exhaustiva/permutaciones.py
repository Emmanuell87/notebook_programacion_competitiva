# Explora todas las posibles soluciones del espacio de busqueda.
# Ejemplo simple: generar todas las permutaciones de un arreglo.

from itertools import permutations


def generar_permutaciones(arr):
    return list(permutations(arr))


if __name__ == "__main__":
    perms = generar_permutaciones([1, 2, 3])
    assert len(perms) == 6
    assert (1, 2, 3) in perms
    assert (3, 2, 1) in perms
    print("OK")
