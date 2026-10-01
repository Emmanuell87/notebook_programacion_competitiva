# Divide matrices grandes en bloques de submatrices y reduce la
# cantidad de multiplicaciones de 8 a 7. Tiempo aproximado:
# O(n^log2(7)) ~= O(n^2.81). A, B = matrices cuadradas (lista de
# listas) del MISMO tamano n x n, y n debe ser potencia de 2 (si no lo
# es, rellenar con ceros -padding- hasta la potencia de 2 siguiente).
# En la practica, para n pequeno la multiplicacion normal O(n^3) suele
# ser mas rapida por la sobrecarga de las llamadas recursivas;
# Strassen rinde para n grande.


def sumar(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def restar(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(sumar(A11, A22), sumar(B11, B22))
    M2 = strassen(sumar(A21, A22), B11)
    M3 = strassen(A11, restar(B12, B22))
    M4 = strassen(A22, restar(B21, B11))
    M5 = strassen(sumar(A11, A12), B22)
    M6 = strassen(restar(A21, A11), sumar(B11, B12))
    M7 = strassen(restar(A12, A22), sumar(B21, B22))

    C11 = sumar(restar(sumar(M1, M4), M5), M7)
    C12 = sumar(M3, M5)
    C21 = sumar(M2, M4)
    C22 = sumar(restar(sumar(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    return C


def mult_normal(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert strassen(A, B) == mult_normal(A, B)

    A4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    B4 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]  # identidad
    assert strassen(A4, B4) == A4
    print("OK")
