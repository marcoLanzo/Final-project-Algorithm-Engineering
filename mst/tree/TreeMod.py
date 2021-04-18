#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../../")
from dictionary_tree.dictionary.dictTrees.trees.treeArrayList \
        import TreeArrayList
from dictionary_tree.dictionary.dictTrees.trees.strutture.Stack \
        import PilaArrayList
from graph.tree.Tree import Tree

class TreeMod(Tree):
    def foundNodeByElem(self, elem):
        """Visita DFS per cercare un nodo che contenga l'indice richiesto."""
        stack = PilaArrayList()
        if self.root != None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            if elem == current.info:
                return current
            for i in range(len(current.sons)):
                stack.push(current.sons[i])
        return None

if __name__ == "__main__":
    print("I moduli sono importati correttamente, nessun test presente.")
