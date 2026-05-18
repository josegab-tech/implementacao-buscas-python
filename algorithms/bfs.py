from collections import deque


class BFS:

    DIRECOES = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    @staticmethod
    def executar(mapa):

        linhas = len(mapa)
        colunas = len(mapa[0])

        linha_inicio = -1
        coluna_inicio = -1

        # Encontrar entrada
        encontrou = False

        for l in range(linhas):

            for c in range(colunas):

                if mapa[l][c] == 'E':

                    linha_inicio = l
                    coluna_inicio = c

                    encontrou = True
                    break

            if encontrou:
                break

        if linha_inicio == -1:
            return False

        fila = deque()

        fila.append((linha_inicio, coluna_inicio))

        while fila:

            l, c = fila.popleft()

            if mapa[l][c] == 'S':
                return True

            for dl, dc in BFS.DIRECOES:

                nova_linha = l + dl
                nova_coluna = c + dc

                if (
                    0 <= nova_linha < linhas
                    and
                    0 <= nova_coluna < colunas
                ):

                    celula = mapa[nova_linha][nova_coluna]

                    if celula == '1' or celula == 'S':

                        # Marca visitado in-place
                        if celula == '1':
                            mapa[nova_linha][nova_coluna] = 'V'

                        fila.append(
                            (nova_linha, nova_coluna)
                        )

        return False