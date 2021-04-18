#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../")
from sorting.Sorting import quickSort
from graph.Graph_IncidenceList import GraphIncidenceList as Graph
from tree.CmpEdge import CmpEdge


class GraphHelper():
    """Questa classe contiene alcuni metodi utili alla gestione di un grafo"""

    @staticmethod
    def sortEdges(graph):
        """Ritorna una lista ordinata di archi del grafo"""
        l = []
        for i in range(len(graph.nodes)):
            curr = graph.inc[i].getFirstRecord()
            while curr != None:
                edge = CmpEdge(curr.elem.tail, curr.elem.head\
                        , curr.elem.weight)
                if edge.head < edge.tail:   #sto prendendo solo meta' dei nodi
                    l.append(edge)
                curr = curr.next
        quickSort(l)
        return l
    @staticmethod
    def buildGraph():
        """Costruisce un grafo tramite liste di incidenza."""
        g = Graph()
        ginfo = ((0, 1, 3.0), (0, 3, 1.0), (1, 3, 2.0), (1, 2, 4.0)\
                , (2, 3, 5.0))
        n = []
        for i in range(4):
            n.append(g.insertNode(i))
        for e in ginfo:
            g.insertEdge(n[e[0]].index, n[e[1]].index, e[2])
            g.insertEdge(n[e[1]].index, n[e[0]].index, e[2])
        return g

    @staticmethod
    def cleanGraph(graph):
        """Rende un qualsiasi grafo connesso ed elimina archi multipli."""
        node_index = 0
        w = len(graph.nodes) * 100
        for _ in graph.inc.values():
            graph.inc[node_index].addAsLast(Edge(node_index,\
                    (node_index + 1) % len(graph.nodes), w))
            graph.inc[(node_index + 1) % len(graph.nodes)]\
                    .addAsLast(Edge((node_index + 1) % len(graph.nodes),\
                    node_index, w))
            w += 1
            node_index += 1
#        graph.printGraph()
        for inc in graph.inc.values():
            heads = []
            curr = inc.getFirstRecord()
            while curr != None:
                if curr.elem.head not in heads:
                    heads.append(curr.elem.head)
                else:
                    inc.deleteRecord(curr)
                curr = curr.next

    @staticmethod
    def clean_graph_AdjMatrix(graph):
        """Rende un qualsiasi grafo connesso."""
        node_index = 0
        w = len(graph.nodes) * 100
        for _ in graph.nodes:
            node2 = (node_index + 1) % len(graph.nodes)
            if graph.adj[node_index][node2] !=GraphAdjacencyMatrix.EMPTY:
                graph.adj[node_index][node2] = w
                graph.adj[node2][node_index] = w
            w += 1
            node_index += 1

if __name__ == "__main__":
    print("I moduli sono stati importati correttamente. Nessun test presente.")
