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
    
    # Carrega mapa (Agora é um array NumPy)
    mapa = MazeLoader.carregar(caminho_arquivo)
    
    # Pega as dimensões direto do NumPy
    linhas, colunas = mapa.shape

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
        
        # Clonagem rápida e correta usando NumPy
        mapa_oficial = mapa.copy()
        mapa_warmup = mapa.copy()

        resultado = Profiler.avaliar(motor, mapa_oficial, mapa_warmup)
        
        # Iterações por segundo (IPS)
        ips = 1000.0 / resultado.media_ms if resultado.media_ms > 0 else 0.0

        print(f"{nome:<10} | {resultado.media_ms:<10.4f} | {resultado.stats_min:<10.4f} | {resultado.stats_max:<10.4f} | {ips:<10.2f} | {resultado.memoria_usada:<12}")

    print("=========================================================================")

if __name__ == "__main__":
    main()