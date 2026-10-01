# Multiplicacion en Cadena de Matrices. Dadas n matrices A1..An,
# determinar el orden optimo de multiplicacion que minimiza el numero
# total de operaciones escalares. p = lista de n+1 enteros (las
# dimensiones: A_i es p[i-1] x p[i]); no recibe las matrices en si.
# Devuelve solo el COSTO MINIMO, no el orden de parentesis a usar.


def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):  # longitud de la subsecuencia
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                costo = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], costo)

    return dp[0][n - 1]


if __name__ == "__main__":
    # matrices de dimensiones 10x20, 20x30, 30x40, 40x30
    p = [10, 20, 30, 40, 30]
    assert matrix_chain_order(p) == 30000
    print("OK")
