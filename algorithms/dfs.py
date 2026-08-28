import numpy as np
from numba import njit

@njit
def _executar_dfs_otimizado(mapa):
    linhas, colunas = mapa.shape
    linha_inicio, coluna_inicio = -1, -1

    for l in range(linhas):
        for c in range(colunas):
            if mapa[l, c] == 2:
                linha_inicio, coluna_inicio = l, c
                break
        if linha_inicio != -1:
            break

    if linha_inicio == -1:
        return False

    tamanho_maximo = linhas * colunas
    pilha_l = np.zeros(tamanho_maximo, dtype=np.int32)
    pilha_c = np.zeros(tamanho_maximo, dtype=np.int32)
    
    topo = 0
    pilha_l[topo] = linha_inicio
    pilha_c[topo] = coluna_inicio
    topo += 1

    dl = np.array([-1, 1, 0, 0], dtype=np.int8)
    dc = np.array([0, 0, -1, 1], dtype=np.int8)

    while topo > 0:
        topo -= 1
        l = pilha_l[topo]
        c = pilha_c[topo]

        if mapa[l, c] == 3:
            return True

        for i in range(4):
            nova_linha = l + dl[i]
            nova_coluna = c + dc[i]

            if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas:
                celula = mapa[nova_linha, nova_coluna]

                if celula == 1 or celula == 3:
                    if celula == 1:
                        mapa[nova_linha, nova_coluna] = 4

                    pilha_l[topo] = nova_linha
                    pilha_c[topo] = nova_coluna
                    topo += 1

    return False

class DFS:
    @staticmethod
    def executar(mapa):
        return _executar_dfs_otimizado(mapa)