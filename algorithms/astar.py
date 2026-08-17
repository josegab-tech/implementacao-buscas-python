import numpy as np
import heapq
from numba import njit

@njit
def _executar_astar_otimizado(mapa):
    linhas, colunas = mapa.shape
    linha_inicio, coluna_inicio = -1, -1
    linha_fim, coluna_fim = -1, -1

    for l in range(linhas):
        for c in range(colunas):
            if mapa[l, c] == 2:
                linha_inicio, coluna_inicio = l, c
            elif mapa[l, c] == 3:
                linha_fim, coluna_fim = l, c

    if linha_inicio == -1 or linha_fim == -1:
        return False

    id_inicio = linha_inicio * colunas + coluna_inicio
    h_inicial = abs(linha_inicio - linha_fim) + abs(coluna_inicio - coluna_fim)

    fila = [(h_inicial, 0, id_inicio)]

    dl = np.array([-1, 1, 0, 0], dtype=np.int8)
    dc = np.array([0, 0, -1, 1], dtype=np.int8)

    while len(fila) > 0:
        f, g, atual_id = heapq.heappop(fila)

        l = atual_id // colunas
        c = atual_id % colunas
        celula = mapa[l, c]

        if celula == 4:
            continue

        if celula == 3:
            return True

        if celula == 1 or celula == 2:
            mapa[l, c] = 4

        for i in range(4):
            nova_l = l + dl[i]
            nova_c = c + dc[i]

            if 0 <= nova_l < linhas and 0 <= nova_c < colunas:
                vizinho = mapa[nova_l, nova_c]

                if vizinho == 1 or vizinho == 3:
                    novo_g = g + 1
                    novo_h = abs(nova_l - linha_fim) + abs(nova_c - coluna_fim)
                    novo_f = novo_g + novo_h
                    novo_id = nova_l * colunas + nova_c

                    heapq.heappush(fila, (novo_f, novo_g, novo_id))

    return False

class AStar:
    @staticmethod
    def executar(mapa):
        return _executar_astar_otimizado(mapa)