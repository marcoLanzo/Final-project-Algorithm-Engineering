#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../")
from elements import Node
from tree.Tree import Tree
from dictionary_tree.dictionary.dictTrees.trees.treeArrayList \
        import TreeArrayListNode
from Graph import Graph

class GraphAdjacencyMatrix(Graph):
    EMPTY = 0

    def __init__(self):
        super().__init__()
        self.nodes = []
        self.adj = []

    def isAdj(self, tail, head):
        if tail < 0 or tail >= len(self.adj) or head < 0\
                or head >= len(self.adj):
            return False
        return self.adj[tail][head] != GraphAdjacencyMatrix.EMPTY

    def insertNode(self, elem):
        newnode = super().insertNode(elem)
        self.nodes.append(newnode)
        #Aggiorna la matrice
        self.adj.append(len(self.adj) * [GraphAdjacencyMatrix.EMPTY])
        for l in self.adj:
            l.append(GraphAdjacencyMatrix.EMPTY)
        return newnode

    def insertEdge(self, tail, head, weight=None):
        if tail < 0 or tail >= len(self.adj) or head < 0\
                or head >= len(self.adj):
            return
        self.adj[tail][head] = weight

    def deleteEdge(self, tail, head):
        if tail < 0 or tail >= len(self.adj) or head < 0\
                or head >= len(self.adj):
            return
        self.adj[tail][head] = GraphAdjacencyMatrix.EMPTY

    def deleteNode(self, index):
        """Cancella un nodo.

        Dopo aver cancellato il nodo e le relative celle nella matrice di
        adiacenza, aggiorna anche gli indici di tutti i restanti nodi.
        """
        if index < 0 or index >= len(self.adj):
            return

        del self.nodes[index]
        for i in range(index, len(self.nodes)):   #aggiorna gli indici
            self.nodes[i].index = i
        self.nextId=len(self.nodes)

        del self.adj[index]    #aggiorna la matrice
        for l in self.adj:
            del l[index]


    def foundNodesBySource(self, index):
        l = []
        for j in range(len(self.adj)):
            if self.adj[index][j] != GraphAdjacencyMatrix.EMPTY:
                l.append(j)
        return l

    def printGraph(self):
        print("matrix:")
        s = "    "
        for n in self.nodes:
            s += str(n.index)+ "   "
        s += "\n"
        count = 0
        for a in self.adj:
            s += str(count)+ " "
            for c in a:
                if c == GraphAdjacencyMatrix.EMPTY:
                    s += " -- "
                else:
                    s += str(c) + " "
            count += 1
            s += "\n"
        print(s)

if __name__ == "__main__":
        G = GraphAdjacencyMatrix();

        nodo0 = G.insertNode(0)
        print("nodo0=insertNodo(0)")
        nodo1 = G.insertNode(1)
        print("nodo1=insertNodo(1)")
        nodo2 = G.insertNode(2)
        print("nodo2=insertNodo(2)")
        nodo3 = G.insertNode(3)
        print("nodo3=insertNodo(3)")
        nodo4 = G.insertNode(4)
        print("nodo4=insertNodo(4)")
        nodo5 = G.insertNode(5)
        print("nodo5=insertNodo(5)")

        G.insertEdge(nodo0.index, nodo2.index, 2.3)
        print("insertEdge(nodo0,nodo2,2.3)")
        G.insertEdge(nodo3.index, nodo4.index, 1.4)
        print("insertEdge(nodo3,nodo4,1.4)")
        G.insertEdge(nodo0.index, nodo1.index, 8.1)
        print("insertEdge(nodo0,nodo1,8.1)")
        G.insertEdge(nodo4.index, nodo3.index, 6.4)
        print("insertEdge(nodo4,nodo3,6.4)")
        G.insertEdge(nodo5.index, nodo1.index, 6.2)
        print("insertEdge(nodo5,nodo1,6.2)")
        G.insertEdge(nodo5.index, nodo4.index, 4.1)
        print("insertEdge(nodo5,nodo4,4.1)")
        G.insertEdge(nodo2.index, nodo3.index, 2.2)
        print("insertEdge(nodo2,nodo3,2.2)")

        G.printGraph()

        print("adiacente(nodo0,nodo2)=" \
                + str(G.isAdj(nodo0.index, nodo2.index)))
        print("adiacente(nodo5,nodo2)=" \
                + str(G.isAdj(nodo5.index, nodo2.index)))


        tree = G.genericSearch(nodo0)
        s = tree.BFS()
        print("generic search from node 0")
        print([str(item) for item in s])

        G.deleteNode(nodo2.index)
        print("deleteNodo(nodo2)")
        G.printGraph()

        G.deleteEdge(nodo4.index, nodo3.index)
        print("deleteEdge(nodo4,nodo3)")
        #print("deleteEdge(nodo{},nodo{})".format(nodo4.index,nodo3.index))
        G.printGraph();


        G.deleteNode(nodo3.index)
        print("deleteNodo(nodo3)")
        G.deleteNode(nodo0.index)
        print("deleteNodo(nodo0)")
        G.deleteNode(nodo1.index)
        print("deleteNodo(nodo1)")
        G.printGraph()

