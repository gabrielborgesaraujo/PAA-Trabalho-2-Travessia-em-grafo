from collections import deque
import time
import json
import threading
import sys
from classDados import Dados
from classGraph import Graph
sys.setrecursionlimit(500000)


def generate_complete_graph(X):
    graph = Graph()  # Cria um objeto Graph

    # Gera os vértices
    vertices = [i + 1 for i in range(X)]

    # Adiciona os vértices ao grafo
    for vertex in vertices:
        graph.add_vertex(vertex)

    # Gera as arestas
    for source in range(1, X + 1):
        for target in range(source + 1, X + 1):
            graph.add_edge(source, target)

    return graph
    

def geraDados(grafo: Graph):
    dadoGrafo = Dados()
    
    start_timeDFS = time.time()
    comparacoes, trocas = grafo.dfs(1)
    end_timeDFS = time.time()
    dadoGrafo.setComparacoesTrocasDFS(comparacoes= comparacoes, trocas= trocas)
    dadoGrafo.setTempoExecucaoDFS(end_timeDFS - start_timeDFS)
    
    dadoGrafo.setNumeroVertices(grafo.count_vertices())
    dadoGrafo.setNumeroArestas(grafo.count_edges())
    
    start_timeArticulationPoints = time.time()
    articulation_points, comparacoes, trocas = grafo.find_articulation_points()
    end_timeArticulationPoints = time.time()
    dadoGrafo.setComparacoesTrocasArticulationPoints(comparacoes= comparacoes, trocas= trocas)
    dadoGrafo.setTempoExecucaoArticulationPoints(end_timeArticulationPoints - start_timeArticulationPoints)
    
    start_timeStronglyConnectedComponents = time.time()
    components, comparacoes, trocas = grafo.find_strongly_connected_components()
    end_timeStronglyConnectedComponents = time.time()
    dadoGrafo.setTempoExecucaoStronglyConnectedComponents(end_timeStronglyConnectedComponents - start_timeStronglyConnectedComponents)
    dadoGrafo.setComparacoesTrocasStronglyConnectedComponents(comparacoes= comparacoes, trocas= trocas)
    
    start_timeBFS = time.time()
    comparacoes, trocas = grafo.bfs(1)
    end_timeBFS = time.time()
    dadoGrafo.setComparacoesTrocasBFS(comparacoes= comparacoes, trocas= trocas)
    dadoGrafo.setTempoExecucaoBFS(end_timeBFS - start_timeBFS)
    
    dadosGrafos.append(dadoGrafo)


dadosGrafos = []

threads = []

allGrafos = []

tamanhos = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]


for tamanho in tamanhos:
    allGrafos.append(generate_complete_graph(tamanho))

for grafoThread in allGrafos:
    threadingGrafo = threading.Thread(target=geraDados, args=(grafoThread,))
    threads.append(threadingGrafo)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("\n\nFim")
    
    
array_dicionario = [obj.to_dic() for obj in dadosGrafos]
    
with open('objetos.json', 'w') as arquivo_json:
    json.dump(array_dicionario, arquivo_json)
    
    