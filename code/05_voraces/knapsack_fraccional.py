# Maximizar el valor total que cabe en una mochila de capacidad
# limitada, permitiendo fracciones de objetos. A diferencia del
# knapsack 0-1 (seccion de DP), aqui si se permite tomar una fraccion
# de un objeto -- por eso es voraz y optimo.


def knapsack_fraccional(pesos, valores, capacidad):
    n = len(pesos)
    items = sorted(
        [(valores[i] / pesos[i], pesos[i], valores[i]) for i in range(n)],
        reverse=True
    )
    total = 0
    for ratio, peso, valor in items:
        if capacidad >= peso:
            capacidad -= peso
            total += valor
        else:
            total += ratio * capacidad
            break
    return total


if __name__ == "__main__":
    # objetos: (peso, valor) = (10,60),(20,100),(30,120); capacidad=50
    # ratios: 6, 5, 4 -> toma el 1ro completo(60), el 2do completo(100),
    # y 20/30 del 3ro = 80 -> total 240
    resultado = knapsack_fraccional([10, 20, 30], [60, 100, 120], 50)
    assert abs(resultado - 240) < 1e-9, resultado
    print("OK")
