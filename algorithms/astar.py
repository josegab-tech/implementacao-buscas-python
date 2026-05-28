import heapq

class AStar:

    DIRECOES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @staticmethod
    def executar(mapa):
        linhas = len(mapa)
        colunas = len(mapa[0])

        linha_inicio, coluna_inicio = -1, -1
        linha_fim, coluna_fim = -1, -1

        # Procura entrada e saída (necessário para a Heurística)
        for l in range(linhas):
            for c in range(colunas):
                if mapa[l][c] == 'E':
                    linha_inicio, coluna_inicio = l, c
                elif mapa[l][c] == 'S':
                    linha_fim, coluna_fim = l, c

        if linha_inicio == -1 or linha_fim == -1:
            return False

        fila = []
        id_inicio = linha_inicio * colunas + coluna_inicio

        # h inicial (Distância de Manhattan)
        h_inicial = abs(linha_inicio - linha_fim) + abs(coluna_inicio - coluna_fim)

        # Insere: (Custo_Total_F, Custo_Real_G, ID_Celula)
        heapq.heappush(fila, (h_inicial, 0, id_inicio))

        while fila:
            
            f, g, atual_id = heapq.heappop(fila)

            l = atual_id // colunas
            c = atual_id % colunas

            celula = mapa[l][c]

            if celula == 'V':
                continue

            if celula == 'S':
                return True

            # Marca in-place apenas ao retirar da fila (certeza do menor caminho)
            if celula == '1' or celula == 'E':
                mapa[l][c] = 'V'

            for dl, dc in AStar.DIRECOES:
                nova_l = l + dl
                nova_c = c + dc

                if 0 <= nova_l < linhas and 0 <= nova_c < colunas:
                    vizinho = mapa[nova_l][nova_c]

                    if vizinho == '1' or vizinho == 'S':
                        
                        novo_g = g + 1
                        novo_h = abs(nova_l - linha_fim) + abs(nova_c - coluna_fim)
                        novo_f = novo_g + novo_h
                        
                        novo_id = nova_l * colunas + nova_c

                        heapq.heappush(fila, (novo_f, novo_g, novo_id))

        return False