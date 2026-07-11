import sys

from loader.maze_loader import MazeLoader
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
from metrics.profiler import Profiler

def main():

    if len(sys.argv) < 2:
        print("Uso: python main.py mapas/labirinto.txt")
        return

    caminho_arquivo = sys.argv[1]
    
    # Carrega mapa
    mapa = MazeLoader.carregar(caminho_arquivo)
    
    linhas = len(mapa)
    colunas = len(mapa[0]) if linhas > 0 else 0

    print("=========================================================================")
    print(f" Mapa: {linhas} x {colunas} | Celulas: {linhas * colunas}")
    print("=========================================================================\n")

    # Fila de Execução Automática
    algoritmos = [
        ("DFS", DFS),
        ("BFS", BFS),
        ("Dijkstra", Dijkstra),
        ("A*", AStar)
    ]

    # Cabeçalho da Tabela
    print(f"{'Algoritmo':<10} | {'Media (ms)':<10} | {'Min (ms)':<10} | {'Max (ms)':<10} | {'IPS':<10} | {'Memoria (B)':<12}")
    print("-" * 75)

    for nome, motor in algoritmos:
        
        # Mantém as matrizes virgens para cada algoritmo
        mapa_oficial = [linha[:] for linha in mapa]
        mapa_warmup = [linha[:] for linha in mapa]

        resultado = Profiler.avaliar(motor, mapa_oficial, mapa_warmup)
        
        # Iterações por segundo (IPS)
        ips = 1000.0 / resultado.media_milis if resultado.media_milis > 0 else 0.0

        print(f"{nome:<10} | {resultado.media_milis:<10.4f} | {resultado.min_milis:<10.4f} | {resultado.max_milis:<10.4f} | {ips:<10.2f} | {resultado.memoria_bytes:<12}")

    print("=========================================================================")

if __name__ == "__main__":
    main()