#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../")
from linked_ds.list.DoubleLinkedList import ListaDoppiamenteCollegata as Lista
from elements import Node, Edge
from dictionary_tree.dictionary.dictTrees.trees.treeArrayList \
        import  TreeArrayListNode
from dictionary_tree.dictionary.dictTrees.trees.strutture.Stack \
        import PilaArrayList
from tree.Tree import Tree
from Graph import Graph

class GraphIncidenceList(Graph):
    def __init__(self):
        super().__init__()
        self.inc = None

    def isAdj(self, tail, head):
        if super().isAdj(tail, head) == True:
            curr = self.inc[tail].getFirstRecord()
            while curr != None:  #controlla nella lista di incidenza della
                                 #sorgente che ci sia il nodo destinazione
                edge = curr.elem
                if edge.head == head:
                    return True
                curr = curr.next
        return False

    def insertNode(self, elem):
        newnode = super().insertNode(elem)
        if self.nodes == None:  #crea nuovi dizionari
            self.nodes = {newnode.index : newnode}
            self.inc = {newnode.index : Lista()}
        else:   #aggiungi ai dizionari esistenti
            self.nodes[newnode.index] = newnode
            self.inc[newnode.index] = Lista()
        return newnode

    def deleteNode(self, index):
        found = False
        for node in self.nodes.items():
            if index == node[0]:
                found = True   #TODO e' possibile cancellare qui il nodo?
                break
        if not found:
            return
        del self.nodes[index]
        del self.inc[index]

        # Controlla TUTTE le liste di incidenza e cancella gli archi che 
        #puntano al nodo eliminato. E' in generale molto lento.
        for inc in self.inc.values():
            curr = inc.getFirstRecord()
            while curr != None:
                if curr.elem.head == index:
                    inc.deleteRecord(curr)   #TODO perche' funziona?
                curr = curr.next

    def insertEdge(self, tail, head, weight=None):
        if head in self.nodes and tail in self.nodes:
            self.inc[tail].addAsLast(Edge(tail, head, weight))

    def deleteEdge(self, tail, head):
        if head in self.nodes and tail in self.nodes:
            curr = self.inc[tail].getFirstRecord()
            while curr != None:
                if curr.elem.head == head:
                    self.inc[tail].deleteRecord(curr)
                    #break   #TODO e' utile questa istruzione?
                curr=curr.next

    def foundNodesBySource(self, tail):
        nodes = []
        curr = self.inc[tail].getFirstRecord()
        while curr != None:
            nodes.append(curr.elem.head)
            curr = curr.next
        return nodes


    def printGraphFast(self):
        """Stampa liste di incidenza sfruttando il metodo __str__() di Edge."""
        for incidentList in self.inc.items():
            print(str(incidentList[0]) + ":")
            listNode = incidentList[1].getFirstRecord()
            s = ''
            while listNode!= None:
                s += str(listNode.elem)
                listNode = listNode.next
            print('[' + s + ']')

    def printGraph(self):
        print("Liste di incidenza:")
        for p in self.inc.items():
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
                    s += "(" + str(current.elem.tail) + ", " + \
                            str(current.elem.head) + ", " + \
                            str(current.elem.weight) + ")"
                    current = current.next
                s += "]"
                print(s)

if __name__ == "__main__":
        myGraph = GraphIncidenceList();

        nodo0 = myGraph.insertNode(0)
        print("nodo0=insertNodo(0)")
        nodo1 = myGraph.insertNode(1)
        print("nodo1=insertNodo(1)")
        nodo2 = myGraph.insertNode(2)
        print("nodo2=insertNodo(2)")
        nodo3 = myGraph.insertNode(3)
        print("nodo3=insertNodo(3)")
        nodo4 = myGraph.insertNode(4)
        print("nodo4=insertNodo(4)")
        nodo5 = myGraph.insertNode(5)
        print("nodo5=insertNodo(5)\n")

        myGraph.insertEdge(nodo0.index, nodo2.index, 2.3)
        print("insertEdge(nodo0,nodo2,2.3)")
        myGraph.insertEdge(nodo3.index, nodo4.index, 1.4)
        print("insertEdge(nodo3,nodo4,1.4)")
        myGraph.insertEdge(nodo0.index, nodo1.index, 8.1)
        print("insertEdge(nodo0,nodo1,8.1)")
        myGraph.insertEdge(nodo4.index, nodo1.index, 6.4)
        print("insertEdge(nodo4,nodo1,6.4)")
        myGraph.insertEdge(nodo5.index, nodo1.index, 6.2)
        print("insertEdge(nodo5,nodo1,6.2)")
        myGraph.insertEdge(nodo5.index, nodo4.index, 4.1)
        print("insertEdge(nodo5,nodo4,4.1)")
        myGraph.insertEdge(nodo2.index, nodo3.index, 2.2)
        print("insertEdge(nodo2,nodo3,2.2)\n")

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
        print("\ndeleteEdge(nodo4,nodo3)")
        myGraph.printGraph();

        myGraph.deleteNode(nodo3.index)
        print("\ndeleteNodo(nodo3)")
        myGraph.deleteNode(nodo0.index)
        print("deleteNodo(nodo0)")
        myGraph.deleteNode(nodo1.index)
        print("deleteNodo(nodo1)")
        myGraph.printGraph()

