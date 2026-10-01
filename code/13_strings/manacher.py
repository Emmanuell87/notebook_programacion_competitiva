# Encontrar el substring palindromico mas largo en O(n) (mucho mejor
# que el O(n^2) de expandir desde cada centro). p[i] en la cadena
# transformada corresponde exactamente a la longitud del palindromo en
# la cadena original centrado ahi.


def manacher(s):
    # transforma "abc" -> "#a#b#c#" para manejar palindromos pares e impares igual
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i] = radio del palindromo centrado en i (en t)
    centro = derecha = 0
    for i in range(n):
        if i < derecha:
            p[i] = min(derecha - i, p[2 * centro - i])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > derecha:
            centro, derecha = i, i + p[i]

    max_len, centro_max = max((v, i) for i, v in enumerate(p))
    inicio = (centro_max - max_len) // 2  # indice en la cadena original
    return s[inicio:inicio + max_len]


if __name__ == "__main__":
    assert manacher("babad") in ("bab", "aba")  # ambos son validos, largo 3
    assert manacher("cbbd") == "bb"
    assert manacher("a") == "a"
    assert manacher("racecar") == "racecar"
    print("OK")
