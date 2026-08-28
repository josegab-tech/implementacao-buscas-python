import time
import tracemalloc
from metrics.benchmark_result import BenchmarkResult

class Profiler:

    TEMPO_LIMITE_SEGUNDOS = 1.0 # Equivalente ao loop do Benchee

    @staticmethod
    def avaliar(algoritmo, mapa_oficial, mapa_warmup):
        
        # 1. Warm-up (Reduzido para 3 para não travar em mapas muito grandes)
        for _ in range(3):
            clone = mapa_warmup.copy()
            algoritmo.executar(clone)

        # Variáveis Estatísticas
        stats_min = float('inf')
        stats_max = 0.0
        tempo_acumulado_ns = 0
        iteracoes = 0
        encontrou_saida = False

        # 2. Início captura de memória
        tracemalloc.start()
        memoria_antes, _ = tracemalloc.get_traced_memory()

        # 3. Loop temporal estilo Benchee
        inicio_global = time.perf_counter()

        while (time.perf_counter() - inicio_global) < Profiler.TEMPO_LIMITE_SEGUNDOS:
            
            # Restaura o mapa FORA do cronômetro usando cópia do NumPy!
            clone = mapa_oficial.copy()

            # ⏱️ LIGA O CRONÔMETRO
            inicio_iteracao = time.perf_counter_ns()
            
            encontrou_saida = algoritmo.executar(clone)
            
            # ⏱️ DESLIGA O CRONÔMETRO
            fim_iteracao = time.perf_counter_ns()

            # Cálculos da iteração
            tempo_iteracao_ms = (fim_iteracao - inicio_iteracao) / 1_000_000.0

            if tempo_iteracao_ms < stats_min: stats_min = tempo_iteracao_ms
            if tempo_iteracao_ms > stats_max: stats_max = tempo_iteracao_ms
            
            tempo_acumulado_ns += (fim_iteracao - inicio_iteracao)
            iteracoes += 1

        # 4. Fim captura de memória
        memoria_depois, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # 5. Matemática Final
        media_ms = (tempo_acumulado_ns / 1_000_000.0) / iteracoes if iteracoes > 0 else 0.0
        memoria_usada = pico - memoria_antes if pico > memoria_antes else 0

        return BenchmarkResult(
            encontrou_saida,
            media_ms,
            stats_min,
            stats_max,
            iteracoes,
            memoria_usada
        )