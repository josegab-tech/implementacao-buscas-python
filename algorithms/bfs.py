import numpy as np
from numba import njit

@njit
def _executar_bfs_otimizado(mapa):
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
    fila_l = np.zeros(tamanho_maximo, dtype=np.int32)
    fila_c = np.zeros(tamanho_maximo, dtype=np.int32)
    
    inicio = 0
    fim = 0

    fila_l[fim] = linha_inicio
    fila_c[fim] = coluna_inicio
    fim += 1

    dl = np.array([-1, 1, 0, 0], dtype=np.int8)
    dc = np.array([0, 0, -1, 1], dtype=np.int8)

    while inicio < fim:
        l = fila_l[inicio]
        c = fila_c[inicio]
        inicio += 1

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

                    fila_l[fim] = nova_linha
                    fila_c[fim] = nova_coluna
                    fim += 1

    return False

class BFS:
    @staticmethod
    def executar(mapa):
        return _executar_bfs_otimizado(mapa)