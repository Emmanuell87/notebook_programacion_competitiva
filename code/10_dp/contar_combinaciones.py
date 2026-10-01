# Contar de cuantas formas se puede obtener una suma exacta N al
# lanzar un dado multiples veces (cada cara vale entre 1 y 6).
# Generalizacion: particiones con repeticiones ilimitadas usando
# enteros dados (el orden de tiradas SI importa, a diferencia de
# contar_monedas que cuenta combinaciones sin importar el orden).


def contar_combinaciones(n, caras=[1, 2, 3, 4, 5, 6]):
    dp = [0] * (n + 1)
    dp[0] = 1  # base: una forma de obtener suma 0

    for i in range(1, n + 1):
        for cara in caras:
            if i - cara >= 0:
                dp[i] += dp[i - cara]

    return dp[n]


if __name__ == "__main__":
    assert contar_combinaciones(1) == 1   # [1]
    assert contar_combinaciones(2) == 2   # [1,1],[2]
    assert contar_combinaciones(3) == 4   # [1,1,1],[1,2],[2,1],[3]
    print("OK")
