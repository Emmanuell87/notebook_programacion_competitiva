# Distancia de Edicion (Wagner-Fischer). Calcular el minimo numero de
# operaciones (insercion, borrado, sustitucion) necesarias para
# transformar una cadena en otra. a, b = strings.


def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # eliminar
                    dp[i][j - 1],      # insertar
                    dp[i - 1][j - 1],  # sustituir
                )

    return dp[n][m]


if __name__ == "__main__":
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("abc", "abc") == 0
    print("OK")
