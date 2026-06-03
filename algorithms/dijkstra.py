import heapq

class Dijkstra:

    DIRECOES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @staticmethod
    def executar(mapa):
        linhas = len(mapa)
        colunas = len(mapa[0])

        linha_inicio, coluna_inicio = -1, -1

        # Procura entrada
        for l in range(linhas):
            for c in range(colunas):
                if mapa[l][c] == 'E':
                    linha_inicio, coluna_inicio = l, c
                    break
            if linha_inicio != -1:
                break

        if linha_inicio == -1:
            return False

        # Fila de prioridade (Min-Heap nativo em C)
        fila = []

        # Truque de performance: Converte coordenada 2D para ID único 1D
        id_inicio = linha_inicio * colunas + coluna_inicio
        
        # Insere apenas inteiros puros: (custo, id_celula)
        heapq.heappush(fila, (0, id_inicio))

        while fila:
            
            custo, atual_id = heapq.heappop(fila)

            # Desempacota o ID 1D de volta para linha e coluna
            l = atual_id // colunas
            c = atual_id % colunas

            celula = mapa[l][c]

            # Lazy Dijkstra: Ignora se já visitamos por um caminho mais barato
            if celula == 'V':
                continue

            # Encontrou saída
            if celula == 'S':
                return True

            # Marca visitado in-place (Nivelamento com C e Java)
            if celula == '1' or celula == 'E':
                mapa[l][c] = 'V'

            for dl, dc in Dijkstra.DIRECOES:
                nova_l = l + dl
                nova_c = c + dc

                if 0 <= nova_l < linhas and 0 <= nova_c < colunas:
                    vizinho = mapa[nova_l][nova_c]

                    # Nivelamento do padrão de caracteres ('1' caminho livre, '0' parede)
                    if vizinho == '1' or vizinho == 'S':
                        novo_custo = custo + 1
                        novo_id = nova_l * colunas + nova_c
                        
                        heapq.heappush(fila, (novo_custo, novo_id))

        return False