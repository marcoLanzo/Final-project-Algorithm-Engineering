#!/usr/bin/env python
#encoding: utf-8
from abc import ABCMeta, abstractmethod
from elements import Node
import sys
sys.path.append("../")
from dictionary_tree.dictionary.dictTrees.trees.treeArrayList \
        import TreeArrayList, TreeArrayListNode
from tree.Tree import Tree

class Graph(metaclass=ABCMeta):
    """Rappresenta un grafo e le operazioni minime da implementare.

    Questa classe non puo' essere istanziata. Tramite una sotto-classe i metodi
    astratti devono essere implementati.
    """
    def __init__(self):
        self.nodes = None
        self.nextId = 0

    @abstractmethod
    def isAdj(self, tail, head):
        """Controlla che due nodi siano adiacenti."""
        if self.nodes == None:
            return False
        if not head in self.nodes or not tail in self.nodes:
            return False
        return True   #questo metodo fa solo un check sull'esistenza dei nodi.

    @abstractmethod
    def insertNode(self, elem):
        newnode = Node(self.nextId, elem)
        self.nextId += 1
        return newnode

    @abstractmethod
    def deleteNode(self, index):
        ...

    @abstractmethod
    def insertEdge(self, tail, head, weight=None):
        ...

    @abstractmethod
    def deleteEdge(self, tail, head):
        ...

    #@abstractmethod
    #def foundNodesBySource(self, tail):
    #    ...

    def genericSearch(self, root):
        treeNode = TreeArrayListNode(root)
        tree = Tree(treeNode)
        vertexSet = set()   #nodi da esaminare
        markedNodes = set()   #nodi gia' marcati per essere esaminati
        markedNodes.add(root.index)
        vertexSet.add(treeNode)
        while len(vertexSet) > 0:  #finche' ci sono nodi da esaminare
            treeNode = vertexSet.pop()   #un generico nodo non esaminato
            nodes = self.foundNodesBySource(treeNode.info.index)
            for nodeIndex in nodes:
                if nodeIndex not in markedNodes:   #crea il nodo per l'albero e
                                                  #collega padre e figlio
                    newTreeNode = TreeArrayListNode(self.nodes[nodeIndex])
                    markedNodes.add(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                else:
                    currNode = tree.foundNodeByIndex(nodeIndex)
                    #TODO: aggiorna il padre 
        return tree

    @abstractmethod
    def printGraph(self):
        ...

if __name__ == "__main__":
    myGraph = Graph()
