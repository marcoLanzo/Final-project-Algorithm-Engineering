#!/usr/bin/env python
#encoding: utf-8
class Node:
    def __init__(self, index, elem):
        self.index = index
        self.elem = elem

    def __str__(self):
        return  str(self.elem)

class Edge:
    def __init__(self, tail, head, weight=None):
        self.head = head  #indice del nodo destinazione
        self.tail = tail  #indice del nodo sorgente
        self.weight = weight  #peso dell'arco


if __name__ == "__main__":
    node = Node(0, "casa")
    print('creato nodo', node)
    edge = Edge(0, 1, 1.5)
    print('creato arco (' , edge.tail , ', ' , edge.head, ', ' \
            , edge.weight , ')')  #TODO: brutto esempio di stampa
