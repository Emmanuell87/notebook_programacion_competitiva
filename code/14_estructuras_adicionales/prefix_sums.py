# Cuando necesitas responder MUCHAS consultas de "suma en un
# rango/rectangulo/prisma fijo" sobre un arreglo que NO CAMBIA (si
# cambia, usa Segment Tree o Fenwick en su lugar). Preprocesamiento
# O(n)/O(nm)/O(XYZ), cada consulta O(1).
#
# pref1d(a) recibe una lista; el resultado p se consulta como
# p[r+1]-p[l] para la suma de a[l..r] (0-indexado, inclusive).
# pref2d(A) recibe una matriz; pref3d(A) un arreglo 3D (lista de
# matrices) -- ambas devuelven arreglos "prefijo" 1-indexados
# internamente, pensados para consultarse con inclusion-exclusion
# (sumar/restar esquinas) igual que pref1d.


def pref1d(a):
    p = [0] * (len(a) + 1)
    for i, x in enumerate(a, 1):
        p[i] = p[i - 1] + x
    return p  # sum[l..r]=p[r+1]-p[l]


def pref2d(A):
    n, m = len(A), len(A[0])
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        fila = 0
        for j in range(1, m + 1):
            fila += A[i - 1][j - 1]
            P[i][j] = P[i - 1][j] + fila
    return P  # suma rectangulo 1-index


def pref3d(A):
    X, Y, Z = len(A), len(A[0]), len(A[0][0])
    P = [[[0] * (Z + 1) for _ in range(Y + 1)] for __ in range(X + 1)]
    for x in range(1, X + 1):
        for y in range(1, Y + 1):
            for z in range(1, Z + 1):
                P[x][y][z] = A[x - 1][y - 1][z - 1] \
                    + P[x - 1][y][z] + P[x][y - 1][z] + P[x][y][z - 1] \
                    - P[x - 1][y - 1][z] - P[x - 1][y][z - 1] - P[x][y - 1][z - 1] \
                    + P[x - 1][y - 1][z - 1]
    return P


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    p = pref1d(a)
    assert p[5] - p[0] == sum(a)
    assert p[3] - p[1] == a[1] + a[2]  # suma de a[1..2]

    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    P = pref2d(A)
    # suma del rectangulo completo
    assert P[3][3] - P[0][3] - P[3][0] + P[0][0] == sum(sum(fila) for fila in A)
    # suma del rectangulo A[1:3][1:3] (filas 1-2, cols 1-2) = 5+6+8+9=28
    assert P[3][3] - P[1][3] - P[3][1] + P[1][1] == 28

    A3 = [[[1] * 2 for _ in range(2)] for _ in range(2)]  # cubo 2x2x2 de unos
    P3 = pref3d(A3)
    assert P3[2][2][2] == 8  # suma de los 8 unos
    print("OK")
