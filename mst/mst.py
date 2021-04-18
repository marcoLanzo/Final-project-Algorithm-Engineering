#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../")
from unionFind.UnionFind_QuickUnion_PathCompression\
        import UnionFindQuickUnionPathCompression as UnionFind
from priorityQueue.PQbinaryHeap import PQbinaryHeap as PriorityQueue
from dictionary_tree.dictionary.dictTrees.trees.treeArrayList\
        import TreeArrayListNode
from tree.TreeMod import TreeMod
from tree.TreeNodeMod import  TreeNodeMod
from GraphHelper import GraphHelper
from graph.elements import Edge
INFINITE = float("inf")

class MST:
    """
    Contiene metodi che implementano vari algoritmi per il calcolo del minimum
    spanning tree, che prendono in input un grafo assunto come orientato
    (implementato con liste di incidenza).
    """

    @staticmethod
    def kruskal(graph):
        """Algoritmo di Kruskal per la ricerca del minimo albero ricoprente.

        Variante implementativa che utilizza strutture union-find.
        """
        uf = UnionFind()
        edges = GraphHelper.sortEdges(graph)  #lista di archi ordinato per peso
        mstEdges = []   #lista di archi scelti per il minimo albero ricoprente
        uf = UnionFind()
        for i in range(len(graph.nodes)):
            uf.makeset(graph.nodes[i])   #makeset per ogni nodo del grafo
        mstWeight = 0   #contatore per mantenere il peso totale del mst
        for edge in edges:   #cerca le due strutture
            r1 = uf.findRoot(uf.nodes[edge.tail])
            r2 = uf.findRoot(uf.nodes[edge.head])
            if r1 != r2:   #fondile se non sono gia' unite e aggiungi l'arco
                           #corrente al mst
                uf.union(r1, r2)
                mstEdges.append(edge)
                mstWeight += edge.weight
        return mstWeight, mstEdges

    @staticmethod
    def prim(graph):
        """Algoritmo di Prim per la ricerca del minimo albero ricoprente.

        Variante che utilizza un albero binario per la gestione della frontiera
        tramite coda con priorita'.
        """
        n = len(graph.nodes)
        currentWeight = n * [INFINITE]  #imposta il peso degli archi a infinito
        pq = PriorityQueue()   #rappresenta la frontiera dell'albero generato
        root = 0    #scelgo arbitrariamente il nodo 0 come radice
        currentWeight[root] = 0

        mstNodes = set()  #insieme dei nodi correnti inclusi nella soluzione

        #inizializzazione dell'albero
        treeNode = TreeArrayListNode(root)
        tree = TreeMod(treeNode)
        mstNodes.add(root)

        #inizializzazione pq
        pq.insert((root,Edge(root,root,0)), 0)  #triviale
        mstWeight = 0

        while not pq.isEmpty():
            vertex = pq.findMin()
            pq.deleteMin()
            if(vertex[0]) not in mstNodes:   #nodo non ancora aggiunto al mst
                #aggiornare albero e peso mst
                connectingEdge = vertex[1]
                treeNode = TreeArrayListNode(vertex[0])
                father = tree.foundNodeByElem(connectingEdge.tail)
                father.sons.append(treeNode)
                treeNode.father = father
                mstNodes.add(vertex[0])
                mstWeight += connectingEdge.weight
            #print(currentWeight)

            currNode = graph.inc[vertex[0]].getFirstRecord()
            while currNode != None:    #scorre tutti gli archi incidenti
                #semplici variabili per semplificare il codice
                edge = currNode.elem
                head = edge.head
                tail = edge.tail
                weight = edge.weight
                currWeight = currentWeight[head]

                if head not in mstNodes: #inserisco solo i nodi che portano
                                         #verso vertici non ancora scelti
                    pq.insert((head, edge), weight)
                    if currWeight == INFINITE:
                        currentWeight[head] = weight
                    elif weight < currWeight:
                        currentWeight[head] = weight
                currNode = currNode.next
        return mstWeight, tree


def main():
    g = GraphHelper.buildGraph()
    print("The graph:")
    g.printGraph()

    print("\nKruskal:")
    w, mst = MST.kruskal(g)
    print("weight:", w)
    print("list of edges:")
    print([str(item) for item in mst])

    print("Prim:")
    w2, mst = MST.prim(g)
    print("weight:", w2)
    bfs = mst.BFS()
    print("BFS on returning mst:")
    print([str(item) for item in bfs])

    if(w == w2):
        print("Computato stesso peso dai 2 algoritmi.")
    else:
        print("Error! I due algoritmi tornano un peso totale differente!")

if __name__ == "__main__":
    main()
