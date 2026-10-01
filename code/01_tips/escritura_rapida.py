import sys

# ---------------------------------------------------------------
# Nivel 1 -- en vez de hacer print(x) una vez por cada resultado
# dentro de un loop (lento: cada llamada a print tiene overhead),
# se acumulan los resultados en una lista y se imprimen todos
# juntos al final con un solo print:
#
#   salida = []
#   for ...:
#       salida.append(str(resultado))
#   print('\n'.join(salida))
#
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Nivel 2 -- para volumenes todavia mas grandes de salida,
# sys.stdout.write evita el overhead extra que tiene print
# (parseo de argumentos, sep, end, flush). Hay que agregar el '\n'
# a mano porque write no lo pone solo:
#
#   import sys
#   salida = []
#   for ...:
#       salida.append(str(resultado))
#   sys.stdout.write('\n'.join(salida) + '\n')
#
# ---------------------------------------------------------------


def armar_salida(resultados):
    """Devuelve el string final listo para imprimir de una sola vez
    (junta con \\n, no agrega un \\n final extra)."""
    return "\n".join(str(r) for r in resultados)


if __name__ == "__main__":
    resultados = [10, 30, 15]
    salida = armar_salida(resultados)
    assert salida == "10\n30\n15", salida

    # uso real: sys.stdout.write(armar_salida(resultados) + "\n")
    print("OK")
