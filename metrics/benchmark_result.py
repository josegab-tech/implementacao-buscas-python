class BenchmarkResult:

    def __init__(self, encontrou_saida, media_milis, min_milis, max_milis, iteracoes, memoria_bytes):
        self.encontrou_saida = encontrou_saida
        self.media_milis = media_milis
        self.min_milis = min_milis
        self.max_milis = max_milis
        self.iteracoes = iteracoes
        self.memoria_bytes = memoria_bytes