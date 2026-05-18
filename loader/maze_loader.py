class MazeLoader:

    @staticmethod
    def carregar(caminho_arquivo):

        mapa = []

        with open(caminho_arquivo, "r") as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                mapa.append(list(linha))

        return mapa