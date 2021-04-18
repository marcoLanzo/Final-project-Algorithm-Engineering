#!/usr/bin/env python
#encoding: utf-8
import sys
sys.path.append("../../")
from dictionary_tree.dictionary.dictTrees.trees.treeArrayList \
        import TreeArrayListNode

class TreeNodeMod(TreeArrayListNode):
    def __init__(self, info):
        super().__init__(info)
        self.realFather = None
