class MazeLoader:

    @staticmethod
    def carregar(caminho_arquivo):

        mapa = []

        #Abre arquivo em modo de leitura
        with open(caminho_arquivo, "r") as arquivo:
            
            #Percorre linha por linha
            for linha in arquivo:

                #Remove quebra de linha
                linha = linha.strip()

                mapa.append(list(linha))

        return mapa