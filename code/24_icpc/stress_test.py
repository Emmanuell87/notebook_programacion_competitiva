import random

# Cuando sale Wrong Answer y no se ve el error: comparar la solucion
# rapida contra una fuerza bruta (lenta pero obviamente correcta) sobre
# muchos casos aleatorios PEQUENOS. Devuelve el primer caso donde difieren
# (o None si no encontro ninguno): ese caso se revisa a mano.


def buscar_contraejemplo(generar, rapida, bruta, intentos=2000):
    for _ in range(intentos):
        caso = generar()
        if rapida(caso) != bruta(caso):
            return caso
    return None


if __name__ == "__main__":
    # --- ejemplo ---
    def generar():
        return [random.randint(-5, 5) for _ in range(random.randint(1, 6))]

    def bruta(arr):        # maxima suma de un subarreglo, probando todos
        return max(sum(arr[i:j]) for i in range(len(arr)) for j in range(i + 1, len(arr) + 1))

    def con_error(arr):    # variante con un error: devuelve 0 si todos son negativos
        mejor = actual = 0
        for x in arr:
            actual = max(0, actual + x)
            mejor = max(mejor, actual)
        return mejor

    random.seed(1)
    assert buscar_contraejemplo(generar, con_error, bruta) is not None
    assert buscar_contraejemplo(generar, bruta, bruta) is None
    # --- fin ejemplo ---

    caso = buscar_contraejemplo(generar, con_error, bruta)
    assert con_error(caso) != bruta(caso)
    print("OK")
