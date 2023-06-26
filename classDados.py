from collections import deque

class Dados:
    
    def __init__(self):
        self.tempoExecucaoDFS = 0
        self.tempoExecucaoBFS = 0
        self.tempoExecucaoArticulationPoints = 0
        self.tempoExecucaoStronglyConnectedComponents = 0
        self.comparacoesDFS = 0
        self.comparacoesBFS = 0
        self.comparacoesArticulationPoints = 0
        self.comparacoesStronglyConnectedComponents = 0
        self.trocasDFS = 0
        self.trocasBFS = 0
        self.trocasArticulationPoints = 0
        self.trocasStronglyConnectedComponents = 0
        self.numeroVertices = 0
        self.numeroArestas = 0
    
    def setTempoExecucaoDFS(self, tempoExecucaoDFS):
        self.tempoExecucaoDFS = tempoExecucaoDFS
    
    def setTempoExecucaoBFS(self, tempoExecucaoBFS):
        self.tempoExecucaoBFS = tempoExecucaoBFS
    
    def setTempoExecucaoArticulationPoints(self, tempoExecucaoArticulationPoints):
        self.tempoExecucaoArticulationPoints = tempoExecucaoArticulationPoints
    
    def setTempoExecucaoStronglyConnectedComponents(self, tempoExecucaoStronglyConnectedComponents):
        self.tempoExecucaoStronglyConnectedComponents = tempoExecucaoStronglyConnectedComponents
    
    def setComparacoesTrocasDFS(self, comparacoes, trocas):
        self.comparacoesDFS = comparacoes
        self.trocasDFS = trocas
    
    def setComparacoesTrocasBFS(self, comparacoes, trocas):
        self.comparacoesBFS = comparacoes
        self.trocasBFS = trocas
    
    def setComparacoesTrocasArticulationPoints(self, comparacoes, trocas):
        self.comparacoesArticulationPoints = comparacoes
        self.trocasArticulationPoints = trocas
    
    def setComparacoesTrocasStronglyConnectedComponents(self, comparacoes, trocas):
        self.comparacoesStronglyConnectedComponents = comparacoes
        self.trocasStronglyConnectedComponents = trocas
    
    def setNumeroVertices(self, numeroVertices):
        self.numeroVertices = numeroVertices
    
    def setNumeroArestas(self, numeroArestas):
        self.numeroArestas = numeroArestas 
    
    def to_dic(self):
        return {
            "tempoExecucaoDFS" : self.tempoExecucaoDFS,
            "tempoExecucaoBFS" : self.tempoExecucaoBFS,
            "tempoExecucaoArticulationPoints" : self.tempoExecucaoArticulationPoints,
            "tempoExecucaoStronglyConnectedComponents" : self.tempoExecucaoStronglyConnectedComponents,
            "comparacoesDFS" : self.comparacoesDFS,
            "comparacoesBFS" : self.comparacoesBFS,
            "comparacoesArticulationPoints" : self.comparacoesArticulationPoints,
            "comparacoesStronglyConnectedComponents" : self.comparacoesStronglyConnectedComponents,
            "trocasDFS" : self.trocasDFS,
            "trocasBFS" : self.trocasBFS,
            "trocasArticulationPoints" : self.trocasArticulationPoints,
            "trocasStronglyConnectedComponents" : self.trocasStronglyConnectedComponents,
            "numeroVertices" : self.numeroVertices,
            "numeroArestas" : self.numeroArestas
        }
    