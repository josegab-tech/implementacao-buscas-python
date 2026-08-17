import numpy as np

class MazeLoader:

    @staticmethod
    def carregar(caminho_arquivo):
        mapa_numerico = []
        tabela = {'0': 0, '1': 1, 'E': 2, 'S': 3, 'V': 4}

        with open(caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    mapa_numerico.append([tabela[char] for char in linha])

        return np.array(mapa_numerico, dtype=np.int8)