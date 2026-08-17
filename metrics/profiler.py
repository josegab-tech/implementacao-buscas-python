import time
import tracemalloc

from metrics.benchmark_result import BenchmarkResult


class Profiler:

    @staticmethod
    def avaliar(algoritmo, mapa_oficial, mapa_warmup):

        # 1. Warm-up
        for _ in range(1000):

            clone = mapa_warmup.copy()

            algoritmo.executar(clone)

        # 2. Início captura memória
        tracemalloc.start()

        memoria_antes, _ = tracemalloc.get_traced_memory()

        # 3. Tempo início
        inicio = time.perf_counter_ns()

        # 4. Execução
        encontrou_saida = algoritmo.executar(mapa_oficial)

        # 5. Tempo fim
        fim = time.perf_counter_ns()

        memoria_depois, pico = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        # 6. Resultados
        tempo_milis = (fim - inicio) / 1_000_000

        memoria_bytes = pico - memoria_antes

        return BenchmarkResult(
            encontrou_saida,
            tempo_milis,
            memoria_bytes
        )