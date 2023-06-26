from classDados import Dados
import matplotlib.pyplot as plt
import json
from pprint import pprint

def generate_plots(data_list: list[Dados]):
    # Extrai os dados do objeto Dados
    tempo_execucao_dfs = [dados.tempoExecucaoDFS for dados in data_list]
    tempo_execucao_bfs = [dados.tempoExecucaoBFS for dados in data_list]
    tempo_execucao_articulation = [dados.tempoExecucaoArticulationPoints for dados in data_list]
    tempo_execucao_strongly_connected = [dados.tempoExecucaoStronglyConnectedComponents for dados in data_list]
    comparacoes_dfs = [dados.comparacoesDFS for dados in data_list]
    comparacoes_bfs = [dados.comparacoesBFS for dados in data_list]
    comparacoes_articulation = [dados.comparacoesArticulationPoints for dados in data_list]
    comparacoes_strongly_connected = [dados.comparacoesStronglyConnectedComponents for dados in data_list]
    trocas_dfs = [dados.trocasDFS for dados in data_list]
    trocas_bfs = [dados.trocasBFS for dados in data_list]
    trocas_articulation = [dados.trocasArticulationPoints for dados in data_list]
    trocas_strongly_connected = [dados.trocasStronglyConnectedComponents for dados in data_list]
    numero_vertices = [dados.numeroVertices for dados in data_list]
    numero_arestas = [dados.numeroArestas for dados in data_list]

    # Criação dos gráficos
    plt.figure(figsize=(12, 8))

    # Gráfico de tempo de execução do DFS
    plt.plot(numero_vertices, tempo_execucao_dfs, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Tempo de execução do DFS')
    plt.savefig('imagens/tempoExecucaoDFS.png')
    plt.close()

    # Gráfico de tempo de execução do BFS
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, tempo_execucao_bfs, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Tempo de execução do BFS')
    plt.savefig('imagens/tempoExecucaoBFS.png')
    plt.close()

    # Gráfico de tempo de execução dos Articulation Points
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, tempo_execucao_articulation, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Tempo de execução dos Articulation Points')
    plt.savefig('imagens/tempoExecucaoArticulationPoints.png')
    plt.close()

    # Gráfico de tempo de execução dos Strongly Connected Components
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, tempo_execucao_strongly_connected, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Tempo de execução dos Strongly Connected Components')
    plt.savefig('imagens/tempoExecucaoStronglyConnectedComponents.png')
    plt.close()

    # Gráfico de comparações do DFS
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, comparacoes_dfs, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de comparações')
    plt.title('Número de comparações do DFS')
    plt.savefig('imagens/comparacoesDFS.png')
    plt.close()

    # Gráfico de comparações do BFS
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, comparacoes_bfs, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de comparações')
    plt.title('Número de comparações do BFS')
    plt.savefig('imagens/comparacoesBFS.png')
    plt.close()

    # Gráfico de comparações dos Articulation Points
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, comparacoes_articulation, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de comparações')
    plt.title('Número de comparações dos Articulation Points')
    plt.savefig('imagens/comparacoesArticulationPoints.png')
    plt.close()

    # Gráfico de comparações dos Strongly Connected Components
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, comparacoes_strongly_connected, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de comparações')
    plt.title('Número de comparações dos Strongly Connected Components')
    plt.savefig('imagens/comparacoesStronglyConnectedComponents.png')
    plt.close()

    # Gráfico de trocas do DFS
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, trocas_dfs, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de trocas')
    plt.title('Número de trocas do DFS')
    plt.savefig('imagens/trocasDFS.png')
    plt.close()

    # Gráfico de trocas do BFS
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, trocas_bfs, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de trocas')
    plt.title('Número de trocas do BFS')
    plt.savefig('imagens/trocasBFS.png')
    plt.close()

    # Gráfico de trocas dos Articulation Points
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, trocas_articulation, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de trocas')
    plt.title('Número de trocas dos Articulation Points')
    plt.savefig('imagens/trocasArticulationPoints.png')
    plt.close()

    # Gráfico de trocas dos Strongly Connected Components
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, trocas_strongly_connected, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de trocas')
    plt.title('Número de trocas dos Strongly Connected Components')
    plt.savefig('imagens/trocasStronglyConnectedComponents.png')
    plt.close()

    # Gráfico de número de arestas
    plt.figure(figsize=(12, 8))
    plt.plot(numero_vertices, numero_arestas, marker='o')
    plt.xlabel('Número de vértices')
    plt.ylabel('Número de arestas')
    plt.title('Número de arestas')
    plt.savefig('imagens/numeroArestas.png')
    plt.close()

