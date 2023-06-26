from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = [edge]

        if edge in self.graph:
            self.graph[edge].append(vertex)
        else:
            self.graph[edge] = [vertex]

    def dfs(self, start_vertex):
        comparacoes = 0
        trocas = 0
        visited = set()
        comparacoesAux = 0
        trocasAux = 0
        comparacoes += 1
        if start_vertex not in self.graph:
            return comparacoes, trocas
        comparacoesAux, trocasAux = self._dfs_helper(start_vertex, visited)
        comparacoes += comparacoesAux
        trocas += trocasAux
        return comparacoes, trocas

    def _dfs_helper(self, vertex, visited):
        comparacoes = 0
        trocas = 0
        visited.add(vertex)
        print(vertex, end=" ")
        comparacoes += 1
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                comparacoes += 1
                if neighbor not in visited:
                    trocas += 1
                    comparacoesAux, trocasAux = self._dfs_helper(neighbor, visited)
                    comparacoes += comparacoesAux
                    trocas += trocasAux
    
        return comparacoes, trocas
    
    def print_adjacency_list(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(str(e) for e in edges)}")
    
    def count_vertices(self):
        return len(self.graph)

    def count_edges(self):
        total_edges = sum(len(edges) for edges in self.graph.values())
        return total_edges // 2  # Dividido por 2 para contar cada aresta apenas uma vez em grafos não direcionados
            
    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = [edge]

        if edge in self.graph:
            self.graph[edge].append(vertex)
        else:
            self.graph[edge] = [vertex]

    def find_articulation_points(self):
        comparacoes = 0
        trocas = 0
        articulation_points = []

        # Variáveis auxiliares para o algoritmo de busca de articulações
        visited = set()
        discovery_time = {}
        low = {}
        parent = {}
        time = 0

        # Função auxiliar para a busca de articulações
        def dfs_articulation(v):
            nonlocal comparacoes
            nonlocal trocas
            nonlocal time
            visited.add(v)
            discovery_time[v] = time
            low[v] = time
            time += 1

            children = 0
            is_articulation = False
            comparacoes += 1
            if v in self.graph:
                for neighbor in self.graph[v]:
                    comparacoes += 1
                    if neighbor not in visited:
                        parent[neighbor] = v
                        trocas += 1
                        children += 1
                        dfs_articulation(neighbor)

                        low[v] = min(low[v], low[neighbor])
                        trocas += 1

                        comparacoes += 1
                        if parent[v] is None and children > 1:
                            is_articulation = True
                        comparacoes += 1
                        if parent[v] is not None and low[neighbor] >= discovery_time[v]:
                            is_articulation = True
                    elif neighbor != parent[v]:
                        low[v] = min(low[v], discovery_time[neighbor])
                        trocas += 1
                    comparacoes += 1

            comparacoes += 1
            if is_articulation:
                articulation_points.append(v)

        # Executa a busca de articulações para cada vértice não visitado
        for vertex in self.graph.keys():
            comparacoes += 1
            if vertex not in visited:
                parent[vertex] = None
                trocas += 1
                dfs_articulation(vertex)

        return articulation_points, comparacoes, trocas
    
    def find_strongly_connected_components(self):
        # Variáveis auxiliares para o algoritmo de busca de SCC
        visited = set()
        stack = []
        low_link = {}
        ids = {}
        on_stack = set()
        result = []
        comparacoes = 0
        trocas = 0

        # Função auxiliar para a busca de SCC
        def dfs_scc(v):
            nonlocal result
            nonlocal comparacoes
            nonlocal trocas
            stack.append(v)
            on_stack.add(v)
            visited.add(v)
            low_link[v] = ids[v] = len(ids)
            trocas += 1

            comparacoes += 1
            if v in self.graph:
                for neighbor in self.graph[v]:
                    comparacoes += 1
                    if neighbor not in visited:
                        dfs_scc(neighbor)
                        low_link[v] = min(low_link[v], low_link[neighbor])
                        trocas += 1
                    elif neighbor in on_stack:
                        low_link[v] = min(low_link[v], ids[neighbor])
                        trocas += 1
                    comparacoes += 1
                    
            comparacoes += 1
            if low_link[v] == ids[v]:
                component = []
                while True:
                    comparacoes += 1
                    node = stack.pop()
                    trocas += 1
                    on_stack.remove(node)
                    component.append(node)
                    comparacoes += 1
                    if node == v:
                        break
                result.append(component)

        # Executa a busca de SCC para cada vértice não visitado
        for vertex in self.graph.keys():
            comparacoes += 1
            if vertex not in visited:
                dfs_scc(vertex)

        return result, comparacoes, trocas
    
    def bfs(self, start_vertex):
        visited = set()
        queue = deque()
        queue.append(start_vertex)
        visited.add(start_vertex)
        comparacoes = 0
        trocas = 0

        while queue:
            current_vertex = queue.popleft()
            trocas += 1
            comparacoes += 1
            print(current_vertex, end=" ")

            comparacoes += 1
            if current_vertex in self.graph:
                for neighbor in self.graph[current_vertex]:
                    comparacoes += 1
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        return comparacoes, trocas
