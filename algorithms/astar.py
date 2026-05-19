import heapq


class AStar:

    @staticmethod
    def heuristica(a, b):

        # Distância Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @staticmethod
    def executar(mapa):

        linhas = len(mapa)
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

        # (prioridade, custo, posição)
        heapq.heappush(fila, (0, 0, inicio))

        visitados = set()

        direcoes = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while fila:

            prioridade, custo, atual = heapq.heappop(fila)

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

                            heuristica = AStar.heuristica(
                                vizinho,
                                fim
                            )

                            prioridade_total = (
                                novo_custo + heuristica
                            )

                            heapq.heappush(
                                fila,
                                (
                                    prioridade_total,
                                    novo_custo,
                                    vizinho
                                )
                            )

        return False