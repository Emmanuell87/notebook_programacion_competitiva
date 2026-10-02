# Dado un arreglo, encontrar el par (i,j) que maximiza a_i XOR a_j, en
# O(n*B) (B = cantidad de bits) en vez de O(n^2) probando todos los
# pares. Idea: inserta cada numero en un Trie recorriendo sus bits de
# mas a menos significativo; para maximizar el XOR con un numero x, en
# cada bit conviene bajar por la rama OPUESTA al bit de x si existe
# (maximiza ese bit del resultado), y si no existe, se baja por la
# rama igual (es la unica disponible).
#
# bits = cantidad de bits a considerar (ajustalo segun el rango de tus
# numeros; por defecto 30 cubre hasta ~10^9).


class TrieXOR:
    def __init__(self, bits=30):
        self.bits = bits
        self.hijos = [[-1, -1]]  # hijos[nodo][bit] = nodo, o -1 si no existe

    def insertar(self, x):
        nodo = 0
        for i in range(self.bits - 1, -1, -1):
            b = (x >> i) & 1
            if self.hijos[nodo][b] == -1:
                self.hijos.append([-1, -1])
                self.hijos[nodo][b] = len(self.hijos) - 1
            nodo = self.hijos[nodo][b]

    def max_xor_con(self, x):
        nodo = 0
        resultado = 0
        for i in range(self.bits - 1, -1, -1):
            b = (x >> i) & 1
            deseado = 1 - b  # el bit opuesto maximiza este bit del XOR
            if self.hijos[nodo][deseado] != -1:
                resultado |= (1 << i)
                nodo = self.hijos[nodo][deseado]
            else:
                nodo = self.hijos[nodo][b]
        return resultado


def max_xor_par(arr):
    if len(arr) < 2:
        return 0
    bits = max(arr).bit_length()
    t = TrieXOR(bits)
    t.insertar(arr[0])
    mejor = 0
    for x in arr[1:]:
        mejor = max(mejor, t.max_xor_con(x))
        t.insertar(x)
    return mejor


def fuerza_bruta_max_xor(arr):
    mejor = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            mejor = max(mejor, arr[i] ^ arr[j])
    return mejor


if __name__ == "__main__":
    # --- ejemplo ---
    assert max_xor_par([3, 10, 5, 25, 2, 8]) == 28   # 5 ^ 25
    t = TrieXOR(5)
    t.insertar(5)
    t.insertar(25)
    assert t.max_xor_con(3) == 26   # 3 ^ 25
    # --- fin ejemplo ---
    import random
    random.seed(2)
    for _ in range(100):
        n = random.randint(2, 12)
        arr = [random.randint(0, 500) for _ in range(n)]
        assert max_xor_par(arr) == fuerza_bruta_max_xor(arr)
    print("OK")
