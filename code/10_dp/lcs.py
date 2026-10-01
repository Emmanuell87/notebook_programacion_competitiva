# Mayor Subsecuencia Comun (LCS). Calcular la longitud de la
# subsecuencia comun mas larga entre dos cadenas. a, b = strings (o
# listas) cualesquiera. Es SUBSECUENCIA (no tiene que ser contigua),
# distinto de "substring comun mas largo".


def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[n][m]


if __name__ == "__main__":
    assert lcs("ABCBDAB", "BDCABA") == 4  # "BCBA" o "BDAB"
    assert lcs("abc", "abc") == 3
    assert lcs("abc", "xyz") == 0
    print("OK")
