import sys

from loader.maze_loader import MazeLoader

from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
from metrics.profiler import Profiler


def main():

    # Verifica argumentos
    if len(sys.argv) < 3:

        print("Uso:")
        print("python main.py <algoritmo> <arquivo>")
        print()
        print("Exemplos:")
        print("python main.py bfs mapas/labirinto.txt")
        print("python main.py dfs mapas/caverna.txt")
        print("python main.py dijkstra mapas/perfeito.txt")
        print("python main.py astar mapas/labirinto_60x30.txt")

        return

    nome_algoritmo = sys.argv[1].lower()

    caminho_arquivo = sys.argv[2]
    
    # Carrega mapa
    mapa = MazeLoader.carregar(caminho_arquivo)

    # Seleção do algoritmo
    algoritmo = None

    if nome_algoritmo == "bfs":
        algoritmo = BFS

    elif nome_algoritmo == "dfs":
        algoritmo = DFS

    elif nome_algoritmo == "dijkstra": 
        algoritmo = Dijkstra

    elif nome_algoritmo == "astar": 
        algoritmo = AStar

    else:
        print("Algoritmo inválido.")
        print("Use: bfs, dfs, dijkstra ou astar")

        return

    # Clones do mapa
    mapa_oficial = [linha[:] for linha in mapa]

    mapa_warmup = [linha[:] for linha in mapa]

    # Benchmark
    resultado = Profiler.avaliar(
        algoritmo,
        mapa_oficial,
        mapa_warmup
    )

    # Resultado
    print()
    print("=== RESULTADO ===")
    print()

    print("Algoritmo:",
          nome_algoritmo.upper())

    print("Encontrou saída:",
          resultado.encontrou_saida)

    print("Tempo:",
          resultado.tempo_milis,
          "ms")

    print("Memória:",
          resultado.memoria_bytes,
          "bytes")


if __name__ == "__main__":
    main()