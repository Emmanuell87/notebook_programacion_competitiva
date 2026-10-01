# Arbol Binario de Busqueda Optimo (Optimal BST). Dadas probabilidades
# de busqueda para claves (ya ordenadas), construir el arbol de
# busqueda binaria con costo esperado minimo. freq = lista de
# frecuencias/pesos de busqueda de cada clave. Devuelve el costo
# minimo esperado (suma ponderada de profundidades), no el arbol
# construido.


def optimal_bst(freq):
    n = len(freq)
    dp = [[0] * n for _ in range(n)]
    suma = [[0] * n for _ in range(n)]

    for i in range(n):
        suma[i][i] = freq[i]
        dp[i][i] = freq[i]  # caso base: subarbol de un solo nodo cuesta su propia frecuencia
        for j in range(i + 1, n):
            suma[i][j] = suma[i][j - 1] + freq[j]

    for l in range(2, n + 1):  # longitud
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for r in range(i, j + 1):
                costo_izq = dp[i][r - 1] if r > i else 0
                costo_der = dp[r + 1][j] if r < j else 0
                dp[i][j] = min(dp[i][j], costo_izq + costo_der + suma[i][j])

    return dp[0][n - 1]


if __name__ == "__main__":
    # claves con frecuencias 34, 10, 8, 50 (ejemplo clasico)
    freq = [34, 10, 8, 50]
    assert optimal_bst(freq) == 180
    # un solo elemento: costo = su propia frecuencia
    assert optimal_bst([5]) == 5
    print("OK")
