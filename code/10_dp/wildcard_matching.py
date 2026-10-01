# Verificar si una cadena s coincide con un patron p que puede incluir
# comodines: '?' reemplaza exactamente un caracter, '*' reemplaza
# cualquier secuencia (incluso vacia). s = texto normal; p = patron.
# Devuelve True/False si p coincide con s COMPLETA (no busca
# substrings).


def wildcard_matching(s, p):
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[n][m]


if __name__ == "__main__":
    assert wildcard_matching("aa", "a") is False
    assert wildcard_matching("aa", "*") is True
    assert wildcard_matching("cb", "?a") is False
    assert wildcard_matching("adceb", "*a*b") is True
    assert wildcard_matching("acdcb", "a*c?b") is False
    print("OK")
