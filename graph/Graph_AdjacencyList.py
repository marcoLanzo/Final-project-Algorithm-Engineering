#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../")
from strutture.linked_ds.list.DoubleLinkedList import ListaDoppiamenteCollegata as Lista
from elements import Node
from dictionary_tree.dictionary.dictTrees.trees.treeArrayList \
        import TreeArrayList, TreeArrayListNode
from tree.Tree import Tree
from Graph import Graph
from abc import abstractmethod

class GraphAdjacencyList(Graph):

    def __init__(self):
        super().__init__()
        self.adj = None

    def isAdj(self, tail, head):
        if super().isAdj(tail, head) == True:
            curr = self.adj[tail].getFirstRecord()
            while curr != None:
                nodeIndex = curr.elem
                if nodeIndex == head:
                    return True
                curr = curr.next
        return False

    def insertNode(self, elem):
        newnode = super().insertNode(elem)
        if self.nodes == None:
            self.nodes = {newnode.index : newnode}   #inizializza dizionario
            self.adj = {newnode.index : Lista()}
        else:
            self.nodes[newnode.index] = newnode   #aggiungi nodo al dizionario
            self.adj[newnode.index] = Lista()

        return newnode

    def deleteNode(self, index):
        found = False
        for node in self.nodes.items():
            if index == node[0]:
                found = True
                break
        if not found:
            return
        del self.nodes[index]
        del self.adj[index]
        # Controlla TUTTE le liste di adiacenza e cancella gli archi che 
        #puntano al nodo eliminato.
        for adj in self.adj.values():
            curr = adj.getFirstRecord()
            while curr != None:
                if curr.elem == index:
                    adj.deleteRecord(curr)
                curr = curr.next

    def insertEdge(self, tail, head):
        if head in self.nodes and tail in self.nodes:
            self.adj[tail].addAsLast(head)

    def deleteEdge(self, tail, head):
        if head in self.nodes and tail in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr != None:
                if curr.elem == head:
                    self.adj[tail].deleteRecord(curr)
                curr=curr.next

    def foundNodesBySource(self, tail):
        nodes = []
        curr = self.adj[tail].getFirstRecord()
        while curr != None:
            nodes.append(curr.elem)
            curr = curr.next
        return nodes



    def printGraph(self):
        print("Liste di adiacenza:")
        for p in self.adj.items():
            print(str(p[0]) + ":")
            l = p[1]
            if l.first == None:
                print("[]")
            else:
                s = "["
                current = l.first
                while current != None:
                    if len(s) > 1:
                        s += ", "
                    s += "(" + str(current.elem)+ ")"
                    current = current.next
                s += "]"
                print(s)

if __name__ == "__main__":
        myGraph = GraphAdjacencyList()
        nodo0 = myGraph.insertNode(0)
        print("nodo0=insertNodo(0)")
        nodo1 = myGraph.insertNode(2)
        print("nodo1=insertNodo(2)")
        nodo2 = myGraph.insertNode(4)
        print("nodo2=insertNodo(4)")
        nodo3 = myGraph.insertNode(6)
        print("nodo3=insertNodo(6)")
        nodo4 = myGraph.insertNode(8)
        print("nodo4=insertNodo(8)")
        nodo5 = myGraph.insertNode(10)
        print("nodo5=insertNodo(10)\n")

        myGraph.insertEdge(nodo0.index, nodo2.index)
        print("insertEdge(nodo0,nodo2)")
        myGraph.insertEdge(nodo3.index, nodo4.index)
        print("insertEdge(nodo3,nodo4)")
        myGraph.insertEdge(nodo0.index, nodo1.index)
        print("insertEdge(nodo0,nodo1)")
        myGraph.insertEdge(nodo4.index, nodo3.index)
        print("insertEdge(nodo4,nodo3)")
        myGraph.insertEdge(nodo5.index, nodo1.index)
        print("insertEdge(nodo5,nodo1)")
        myGraph.insertEdge(nodo5.index, nodo4.index)
        print("insertEdge(nodo5,nodo4)")
        myGraph.insertEdge(nodo2.index, nodo3.index)
        print("insertEdge(nodo2,nodo3)\n")

        myGraph.printGraph()

        print("adiacente(nodo0,nodo2)=" + str(myGraph.isAdj(nodo0.index,\
                nodo2.index)))
        print("adiacente(nodo5,nodo2)=" + str(myGraph.isAdj(nodo5.index,\
                nodo2.index)))

        print("\ngenericSearch da nodo0"        )
        tree = myGraph.genericSearch(nodo0)
        s = tree.BFS()
        print([str(item) for item in s])

        myGraph.deleteNode(nodo2.index)
        print("\ndeleteNodo(nodo2)")
        myGraph.printGraph()

        myGraph.deleteEdge(nodo4.index, nodo3.index)
        print("deleteEdge(nodo4,nodo3)")
        myGraph.printGraph();


        myGraph.deleteNode(nodo3.index)
        print("deleteNodo(nodo3)")
        myGraph.deleteNode(nodo0.index)
        print("deleteNodo(nodo0)")
        myGraph.deleteNode(nodo1.index)
        print("deleteNodo(nodo1)")
        myGraph.printGraph()

