# Dada una lista con valores que alternan alguna propiedad (color,
# signo, paridad...), contar cuantas subsecuencias NO VACIAS
# conservan esta alternancia. cadena = string o lista donde cada
# elemento es 'R' o 'A' (u otra pareja de valores, si adaptas la
# condicion). Se puede adaptar para signo, par-impar, etc.


def contar_subs_alternantes(cadena):
    n = len(cadena)
    # dp[i][0] = cantidad de subsecuencias alternantes en cadena[0..i]
    # que terminan en 'R'; dp[i][1] = idem terminando en 'A' (cuenta
    # ACUMULADA hasta la posicion i, no solo "las que usan cadena[i]")
    dp = [[0, 0] for _ in range(n)]

    if cadena[0] == 'R':
        dp[0][0] = 1
    else:
        dp[0][1] = 1

    for i in range(1, n):
        if cadena[i] == 'R':
            # se preservan las que ya terminaban en R (no usan cadena[i]),
            # se suman las que terminaban en A extendidas con este R,
            # y se suma el propio cadena[i] como subsecuencia nueva de largo 1
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + 1
            dp[i][1] = dp[i - 1][1]
        else:
            dp[i][1] = dp[i - 1][1] + dp[i - 1][0] + 1
            dp[i][0] = dp[i - 1][0]

    # el total final ya esta acumulado en la ULTIMA fila; no hay que sumar todas las filas
    return dp[n - 1][0] + dp[n - 1][1]


if __name__ == "__main__":
    # "R" sola, "A" sola, "RA" -> 3 subsecuencias alternantes
    assert contar_subs_alternantes("RA") == 3
    # "RAR": R, A, R, RA, AR, RAR = 6
    assert contar_subs_alternantes("RAR") == 6
    print("OK")
