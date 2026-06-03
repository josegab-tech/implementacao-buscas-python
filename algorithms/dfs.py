class DFS:

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

        # PRÉ-ALOCAÇÃO: Cria listas com o tamanho máximo possível, evita refatoração
        tamanho_maximo = linhas * colunas
        pilha_l = [0] * tamanho_maximo
        pilha_c = [0] * tamanho_maximo
        
        topo = 0 # ponteiro manual

        # Push inicial
        pilha_l[topo] = linha_inicio
        pilha_c[topo] = coluna_inicio
        topo += 1

        while topo > 0:
            # Pop
            topo -= 1
            l = pilha_l[topo]
            c = pilha_c[topo]

            if mapa[l][c] == 'S':
                return True

            for dl, dc in DFS.DIRECOES:
                nova_linha = l + dl
                nova_coluna = c + dc

                if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas:
                    celula = mapa[nova_linha][nova_coluna]

                    if celula == '1' or celula == 'S':
                        if celula == '1':
                            mapa[nova_linha][nova_coluna] = 'V'

                        # Push (Reaproveita o espaço de memória existente)
                        pilha_l[topo] = nova_linha
                        pilha_c[topo] = nova_coluna
                        topo += 1

        return False