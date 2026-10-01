import io
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


# ---------------------------------------------------------------
# Nivel 3 -- cuando el problema NO dice cuantos casos/lineas hay y
# hay que leer hasta que se acabe el input (EOF, "End Of File"):
#
#   resultado = []
#   try:
#       while True:
#           resultado.append(input())
#   except EOFError:
#       pass
#
# ---------------------------------------------------------------


def leer_hasta_eof(entrada_simulada=None):
    """Lee lineas hasta EOF con el patron de arriba. entrada_simulada:
    string con el input completo (para pruebas, reemplaza sys.stdin),
    o None para leer de sys.stdin de verdad."""
    if entrada_simulada is not None:
        sys.stdin = io.StringIO(entrada_simulada)

    resultado = []
    try:
        while True:
            resultado.append(input())
    except EOFError:
        pass
    return resultado


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

    lineas = leer_hasta_eof("hola\nmundo\n123\n")
    assert lineas == ["hola", "mundo", "123"], lineas

    print("OK")
