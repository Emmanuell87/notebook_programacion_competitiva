import sys

# ---------------------------------------------------------------
# Nivel 1 -- reemplazo simple de input(), se usa exactamente igual:
#
#   import sys
#   input = sys.stdin.readline
#
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Nivel 2 -- leer TODO el input de una sola vez. El patron que se
# pega tal cual al inicio de una solucion real es:
#
#   import sys
#   data = sys.stdin.buffer.read().split()
#   idx = 0
#
#   def leer_int():
#       global idx
#       val = int(data[idx]); idx += 1
#       return val
#
#   def leer_ints(k):
#       return [leer_int() for _ in range(k)]
#
# Aqui abajo esta la misma idea pero envuelta en una funcion (con
# closures en vez de variables globales) para poder probarla con
# distintos inputs de prueba sin reiniciar el interprete.
# ---------------------------------------------------------------


def leer_tokens(fuente=None):
    """Devuelve (leer_int, leer_ints) que consumen tokens en orden.
    fuente: string con el input completo (para pruebas), o None
    para leer de sys.stdin de verdad."""
    if fuente is None:
        data = sys.stdin.buffer.read().split()
    else:
        data = fuente.split()

    idx = 0

    def leer_int():
        nonlocal idx
        val = int(data[idx])
        idx += 1
        return val

    def leer_ints(k):
        return [leer_int() for _ in range(k)]

    return leer_int, leer_ints


if __name__ == "__main__":
    entrada_simulada = "3\n4\n1 2 3 4\n2\n10 20\n5\n5 4 3 2 1\n"
    leer_int, leer_ints = leer_tokens(entrada_simulada)

    T = leer_int()
    resultados = []
    for _ in range(T):
        n = leer_int()
        arr = leer_ints(n)
        resultados.append(sum(arr))

    assert resultados == [10, 30, 15], resultados
    print("OK")
