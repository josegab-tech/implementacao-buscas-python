class BFS:

    DIRECOES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @staticmethod
    def executar(mapa):
        linhas = len(mapa)
        colunas = len(mapa[0])

        linha_inicio, coluna_inicio = -1, -1

        for l in range(linhas):
            for c in range(colunas):
                if mapa[l][c] == 'E':
                    linha_inicio, coluna_inicio = l, c
                    break
            if linha_inicio != -1:
                break

        if linha_inicio == -1:
            return False

        # PRÉ-ALOCAÇÃO (Tamanho Máximo)
        tamanho_maximo = linhas * colunas
        fila_l = [0] * tamanho_maximo
        fila_c = [0] * tamanho_maximo
        
        inicio = 0
        fim = 0

        # Enfileira o inicial
        fila_l[fim] = linha_inicio
        fila_c[fim] = coluna_inicio
        fim += 1

        while inicio < fim:
            # Desenfileira
            l = fila_l[inicio]
            c = fila_c[inicio]
            inicio += 1

            if mapa[l][c] == 'S':
                return True

            for dl, dc in BFS.DIRECOES:
                nova_linha = l + dl
                nova_coluna = c + dc

                if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas:
                    celula = mapa[nova_linha][nova_coluna]

                    if celula == '1' or celula == 'S':
                        if celula == '1':
                            mapa[nova_linha][nova_coluna] = 'V'

                        # Enfileira
                        fila_l[fim] = nova_linha
                        fila_c[fim] = nova_coluna
                        fim += 1

        return False