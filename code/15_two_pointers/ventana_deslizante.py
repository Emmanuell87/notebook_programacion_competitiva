# Ventana deslizante: ambos punteros avanzan en la misma direccion.
# Cuando usar: problemas de "subarreglo contiguo mas largo/corto/
# cantidad que cumple una condicion" cuando agregar elementos por la
# derecha y quitar por la izquierda mantiene la monotonia de la
# condicion (ej. sumas con elementos positivos, conteo de distintos).

from collections import defaultdict


def subarreglo_mas_largo_suma_max(arr, S):
    # requiere que todos los elementos sean positivos, para que la
    # suma sea monotona al mover los punteros
    izq = 0
    suma = 0
    mejor = 0
    for der in range(len(arr)):
        suma += arr[der]
        while suma > S:  # la ventana se paso, achicarla por la izquierda
            suma -= arr[izq]
            izq += 1
        mejor = max(mejor, der - izq + 1)
    return mejor


def contar_subarreglos_a_lo_sumo_k_distintos(arr, k):
    # patron "at most K", muy frecuente; para "exactamente K" se
    # resuelve como a_lo_sumo(K) - a_lo_sumo(K-1)
    freq = defaultdict(int)
    izq = 0
    distintos = 0
    total = 0
    for der in range(len(arr)):
        if freq[arr[der]] == 0:
            distintos += 1
        freq[arr[der]] += 1
        while distintos > k:
            freq[arr[izq]] -= 1
            if freq[arr[izq]] == 0:
                distintos -= 1
            izq += 1
        total += der - izq + 1  # cuenta subarreglos [i..der] validos con i entre izq y der
    return total


def fuerza_bruta_suma_max(arr, S):
    n = len(arr)
    mejor = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s <= S:
                mejor = max(mejor, j - i + 1)
    return mejor


def fuerza_bruta_a_lo_sumo_k(arr, k):
    n = len(arr)
    cnt = 0
    for i in range(n):
        vistos = set()
        for j in range(i, n):
            vistos.add(arr[j])
            if len(vistos) <= k:
                cnt += 1
            else:
                break
    return cnt


if __name__ == "__main__":
    import random
    random.seed(1)
    for _ in range(100):
        n = random.randint(1, 15)
        arr = [random.randint(1, 10) for _ in range(n)]
        S = random.randint(1, 50)
        assert subarreglo_mas_largo_suma_max(arr, S) == fuerza_bruta_suma_max(arr, S)

    random.seed(2)
    for _ in range(100):
        n = random.randint(1, 15)
        arr = [random.randint(1, 5) for _ in range(n)]
        k = random.randint(1, 5)
        assert contar_subarreglos_a_lo_sumo_k_distintos(arr, k) == fuerza_bruta_a_lo_sumo_k(arr, k)
    print("OK")
