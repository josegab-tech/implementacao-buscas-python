import heapq


class Dijkstra:

    @staticmethod
    def executar(mapa):

        #quantidade de linhas mapa
        linhas = len(mapa)
        #quantidade colunas mapa
        colunas = len(mapa[0])

        inicio = None
        fim = None

        # Procura entrada e saída
        for i in range(linhas):
            for j in range(colunas):

                if mapa[i][j] == 'E':
                    inicio = (i, j)

                elif mapa[i][j] == 'S':
                    fim = (i, j)

        # Fila de prioridade
        fila = []

        # (custo, posição) Sempre remove o menor custo primeiro
        heapq.heappush(fila, (0, inicio))

        #ja visitado
        visitados = set()

        # Direções:
        # cima, baixo, esquerda, direita
        direcoes = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        #Enquanto tiver o que explorar
        while fila:
            
            #Removendo posiçao com menor custo
            custo, atual = heapq.heappop(fila)

            
            if atual in visitados:
                continue

            visitados.add(atual)

            # Encontrou saída
            if atual == fim:
                return True

            for dx, dy in direcoes:

                nx = atual[0] + dx
                ny = atual[1] + dy

                if 0 <= nx < linhas and 0 <= ny < colunas:

                    if mapa[nx][ny] != '#':

                        vizinho = (nx, ny)

                        if vizinho not in visitados:

                            novo_custo = custo + 1

                            heapq.heappush(
                                fila,
                                (novo_custo, vizinho)
                            )

        return False