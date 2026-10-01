# Deteccion de ciclo en grafos DIRIGIDOS. g = lista de adyacencia
# 0-indexada (g[u] = vecinos de u), NO diccionario. Usa 3 colores para
# distinguir un ciclo real de simplemente revisitar un nodo ya
# terminado (clave en dirigidos: visitar un nodo "en proceso" -color
# 1- indica ciclo; visitar uno "terminado" -color 2- no).


def ciclo_dirigido(g):
    n = len(g)
    color = [0] * n  # 0=unseen,1=visiting,2=done

    def dfs(u):
        color[u] = 1
        for v in g[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    return any(color[i] == 0 and dfs(i) for i in range(n))


if __name__ == "__main__":
    # 0->1->2->0 (ciclo)
    g_con_ciclo = [[1], [2], [0]]
    assert ciclo_dirigido(g_con_ciclo) is True

    # 0->1->2 (sin ciclo)
    g_sin_ciclo = [[1], [2], []]
    assert ciclo_dirigido(g_sin_ciclo) is False

    # diamante sin ciclo: 0->1, 0->2, 1->3, 2->3 (revisita 3 pero color=2, no es ciclo)
    g_diamante = [[1, 2], [3], [3], []]
    assert ciclo_dirigido(g_diamante) is False
    print("OK")
