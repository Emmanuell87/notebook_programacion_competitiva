# Cortar un cable de longitud n para maximizar la ganancia segun
# precios dados para cada longitud posible. precios[j-1] es lo que
# pagan por un trozo de longitud j (1-indexado en el enunciado,
# 0-indexado en la lista); n = longitud total del cable.


def cortar_cable(precios, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], precios[j - 1] + dp[i - j])
    return dp[n]


if __name__ == "__main__":
    # precios[0..7]: longitud 1..8 vale 1,5,8,9,10,17,17,20
    precios = [1, 5, 8, 9, 10, 17, 17, 20]
    assert cortar_cable(precios, 8) == 22  # 2+6 -> 5+17=22
    assert cortar_cable(precios, 4) == 10  # 2+2 -> 5+5=10
    print("OK")
