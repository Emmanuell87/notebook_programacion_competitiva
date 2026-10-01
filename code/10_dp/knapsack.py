# Maximizar el valor de los objetos seleccionados sin exceder una
# capacidad, con cada objeto incluido o no (a diferencia del
# fraccional de Voraces, aqui NO se pueden partir objetos).
# O(n * capacidad) -- solo viable si capacidad no es demasiado grande.


def knapsack(pesos, valores, capacidad):
    n = len(pesos)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidad]


if __name__ == "__main__":
    pesos = [1, 3, 4, 5]
    valores = [1, 4, 5, 7]
    assert knapsack(pesos, valores, 7) == 9  # objetos de peso 3 y 4 -> valor 4+5=9
    assert knapsack(pesos, valores, 0) == 0
    print("OK")
