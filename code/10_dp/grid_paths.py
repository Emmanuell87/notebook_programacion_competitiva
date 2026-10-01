# Caminos en grilla (DP con obstaculos). Contar caminos desde la
# esquina (0,0) hasta (n-1,m-1) moviendose solo hacia abajo o hacia la
# derecha, evitando celdas bloqueadas. n,m = dimensiones de la
# grilla; blocked = lista (o None) de (i,j) bloqueadas. Devuelve el
# conteo modulo 10^9+7.


def grid_paths(n, m, blocked=None):
    MOD = 10 ** 9 + 7
    blk = set(blocked or [])
    dp = [[0] * m for _ in range(n)]
    if (0, 0) not in blk:
        dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if (i, j) in blk:
                dp[i][j] = 0
            else:
                if i:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
                if j:
                    dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    assert grid_paths(3, 3) == 6  # C(4,2) caminos sin obstaculos
    assert grid_paths(3, 3, blocked=[(1, 1)]) == 2  # bloquear el centro
    assert grid_paths(2, 2, blocked=[(0, 0)]) == 0  # el inicio esta bloqueado
    print("OK")
