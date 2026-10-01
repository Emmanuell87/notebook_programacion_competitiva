# Dado un monto n y monedas de distintas denominaciones, contar de
# cuantas formas se puede formar ese monto usando cada moneda una
# cantidad ilimitada de veces. IMPORTANTE: el orden de los bucles
# (moneda afuera, monto adentro) hace que cuente COMBINACIONES (no
# importa el orden en que se usan las monedas); si se invirtiera el
# orden de los bucles, contaria PERMUTACIONES (ver
# contar_combinaciones.py, que SI cuenta orden) -- vigila cual pide
# el enunciado.


def contar_monedas(monedas, n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for moneda in monedas:
        for i in range(moneda, n + 1):
            dp[i] += dp[i - moneda]

    return dp[n]


if __name__ == "__main__":
    # monedas 1,2,5 para formar 5: {1+1+1+1+1},{1+1+1+2},{1+2+2},{5} = 4 formas
    assert contar_monedas([1, 2, 5], 5) == 4
    assert contar_monedas([2], 3) == 0  # imposible formar 3 solo con monedas de 2
    assert contar_monedas([1], 4) == 1
    print("OK")
