# Frog (AtCoder DP A). Una rana en la piedra 0 quiere llegar a la
# piedra n-1 saltando a la piedra siguiente o saltando una piedra (dos
# posiciones), pagando un costo igual a la diferencia de alturas;
# minimizar el costo total. h = lista de alturas de las piedras. Es
# la plantilla mas simple de "DP sobre una linea con saltos de tamano
# limitado".


def frog(h):
    n = len(h)
    INF = 10 ** 18
    dp = [INF] * n
    dp[0] = 0
    for i in range(1, n):
        dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))
    return dp[-1]


if __name__ == "__main__":
    assert frog([10, 30, 40, 20]) == 30   # 10->30->20: |20|+|10|=30, o 10->40->20:30+20=50
    assert frog([10, 20, 10]) == 0        # 10->10 saltando: |0|
    assert frog([30, 10, 60, 10, 60, 50]) == 40
    print("OK")
