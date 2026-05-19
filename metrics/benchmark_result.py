class BenchmarkResult:

    def __init__(self, encontrou_saida, tempo_milis, memoria_bytes):
        
        #indica se encontrou caminho até saída
        self.encontrou_saida = encontrou_saida
        
        #Tempo de execução em milissegundos
        self.tempo_milis = tempo_milis
        
        #Memória utilizada em KB
        self.memoria_bytes = memoria_bytes