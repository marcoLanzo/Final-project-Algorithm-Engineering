#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../../")
from graph.elements import Edge

class CmpEdge(Edge):
    """Estende un oggetto di tipo Edge tramite 'rich comparison operators'.

    Un arco potra' quindi essere comparato ad un altro arco tramite
    operatori quali >, <, ==, etc..
    """
    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return not self.weight == other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

def main():
        print("Compare different edges:")
        edges = []
        #edge1 = CmpEdge( 1, 2)  #arco non pesato(weight=None)
        edge2 = CmpEdge( 1, 2, 2)
        edge3 = CmpEdge( 1, 2, 3)
        #edges.append(edge1)
        edges.append(edge2)
        edges.append(edge3)
        for i in range(len(edges)):
            print("edge " + str(i) + " : ", edges[i])

        input("\nwhat happen comparing these edges?..think about it then"\
                " press enter button.")

        for i in range(len(edges)):
            for j in range(i, len(edges)):
                    print("edge "+ str(i) + " == " + str(j) +\
                            "? " + str(edges[i] == edges[j]))
                    print("edge "+ str(i) + " != " + str(j)\
                            + "? " + str(edges[i] != edges[j]))
                    print("edge "+ str(i) + " > " + str(j)\
                            + "? " + str(edges[i] > edges[j]))
                    print("edge "+ str(i) + " >="\
                            + " edge " + str(j) + "? "\
                            + str(edges[i] >= edges[j]))
                    print("edge "+ str(i) + " < " + str(j)\
                            + "? " + str(edges[i] < edges[j]))
                    print("edge "+ str(i) + " <="\
                            + " edge " + str(j) + "? "\
                            + str(edges[i] <= edges[j]))
if __name__ == "__main__":
    main()
